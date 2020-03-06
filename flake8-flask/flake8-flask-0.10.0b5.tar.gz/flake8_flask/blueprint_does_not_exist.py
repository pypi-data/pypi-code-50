import ast
import json
import logging
import sys
import os
from typing import List, Set, Dict, Optional, Any

from flake8_flask.constants import MODULE_NAME
from flake8_flask.flask_base_visitor import FlaskBaseVisitor
from flake8_flask.upsell_blueprint import FlaskDecoratorVisitor

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(stream=sys.stderr)
handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
logger.addHandler(handler)

# What we'll need to do is:
# 1. Find all the Blueprints that are created. Track their string name and variable name.
# 2. Find all the Blueprints that are registered. Filter out created blueprints that are not registered.
# 3. Find all call sites of 'url_for' and resolve the Blueprint naming scheme to registered blueprints.
#   3a. Fire if 'url_for' doesn't resolve.

# However, since flake8 only runs on a per-file basis, I'll need to hack
# this scheme a little bit.
# BlueprintDoesNotExistVisitor will look for the creation of a Flask app,
# and without a Flask app name won't run.
# If it has a Flask app, it will look for calls to register_blueprint.
# Then it will try and resolve the filenames of the blueprints.
# BlueprintDoesNotExistVisitor will then run BlueprintVisitor on that file
# to look for the actual name of the blueprint.
# BlueprintVisitor will also look for all invocations of url_for and keep
# track of the arguments.
# BlueprintVisitor will return the names of blueprints and url_for's.


class UrlForLookup:
    def __init__(self, node: ast.Str, filename: str):
        self.node = node
        self.filename = filename

    def __str__(self):
        return f"{self.filename} {self.node.s}"

    def __hash__(self):
        return hash(self.__str__())

    def json(self):
        return json.dumps(
            {
                "filename": self.filename,
                "lookup": self.node.s,
                "line": self.node.lineno,
                "col": self.node.col_offset,
            }
        )


class BaseBlueprintVisitor(FlaskBaseVisitor):
    def __init__(self):
        self.url_for_lookups = []
        self.blueprints = {}
        self.flask_app_name = None
        super(BaseBlueprintVisitor, self).__init__()

    def _is_url_for(self, call_node: ast.Call) -> bool:
        fxn = "url_for"
        if self.is_node_method_alias_of(call_node, fxn, MODULE_NAME):
            logger.debug("Found url_for")
            return True
        return False

    def _is_caller_flask_app(self, attr_node: ast.Attribute) -> bool:
        """Check to see if the left-hand-side of a Attribute is a Flask app."""
        if not self.flask_app_name:
            logger.debug("Flask app name has not been discovered.")
            return False

        if not isinstance(attr_node, ast.Attribute):
            return False

        if not isinstance(attr_node.value, ast.Name):
            logger.debug("Caller is not a Name node")
            return False

        caller = attr_node.value.id
        if caller != self.flask_app_name:
            logger.debug(
                f"This isn't the Flask app. caller: {caller}; Flask app name: {self.flask_app_name}"
            )
            return False

        return True


class BlueprintVisitor(BaseBlueprintVisitor):
    def __init__(self, filename: str):
        self.blueprint_lookup = {}
        self.filename = filename
        super(BlueprintVisitor, self).__init__()

    def _get_route_prefix(self, decorator: Any) -> Optional[str]:
        if not isinstance(decorator, ast.Call):
            return None
        elif not isinstance(decorator.func, ast.Attribute):
            return None
        elif decorator.func.attr != "route":
            return None
        elif not isinstance(decorator.func.value, ast.Name):
            return None
        logger.debug(f"Blueprint route prefix: {decorator.func.value.id}")
        return decorator.func.value.id

    def visit_Assign(self, assign_node: ast.Assign):
        """Gathers Blueprint names and url_for's."""
        rhs = assign_node.value
        if not isinstance(rhs, ast.Call):
            logger.debug("Not a call node; abort!")
            return

        if self.is_node_method_alias_of(rhs, "Flask", MODULE_NAME):
            try:
                self.flask_app_name = assign_node.targets[0].id
            except Exception:
                logger.error(
                    "Nice try, you thought you could take a shortcut! Fixup this."
                )
        elif self.is_node_method_alias_of(rhs, "Blueprint", MODULE_NAME):
            try:
                blueprint_variable_name = assign_node.targets[0].id
                blueprint_string_name = rhs.args[0].s
                logger.debug(f"Found Blueprint: {blueprint_string_name}")
                self.blueprint_lookup[blueprint_variable_name] = blueprint_string_name
                self.blueprints[blueprint_string_name] = []
            except Exception as e:
                logger.error(f"Error dealing with Blueprint. Error: {e}")

        self.generic_visit(assign_node)

    def visit_Call(self, call_node: ast.Call):
        if self._is_url_for(call_node):
            url_for_lookup = call_node.args[0]
            self.url_for_lookups.append(
                UrlForLookup(node=url_for_lookup, filename=self.filename)
            )
        self.generic_visit(call_node)

    def visit_FunctionDef(self, def_node: ast.FunctionDef):
        for decorator in def_node.decorator_list:
            if isinstance(decorator, ast.Call) and not self._is_caller_flask_app(
                decorator.func
            ):
                route_prefix = self._get_route_prefix(decorator)
                if route_prefix:
                    try:
                        blueprint_string_name = self.blueprint_lookup[route_prefix]
                    except KeyError:
                        logger.debug(
                            f"Assuming {route_prefix} is the Flask app. Skipping..."
                        )
                        return
                    self.blueprints[blueprint_string_name].append(def_node.name)
        self.generic_visit(def_node)


