from importlinter.cli import lint_imports


def test_architecture_contracts():
    result = lint_imports()
    assert 0 == result, "One of the architecture contract was broken"
