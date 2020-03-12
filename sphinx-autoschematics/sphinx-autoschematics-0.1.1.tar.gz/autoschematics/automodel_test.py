# coding=utf8

import pytest

from schematics.types import StringType
from schematics.types.compound import ListType

from sphinx.testing import util

from autoschematics.automodel import as_annotation, full_model_class_name, humanize


def test_humanize():
    assert humanize("employee_salary") == "Employee salary"


def test_full_model_class_name():
    class ExampleModel(object):
        pass

    assert (
        full_model_class_name(ExampleModel)
        == "autoschematics.automodel_test.ExampleModel"
    )


def test_as_annotation():
    assert as_annotation(StringType()) == "StringType()"
    assert as_annotation(ListType(StringType)) == "ListType(StringType())"


@pytest.fixture(scope="module")
def rootdir():
    """rootdir is a sphinx fixture that allows for specifying where our "document root" is when running marked tests"""
    return util.path(__file__).parent.parent.abspath()


@pytest.mark.sphinx("html")
def test_documenters(app):
    app.build()
    content = app.env.get_doctree("index")
    expected = u"\n\nclass models.ExampleModel\n\nExampleModel is a model for testing\n\nJust like in Sphinx .rst files you can use restructured text directives in the\ndocstring to provide rich content in the generated docs.\n\nfoo: Foo\nbar:\n  - bar1\n  - bar2\n\n\n\nbar ListType(StringType())\n\nRequired: False\n\nDefault: Undefined\n\n\n\nfoo StringType()\n\nRequired: True\n\nDefault: Undefined\n\nCustom value: True"  # noqa
    assert content.astext() == expected