class BlueprintDoesNotExistVisitor(BaseBlueprintVisitor):
    def __init__(self, filename: str):
        self.base_path = os.path.dirname(os.path.realpath(filename))
        self.filename = filename
        super(BlueprintDoesNotExistVisitor, self).__init__()

    name = "r2c-flask-blueprint-does-not-exist"

    def _is_register_blueprint(self, call_node: ast.Call) -> bool:
        """Check to see if this Call is 'app.register_blueprint'."""
        if not isinstance(call_node.func, ast.Attribute):
            logger.debug("Not app.register_blueprint. Abandoning...")
            return False

        if not self._is_caller_flask_app(call_node.func):
            logger.debug("Not a flask app! No need to continue.")
            return False

        return call_node.func.attr == "register_blueprint"

    def _is_blueprint_defined_in_same_file(self, blueprint_variable_name: str) -> bool:
        symbol = self._symbol_lookup(blueprint_variable_name)
        logger.debug(f"Symbol lookup for '{blueprint_variable_name}': {symbol}")
        if symbol:
            return True
        return False

    def _resolve_blueprint_file(self, blueprint_variable_name: str) -> List[str]:
        """Infer blueprint filename from import"""
        for module in self.modules:
            if blueprint_variable_name in self.methods[module]:
                logger.debug(
                    f"module: {module}; blueprint_variable_name: {blueprint_variable_name}"
                )
                guessed_file = os.path.join(
                    self.base_path,
                    *module.split(".")[1:-1],
                    module.split(".")[-1] + ".py",
                )
                if os.path.exists(guessed_file):
                    return [guessed_file]

                # If not, try again with __init__
                guessed_file = os.path.join(
                    self.base_path, *module.split(".")[1:], "__init__.py"
                )
                if os.path.exists(guessed_file):
                    # Assume that the blueprint definition is spread out in the module.
                    module_dir = os.path.dirname(guessed_file)
                    module_files = os.listdir(module_dir)
                    module_files = list(
                        filter(lambda path: path.endswith(".py"), module_files)
                    )
                    return [os.path.join(module_dir, f) for f in module_files]
        logger.info(
            f"Could not find the file where the blueprint '{blueprint_variable_name}' is defined."
        )
        return []

    def _run_blueprint_visitor(self, blueprint_file_paths: List[str]):
        """
        Run BlueprintVisitor on the file.
        Collect blueprint names and url_for's.
        """
        blueprint_visitor = BlueprintVisitor(self.filename)
        for blueprint_file_name in blueprint_file_paths:
            with open(blueprint_file_name, "r") as fin:
                try:
                    tree = ast.parse(fin.read())
                except SyntaxError as e:
                    logger.warning(
                        f"Could not parse {blueprint_file_name}. Skipping. {e}"
                    )
                    return
            blueprint_visitor.visit(tree)
            self.url_for_lookups.extend(blueprint_visitor.url_for_lookups)
            self.blueprints.update(blueprint_visitor.blueprints)
            logger.debug(
                f"After running BlueprintVisitor: self.url_for_lookups: {[n.node.__dict__.get('s') for n in self.url_for_lookups]}; self.blueprints: {self.blueprints}"
            )

    def _get_invalid_lookups(self) -> Set[str]:
        # For url_fors, check blueprints
        invalid_lookups = []
        for url_for_lookup_obj in self.url_for_lookups:
            url_for_lookup = url_for_lookup_obj.node.s
            logger.debug(f"Checking validity of url_for route: {url_for_lookup}")
            if self._is_invalid_url_for_lookup(url_for_lookup):
                invalid_lookups.append(url_for_lookup_obj)
        return set(invalid_lookups)

    def _is_invalid_url_for_lookup(self, url_for_lookup: str) -> bool:
        if "." not in url_for_lookup:
            logger.debug(f"{url_for_lookup} is not a blueprint lookup.")
            return False
        try:
            blueprint_name, blueprint_route = url_for_lookup.split(".")
        except ValueError:
            logger.info(
                f"Blueprint lookup in 'url_for' does not have two fields, which we do not support: {url_for_lookup}"
            )
            return False
        if blueprint_name == "":
            # We've encountered something like '.login'.
            # Approximate by checking all the routes we have for mispellings.
            # Flatten the list of values
            all_routes = [
                route for sublist in self.blueprints.values() for route in sublist
            ]
            if blueprint_route not in all_routes:
                logger.debug(f"Cannot find route '{blueprint_route}'.")
                return True
        elif blueprint_name not in self.blueprints:
            logger.debug(f"Blueprint '{blueprint_name}' not found")
            return True
        elif blueprint_route not in self.blueprints[blueprint_name]:
            logger.debug(
                f"Blueprint route '{blueprint_name}.{blueprint_route}' not found"
            )
            return True
        return False

    def visit_Assign(self, assign_node: ast.Assign):
        """
        Retrieves the name of the Flask app.
        """
        rhs = assign_node.value
        if not isinstance(rhs, ast.Call):
            logger.debug("Not a call node; abort!")
            return

        if not self.is_node_method_alias_of(rhs, "Flask", MODULE_NAME):
            logger.debug("Not 'flask.Flask'. Moving along.")
            return

        try:
            self.flask_app_name = assign_node.targets[0].id
        except Exception:
            logger.error("Nice try, you thought you could take a shortcut! Fixup this.")

        self.generic_visit(assign_node)

    def visit_Call(self, call_node: ast.Call):
        if self._is_register_blueprint(call_node):
            if not isinstance(call_node.args[0], ast.Name):
                return
            blueprint_variable_name = call_node.args[0].id

            logger.debug(f"Running blueprint on Flask app file.")
            self._run_blueprint_visitor([os.path.join(self.base_path, self.filename)])

            blueprint_files = self._resolve_blueprint_file(blueprint_variable_name)
            logger.debug(f"Guessing blueprint files: {blueprint_files}")
            self._run_blueprint_visitor(blueprint_files)

        self.generic_visit(call_node)

    def _generate_message(self, url_for_lookup: UrlForLookup, extra=False) -> str:
        """
        Because flake8 only runs checks per-file, this check hacks things a bit by running on other
        files. This function is here to handle the case where a finding is reported in another filename
        besides the flake8 target file.
        Set extra to True if we end up running in to this case.
        This is for future-proofing.
        """
        message = f"{self.name} Invalid url_for blueprint: '{url_for_lookup.node.s}' found in file '{url_for_lookup.filename}'. This will cause a runtime error upon lookup. Check to make sure everything is spelled correctly."
        if extra:
            message += " EXTRA: {json.dumps(url_for_lookup.json())}"
        return message

    def _nuke_line_number(self, url_for_lookup: UrlForLookup) -> ast.Str:
        """
        Set lineno and col_offset to 0 if the finding doesn't come from the
        flake8 target file.
        """
        n = url_for_lookup.node
        if url_for_lookup.filename != self.filename:
            n.lineno = 0
            n.col_offset = 0
        return n

    def post_run(self):
        """
        This will run in main.py after visit() has been called.
        Use this for any post-processing you'll need to do after linting a file.
        """
        invalid_lookups = self._get_invalid_lookups()
        for invalid_lookup in invalid_lookups:
            self._nuke_line_number(invalid_lookup)
            message = self._generate_message(invalid_lookup)
            self.report_nodes.append(
                {"node": self._nuke_line_number(invalid_lookup), "message": message,}
            )
