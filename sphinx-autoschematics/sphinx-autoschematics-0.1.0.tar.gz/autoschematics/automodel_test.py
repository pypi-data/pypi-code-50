from autoschematics.automodel import humanize


def test_humanize():
    assert humanize("employee_salary") == "Employee salary"
