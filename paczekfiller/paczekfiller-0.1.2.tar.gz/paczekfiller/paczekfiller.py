# -*- coding: utf-8 -*-
import sys
from jinja2 import Template, Environment, meta, select_autoescape

DELIM = '_'
SPACE = ' '


def main_function(template_file):
    """Load the template, get values for variables
    and return it"""

    try:
        content = load(template_file)
        assert content, "Couldn't load template"

        template = Template(content)
        print(content)
        return template.render(context(content))
    except EOFError:
        sys.stderr.write("Error EOF")
    except OSError:
        sys.stderr.write("Error loading template file")
    except Exception as e:
        sys.stderr.write("Unexptected exception %s" % e)


def extract_variables(content: str) -> set:
    """Extract variables to fill in"""

    env = Environment(autoescape=select_autoescape(['html', 'xml']))

    return meta.find_undeclared_variables(env.parse(content))


def context(template):
    """Create template context from
    variables used in the template.

    Fill them out interactively using
    `InteractiveVariable`s
    """

    return {
        v.key: v.read()
        for v in
        [Variable(name) for name in extract_variables(template)]
    }


class Variable:
    """Representation of the template variable
    that will handle the user input"""
    def __init__(self, variable_name):
        self.key = variable_name
        self.message = self.key.replace(DELIM, SPACE)
        self.value = None

    def prompt(self):
        """Ask user for value"""
        return input(self.message + ": ").strip()

    def read(self):
        """Read the value and return it"""
        value_from_cli = self.prompt()

        self.value = value_from_cli
        return value_from_cli


def load(template):
    """Read the contents of the template file"""
    with open(template) as f:
        return f.read()
