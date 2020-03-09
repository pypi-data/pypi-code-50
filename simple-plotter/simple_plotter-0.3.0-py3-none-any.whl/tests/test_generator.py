from simple_plotter.core import code_generator


def create_default_example():
    """Creates example objects and return manager"""

    formula = code_generator.Formula(equation="x**2")
    plot_defs = code_generator.PlotData()
    manager = code_generator.DataHandler(formula=formula, plot_data=plot_defs)

    return manager


def create_example2():
    """Creates example including constants"""

    constants = [
        {"Const. name": "a", "Value": 2, "Unit": None, "Comment": None},
        {"Const. name": "b", "Value": 5, "Unit": None, "Comment": None},
        {"Const. name": "c", "Value": 10, "Unit": None, "Comment": None}
    ]

    formula = code_generator.Formula(equation="a * x**2 + b * x + c", constants=constants)
    plot_defs = code_generator.PlotData()
    manager = code_generator.DataHandler(formula=formula, plot_data=plot_defs)

    return manager


def test_definitions():
    """Test if variable and equation definitions are working"""

    manager = create_default_example()
    def_str = manager.write_imports() + manager.write_funcdef()

    exec(def_str, locals())
    assert(locals()['f'](10) == 100)


def test_definition_w_constants():
    """Test if equation with constants is working"""

    a = 2
    b = 5
    c = 10

    constants = [
        {"Const. name": "a", "Value": a, "Unit": None, "Comment": None},
        {"Const. name": "b", "Value": b, "Unit": None, "Comment": None},
        {"Const. name": "c", "Value": c, "Unit": None, "Comment": None}
    ]

    formula = code_generator.Formula(equation="a * x**2 + b * x + c", constants=constants)
    plot_defs = code_generator.PlotData()
    manager = code_generator.DataHandler(formula=formula, plot_data=plot_defs)

    def_str2 = manager.write_imports() + manager.write_funcdef() + manager.write_constdefs()

    exec(def_str2, locals())
    assert(locals()['f'](10, a, b, c) == 260)


def test_invalid_constants():
    """Test if constant definitions will be corretly identified as invalid"""

    formula = code_generator.Formula()
    plot_defs = code_generator.PlotData()
    manager = code_generator.DataHandler(formula=formula, plot_data=plot_defs)

    constants = [{"Const. name": "a", "Value": 10, "Unit": None, "Comment": None}]
    formula.constants = constants
    assert manager.check_const_validity() is True

    constants = [{"Const. name": "", "Value": 10, "Unit": None, "Comment": None}]
    formula.constants = constants
    assert manager.check_const_validity() is False

    constants = [{"Const. name": None, "Value": 10, "Unit": None, "Comment": None}]
    formula.constants = constants
    assert manager.check_const_validity() is False

    constants = [{"Const. name": "a", "Value": None, "Unit": None, "Comment": None}]
    formula.constants = constants
    assert manager.check_const_validity() is False

    constants = [{"Const. name": "a", "Value": "", "Unit": None, "Comment": None}]
    formula.constants = constants
    assert manager.check_const_validity() is False
