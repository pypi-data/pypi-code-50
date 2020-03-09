from simple_plotter.core.code_generator import Formula, PlotData, DataHandler
from simple_plotter.core.code_parser import *
import pytest


def create_code_checker():
    # code checker setup
    allowed_imports = ['numpy', 'matplotlib.pyplot', 'csv']
    allowed_calls = ['f']
    allowed_FunctionDefs = ['f']
    # allowed_names = ['np.pi', 'np.inf', 'np.e', 'np.euler_gamma', 'np.inf']
    allowed_aliases = ['np', 'plt']

    cc1 = CodeChecker(allowed_imports=allowed_imports, allowed_calls=allowed_calls,
                      allowed_aliases=allowed_aliases, allowed_FunctionDefs=allowed_FunctionDefs)

    return cc1


def test_node_visitor_imports():
    """test if correct errors are returned for invalid statements"""
    cc = create_code_checker()

    # imports
    good_code = Code("import numpy as np")
    bad_code = Code("import os")
    assert(cc.visit(good_code.code_tree) is None)
    with pytest.raises(IllegalImportExc):
        cc.visit(bad_code.code_tree)


def test_node_visitor_calls():
    cc = create_code_checker()
    # calls
    good_code1 = Code("np.sin(x)")
    good_code2 = Code("f(6)")
    bad_code = Code("os.getcwd()")
    assert (cc.visit(good_code1.code_tree) is None)
    assert (cc.visit(good_code2.code_tree) is None)
    with pytest.raises(IllegalCallExc):
        cc.visit(bad_code.code_tree)


def test_node_visitor_expr():
    cc = create_code_checker()
    bad_code = Code("open(\"some_file\", \"r\")")
    with pytest.raises(IllegalExprExc):
        cc.visit(bad_code.code_tree)


def test_node_visitor_functiondef():
    cc = create_code_checker()
    good_code = Code("def f():\n    return None")
    bad_code = Code("def test():\n    return None")
    assert (cc.visit(good_code.code_tree) is None)
    with pytest.raises(IllegalFuncionDefExc):
        cc.visit(bad_code.code_tree)


def test_node_visitor_assign():
    cc = create_code_checker()
    good_code = Code("a = 10")
    bad_code = Code("a = open")
    assert (cc.visit(good_code.code_tree) is None)
    with pytest.raises(IllegalAssignmentExc):
        cc.visit(bad_code.code_tree)


def test_check_code():
    # higher level
    cc = create_code_checker()
    good_code = Code("import numpy as np")
    bad_code = Code("import os")

    assert(cc.check_code(good_code)[0] is True)
    assert(cc.check_code(bad_code)[0] is False)
    assert("illegal import" in cc.check_code(bad_code)[1][0])


def test_node_types():
    """test parser first pass - node types"""
    cc = create_code_checker()

    bad_code = Code("from numpy import matrix")

    assert (cc.check_code(bad_code)[0] is False)


def create_problem_def():
    # math & plot problem setup
    constants = [
            {"Const. name": "a", "Value": 2, "Unit": "m/s2", "Comment": None},
            {"Const. name": "b", "Value": "np.pi", "Unit": None, "Comment": None},
        ]

    function = "a * x**2 + b * x + c"

    set_var_name = ""
    set_var_explicit = ""
    set_var_min = 1
    set_var_max = 3
    no_sets = 3

    formula = Formula(equation=function,
                      constants=constants,
                      explicit_set_values=set_var_explicit,
                      set_var_name=set_var_name,
                      set_min_val=set_var_min,
                      set_max_val=set_var_max,
                      no_sets=no_sets,
                      set_var_unit="m/s")
    plot_data = PlotData(grid=True, swap_xy=False, y_log=False)

    return formula, plot_data


def test_valid():
    cc1 = create_code_checker()
    formula, plot_data = create_problem_def()

    data_handler = DataHandler(formula=formula, plot_data=plot_data, export_csv=True, code_checker=cc1)

    error_codes, _ = data_handler.check_code()

    assert (error_codes == [])


