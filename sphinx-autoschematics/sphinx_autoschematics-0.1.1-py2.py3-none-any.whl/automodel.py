import re
from collections import OrderedDict

from schematics.types import BaseType, CompoundType, DictType, ListType, ModelType
from sphinx.ext.autodoc import AttributeDocumenter, ClassDocumenter
from sphinx.util.docstrings import prepare_docstring


class SchematicsModelDocumenter(ClassDocumenter):
    """SchematicsModelDocumenter is a Sphinx documenter class built for generating
    nicely formatted documentation for Schematics models
    """

    objtype = "model"
    directivetype = "class"
    option_spec = {}

    def format_args(self, **kwargs):
        """Since we're generating documentation for consumption of the model attrs,
        we don't show any args
        """
        return ""

    def get_object_members(self, want_all):
        # Force get_object_members to return all members
        # We will filter out the schematics types in filter_members below
        return super(SchematicsModelDocumenter, self).get_object_members(want_all=True)

    def filter_members(self, members, want_all):
        """Filter the members of the model to return all of the types"""
        ret = []

        for (name, member) in members:
            if not isinstance(member, BaseType):
                continue

            if member.metadata.get("document") is False:
                continue

            ret.append((name, member, True))

        return ret

    def generate(self, *args, **kwargs):
        old_indent = self.indent

        super(SchematicsModelDocumenter, self).generate(*args, **kwargs)

        self.indent = old_indent

        sourcename = self.get_sourcename()

        _, members = self.get_object_members(True)
        for (name, member) in members:
            if not isinstance(member, ModelType):
                continue

            self.add_line("", sourcename)
            self.add_line("| ", sourcename)
            self.add_line("| ", sourcename)
            self.add_line("", sourcename)

            self.add_line(
                ".. automodel:: {}\n".format(full_model_class_name(member.model_class)),
                sourcename,
            )


class SchematicsTypeDocumenter(AttributeDocumenter):
    """SchematicsTypeDocumenter is a specialized AttributeDocumenter that works on
    Schematics types and presents them in a way that leverages the type information
    and metadata
    """

    objtype = "schematics.type"
    directivetype = "attribute"
    priority = 100

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, BaseType)

    def add_directive_header(self, sig):
        self.options["annotation"] = as_annotation(self.object)
        super(SchematicsTypeDocumenter, self).add_directive_header(sig)

    def add_content(self, more_content, no_docstring=False):
        super(SchematicsTypeDocumenter, self).add_content(more_content, no_docstring)

        sourcename = self.get_sourcename()

        if isinstance(self.object, ModelType):
            self.add_line(
                "See :py:class:`{}`".format(
                    full_model_class_name(self.object.model_class)
                ),
                sourcename,
            )
            self.add_line("", sourcename)

        desc = self.object.metadata.get("description")
        if desc is not None:
            for line in prepare_docstring(desc):
                self.add_line(line, sourcename)

        IGNORE = [
            "coerce_key",
            "export_level",
            "export_mapping",
            "field",
            "is_compound",
            "metadata",
            "messages",
            "model_name",
            "name",
            "owner_model",
            "parent_field",
            "typeclass",
            "validators",
        ]
        values = OrderedDict(self.object.__dict__.copy())
        values["default"] = values["_default"]
        for k in values:
            if k[0] == "_":
                continue

            if k in IGNORE:
                continue

            v = values[k]
            if v is None:
                continue
            if isinstance(v, (list, tuple, dict)) and len(v) == 0:
                continue

            if isinstance(v, (list, tuple)):
                v = ", ".join(v)

            if isinstance(v, dict):
                v = ", ".join("{}={}".format(dk, dv) for dk, dv in v.items())

            self.add_line("| **{}**: {}".format(humanize(k), v), sourcename)

        for key in self.object.metadata:
            if key == "description":
                continue
            self.add_line(
                "| **{}**: {}".format(humanize(key), self.object.metadata[key]),
                sourcename,
            )

        self.add_line("", sourcename)


def as_annotation(field):
    if isinstance(field, (ListType, DictType)):
        repr_info = as_annotation(field.field)
    else:
        repr_info = field._repr_info() or ""

    return "{}({})".format(field.__class__.__name__, repr_info)


def full_model_class_name(model_class):
    return "{}.{}".format(model_class.__module__, model_class.__name__)


def humanize(word):
    """
    Capitalize the first word and turn underscores into spaces and strip a
    trailing ``"_id"``, if any. Like :func:`titleize`, this is meant for
    creating pretty output.

    Examples::
        >>> humanize("employee_salary")
        "Employee salary"
    """
    word = word.replace("_", " ")
    word = re.sub(r"(?i)([a-z\d]*)", lambda m: m.group(1).lower(), word)
    word = re.sub(r"^\w", lambda m: m.group(0).upper(), word)
    return word