def test_invalid_equation():

    cc1 = create_code_checker()
    formula, plot_data = create_problem_def()

    data_handler = DataHandler(formula=formula, plot_data=plot_data, export_csv=True, code_checker=cc1)

    data_handler.formula.equation = "a * x**2 + b * x + c * kill()"
    error_codes, _ = data_handler.check_code()

    assert (error_codes == [1])  # error in equation


def test_invalid_constants():
    cc1 = create_code_checker()
    formula, plot_data = create_problem_def()

    data_handler = DataHandler(formula=formula, plot_data=plot_data, export_csv=True, code_checker=cc1)

    invalid_const = {"Const. name": "c", "Value": "print(\"Hello World!\")", "Unit": None, "Comment": None}
    formula.constants.append(invalid_const)
    error_codes, _ = data_handler.check_code()

    assert (error_codes == [2, 6])  # error in constants and plot setup

# code = Code(code_str=data_handler.combine_code())
# code.print_code_lines()
#
# error_codes, error_logs = data_handler.plot()
#
# if error_codes:
#     for i, code in enumerate(error_codes):
#         print("Error code:", code, "-", data_handler.error_codes[code])
#         for log in error_logs[i]:
#             print("   ", log)

# with open('template_setvardefs.txt', 'r') as file:
#     defs_str = file.read()
#
# template = Template(defs_str)
#
# formula_dict = vars(formula)
# formula_dict = fix_none_values(formula_dict)
# plot_data_dict = vars(plot_data)
# plot_data_dict = fix_none_values(plot_data_dict)
#
# code_def = template.render(
#             equation=formula_dict["equation"],
#             constants=formula_dict["constants"],
#             var_name=formula_dict["var_name"],
#             var_start_val=plot_data_dict["start_val"],
#             var_end_val=plot_data_dict["end_val"],
#             no_pts=plot_data_dict["no_pts"],
#             set_const_name=formula_dict["set_var_name"],
#             explicit_set_values=formula_dict["explicit_set_values"],
#             set_min_val=formula_dict["set_min_val"],
#             set_max_val=formula_dict["set_max_val"],
#             no_sets=formula_dict["no_sets"],
#             export_csv=data_handler.export_csv
# )
#
# # print(code_def)
#
#
#
# code_str = "import numpy as np\n" \
#            "from blabla import matrix\n" \
#            "a = np.linspace = print\n" \
#            "b = np.linspace(\"Game over!\")\n" \
#            "d = kill.kill\n" \
#            "np.kill(\"all\")\n" \
#            "def f(a):\n" \
#            "    return a\n" \
#            "f(6)"
#
#
# # parse code
# # parsed_code = parse(code_def)
#
# code1 = Code(code_str)
#
#
# #cc1.visit(parsed_code)
# code1.print_code_lines()
# valid, error_log = cc1.check_code(code=code1)
#
# for error in error_log:
#     print(error)
#
# print("Code valid:", valid)
#
# code2 = Code(code_def)
# valid, error_log = cc1.check_code(code2)
#
# for error in error_log:
#     print(error)
#
# print("Code valid:", valid)
#
# # ------------- plot code ---------------#
#
# with open('template_plotsetup.txt', 'r') as file:
#     plt_str = file.read()
#
# plt_template = Template(plt_str)
#
# code_plot = plt_template.render(
#     equation=formula_dict["equation"],
#     constants=formula_dict["constants"],
#     var_name=formula_dict["var_name"],
#     set_const_name=formula_dict["set_var_name"],
#     set_const_unit=formula_dict["set_var_unit"],
#     func_name=formula_dict["function_name"],
#     func_unit=formula_dict["function_unit"],
#     swap_xy=plot_data_dict["swap_xy"],
#     x_log=plot_data_dict["x_log"],
#     y_log=plot_data_dict["y_log"],
#     var_min=plot_data_dict["start_val"],
#     var_max=plot_data_dict["end_val"],
#     y_min=plot_data_dict["y_min"],
#     y_max=plot_data_dict["y_max"],
#     grid=plot_data_dict["grid"],
#     plot_title=plot_data_dict["plot_title"]
# )
#
# code3 = Code(code_plot)
# valid, error_log = cc1.check_code(code3)
#
# for error in error_log:
#     print(error)
#
# print("Code valid:", valid)
#
# # exec(code_str)



