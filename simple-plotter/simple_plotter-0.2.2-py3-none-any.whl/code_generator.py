#!/usr/bin/python3

"""
simple_plotter - simple 2d curve plotting front-end and numpy/matplotlib code generator
Copyright (C) 2018, 2019  Thies Hecker

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# import matplotlib.pyplot as plt
import numpy as np  # needs to be imported, since we launch code with exec which contains numpy statements
import jsonpickle
import json
from jinja2 import Template
from simple_plotter.code_parser import Code, CodeChecker
import warnings
import os
from pathlib import Path

# might be helpful for debugging, when parser is launched from GUI...
# try:
#     import faulthandler
#     faulthandler.enable()
# except ModuleNotFoundError:
#     print("faulthandler module not found. If you want additional program output for debugging purposes, "
#           "please install the faulthandler module.")


def check_valid_input(input_value):
    """Checks if an input value corresponds to a valid value - i.e. not None, "", "None",...

    Args:
        input_value: Any type of input value

    Returns:
        bool: True if valid

    """

    if input_value is None or input_value == "" or input_value == "None":
        valid = False
    else:
        valid = True

    return valid


def fix_none_values(dict_):
    """Converts any dictionary item, which is "None" or "" to None"""
    for key in dict_.keys():
        if dict_[key] in ["", "None"]:
            dict_[key] = None
    return dict_


class Formula:

    def __init__(self, function_name='y', var_name='x', equation='x**2',
                 constants=None, set_var_name=None, set_min_val=None,
                 set_max_val=None, no_sets=None, var_unit=None, function_unit=None, set_var_unit=None,
                 explicit_set_values=None):
        """
        Data container for definition of the equation

        Args:
            function_name(str): Name of the "return value" - e.g. y = ...
            var_name(str): Name of the function variable - e.g. x
            equation(str): String representation of an equation (python, numpy code)
            constants(list): List with a dictionary for each constant - see notes
            set_var_name(str): Name of the set parameter
            set_min_val(float): Min. value of the set parameter
            set_max_val(float): Max. value of the set parameter
            no_sets(int): Number of set parameter values to create between min. and max. value
            var_unit(str): Unit for the variable (only used for display)
            function_unit(str): Unit of the function return value (only used for display)
            set_var_unit(str): Unit of set parameter (only used for display)
            explicit_set_values(str): String of explicit values for set parameters (like a list separated with comma)

        Notes:
            * the constants dictionary consists of following keys (all values are strings): "Const. name", "Value",
              "Unit" and "Comment"
        """
        self.function_name = function_name
        self.function_unit = function_unit
        self.var_name = var_name
        self.var_unit = var_unit
        self.equation = equation
        if constants is None:
            self.constants = []
        else:
            self.constants = constants
        self.set_var_name = str(set_var_name)
        self.set_var_unit = str(set_var_unit)
        self.set_min_val = set_min_val
        self.set_max_val = set_max_val
        self.no_sets = no_sets
        self.explicit_set_values = explicit_set_values


class PlotData:

    def __init__(self, start_val=-10.0, end_val=10.0, no_pts=50, x_log=False, y_log=False, swap_xy=False, grid=False,
                 user_data=None, y_min=None, y_max=None, plot_title=None):
        """Data container for plot definition

        Args:
            start_val(float): start of x value range
            end_val(float): end of x value range
            no_pts(int): Number of data points for x value
            x_log(bool): Sets x scale to logarithmic if True
            y_log(bool): Sets y scale to logarithmic if True
            swap_xy(bool): Swaps x and y axis if True
            grid(bool): Enables grid if True
            user_data(list): Not implemented yet
            y_min(float): Min y value for plot display
            y_max(float): Max y value for plot display
            plot_title(str): Manually defined plot title (if None, plot title will be created from formula
                             automatically)

        Notes:

            * All float values will be converted to str and may also be passed as str directly.
        """
        self.start_val = start_val
        self.end_val = end_val
        self.no_pts = no_pts
        self.x_log = x_log
        self.y_log = y_log
        self.swap_xy = swap_xy
        self.grid = grid
        if user_data is None:
            self.user_data = []
        else:
            self.user_data = user_data
        self.y_min = y_min
        self.y_max = y_max
        self.plot_title = plot_title


class DataHandler:

    error_codes = {
        0: "Error(s) in imports",
        1: "Error(s) in function definition",
        2: "Error(s) in constants definition",
        3: "Error(s) variable definition",
        4: "Error(s) in set constants definition",
        5: "Error(s) in plot call",
        6: "Error(s) in plot setup",
        7: "Error(s) in code execution"
    }

    def __init__(self, formula, plot_data, export_csv=False, filename=None, code_checker=None, plot_lib='matplotlib'):
        """
        Main class for parser - includes all code generator methods

        Args:
            formula(Formula): Formula container object
            plot_data(PlotData): plot data container object
            export_csv(bool): If true code to export curve values to csv will be embedded
            filename(str): Name of the project file (JSON)
            code_checker(CodeChecker): Code checker object
            plot_lib(str): Library used for plotting - either 'matplotlib' or 'kivy-garden/graph'
        """
        self.formula = formula
        self.plot_data = plot_data
        self.export_csv = export_csv
        self.filename = filename
        self.code_checker = code_checker

        self.template_path = Path(__file__).parent / "templates"
        self.plot_lib = plot_lib

        if self.plot_lib == 'matplotlib':
            self.code_writers = [
                "write_imports",
                "write_funcdef",
                "write_constdefs",
                "write_vardef",
                "write_setvardef",
                "write_plot_call",
                "write_plot_setup",
            ]
        elif self.plot_lib == 'kivy-garden/graph':
            self.code_writers = [
                "write_imports",
                "write_funcdef",
                "write_constdefs",
                "write_vardef",
                "write_setvardef",
                "write_garden_plot",
            ]
        else:
            raise ValueError('Unsupported plotting library: {}. '
                             '\'matplotlib\' or \'kivy-garden/graph\' are supported.'.format(self.plot_lib))

    @staticmethod
    def check_valid_input(input_value):
        """Checks if an input value corresponds to a valid value - i.e. not None, "", "None",...

        Returns:
            bool: True if valid input value
        """

        return check_valid_input(input_value)

    def write_py_file(self, filename):
        """
        writes a python file with code generated by combine_code
        """
        with open(filename, "w") as file:
            file.write(self.combine_code())

        print('Python source code exported to '+filename)

    def check_code(self):
        """Checks the code for each segment

        Returns:
            tuple: Consisting of:

                * list: List of error codes
                * list: List of error logs

        Notes:
            * following error codes exist:
                * 0: Error in imports
                * 1: Error in function definition
                * 2: Error in constants definition
                * 3: Error variable definition
                * 4: Error in set constants definition
                * 5: Error in plot call
                * 6: Error in plot setup
        """

        if self.code_checker is None:
            raise ValueError("No code-checker defined!")

        #TODO: Handle csv code...

        errors = []
        error_logs = []

        for i, writer in enumerate(self.code_writers):
            code = Code(code_str=getattr(self, writer)())
            valid, error_log = self.code_checker.check_code(code=code)
            if not valid:
                errors.append(i)
                error_logs.append(error_log)

        return errors, error_logs

    def combine_code(self):
        """Assembles complete code

        Returns:
            str: combined python code
        """

        code_str = ""

        for writer in self.code_writers:
            code_str += getattr(self, writer)()

        if self.export_csv:
            code_str += self.write_csv_export()

        return code_str

    def write_imports(self):
        """Writes the imports"""

        with open(self.template_path / 'template_imports.txt', 'r') as file:
            temp_str = file.read()

        template = Template(temp_str)

        code_str = template.render(
            export_csv=self.export_csv,
            plot_lib=self.plot_lib
        )

        return code_str

    def write_funcdef(self):
        """Writes the function definition"""

        if self.plot_lib == 'matplotlib':
            template_file = 'template_funcdef_mpl.txt'
        elif self.plot_lib == 'kivy-garden/graph':
            template_file = 'template_funcdef_kvg.txt'

        with open(self.template_path / template_file, 'r') as file:
            temp_str = file.read()

        template = Template(temp_str)

        formula_dict = vars(self.formula)
        formula_dict = fix_none_values(formula_dict)

        code_str = template.render(
            equation=formula_dict["equation"].replace('^', '**'),
            constants=formula_dict["constants"],
            var_name=formula_dict["var_name"],
            set_const_name=formula_dict["set_var_name"],
        )

        return code_str

    def write_constdefs(self):
        """Write constants definition"""

        with open(self.template_path / 'template_constdef.txt', 'r') as file:
            temp_str = file.read()

        template = Template(temp_str)

        formula_dict = vars(self.formula)
        formula_dict = fix_none_values(formula_dict)

        code_str = template.render(
            constants=formula_dict["constants"],
        )

        return code_str

    def write_vardef(self):
        """Write variable definition"""

        with open(self.template_path / 'template_vardef.txt', 'r') as file:
            temp_str = file.read()

        template = Template(temp_str)

        formula_dict = vars(self.formula)
        formula_dict = fix_none_values(formula_dict)
        plot_data_dict = vars(self.plot_data)
        plot_data_dict = fix_none_values(plot_data_dict)

        code_str = template.render(
            var_name=formula_dict["var_name"],
            var_start_val=plot_data_dict["start_val"],
            var_end_val=plot_data_dict["end_val"],
            no_pts=plot_data_dict["no_pts"],
        )

        return code_str

    def write_setvardef(self):
        """writes definition for set variable

        Returns:
            str: python code for definitions
        """
        with open(self.template_path / 'template_setvardefs.txt', 'r') as file:
            defs_str = file.read()

        template = Template(defs_str)

        formula_dict = vars(self.formula)
        formula_dict = fix_none_values(formula_dict)
        plot_data_dict = vars(self.plot_data)
        plot_data_dict = fix_none_values(plot_data_dict)

        code_str = template.render(
            set_const_name=formula_dict["set_var_name"],
            explicit_set_values=formula_dict["explicit_set_values"],
            set_min_val=formula_dict["set_min_val"],
            set_max_val=formula_dict["set_max_val"],
            no_sets=formula_dict["no_sets"],
            x_log=plot_data_dict["x_log"],
        )

        return code_str

    def write_plot_call(self):
        """Writes the plot call code"""

        formula_dict = vars(self.formula)
        formula_dict = fix_none_values(formula_dict)
        plot_data_dict = vars(self.plot_data)
        plot_data_dict = fix_none_values(plot_data_dict)

        with open(self.template_path / 'template_plotcall.txt', 'r') as file:
            plt_str = file.read()

        plt_template = Template(plt_str)

        code_str = plt_template.render(
            constants=formula_dict["constants"],
            var_name=formula_dict["var_name"],
            set_const_name=formula_dict["set_var_name"],
            set_const_unit=formula_dict["set_var_unit"],
            swap_xy=plot_data_dict["swap_xy"],
        )

        return code_str

    def write_plot_setup(self):
        """writes the plot setup code

        Returns:
            str: python code for plotting section
        """

        formula_dict = vars(self.formula)
        formula_dict = fix_none_values(formula_dict)
        plot_data_dict = vars(self.plot_data)
        plot_data_dict = fix_none_values(plot_data_dict)

        with open(self.template_path / 'template_plotsetup.txt', 'r') as file:
            plt_str = file.read()

        plt_template = Template(plt_str)

        code_str = plt_template.render(
            equation=formula_dict["equation"],
            constants=formula_dict["constants"],
            var_name=formula_dict["var_name"],
            var_unit=formula_dict["var_unit"],
            set_const_name=formula_dict["set_var_name"],
            set_const_unit=formula_dict["set_var_unit"],
            func_name=formula_dict["function_name"],
            func_unit=formula_dict["function_unit"],
            swap_xy=plot_data_dict["swap_xy"],
            x_log=plot_data_dict["x_log"],
            y_log=plot_data_dict["y_log"],
            var_min=plot_data_dict["start_val"],
            var_max=plot_data_dict["end_val"],
            y_min=plot_data_dict["y_min"],
            y_max=plot_data_dict["y_max"],
            grid=plot_data_dict["grid"],
            plot_title=plot_data_dict["plot_title"]
        )

        return code_str

    def write_garden_plot(self):

        formula_dict = vars(self.formula)
        formula_dict = fix_none_values(formula_dict)
        plot_data_dict = vars(self.plot_data)
        plot_data_dict = fix_none_values(plot_data_dict)

        with open(self.template_path / 'template_garden_graph_plot.txt', 'r') as file:
            plt_str = file.read()

        plt_template = Template(plt_str)
        code_str = plt_template.render(
            equation=formula_dict["equation"],
            constants=formula_dict["constants"],
            var_name=formula_dict["var_name"],
            var_unit=formula_dict["var_unit"],
            set_const_name=formula_dict["set_var_name"],
            set_const_unit=formula_dict["set_var_unit"],
            func_name=formula_dict["function_name"],
            func_unit=formula_dict["function_unit"],
            swap_xy=plot_data_dict["swap_xy"],
            x_log=plot_data_dict["x_log"],
            y_log=plot_data_dict["y_log"],
            var_min=plot_data_dict["start_val"],
            var_max=plot_data_dict["end_val"],
            y_min=plot_data_dict["y_min"],
            y_max=plot_data_dict["y_max"],
            grid=plot_data_dict["grid"],
            plot_title=plot_data_dict["plot_title"]
        )
        return code_str

    def write_csv_export(self):
        """writes the code to export to filename.csv

        Returns:
            str: python code for export to csv file
        """
        #TODO: replace with jinja template

        warnings.warn("CSV export currently not supported!")

        code_str = ""

        # if self.filename in ["", None]:
        #     filename = "temp"
        # else:
        #     filename = self.filename
        #
        # code_str = ""
        #
        # code_str += '\n\n#csv export code'
        # code_str += '\nheader = \'#' + self.formula.var_name + '\''
        # if self.check_valid_input(self.formula.set_var_name):
        #     code_str += '\nfor setConst in ' + self.formula.set_var_name + ':\n    header+=\', ' + \
        #                 self.formula.set_var_name + '=\'+str(setConst)'
        # else:
        #     code_str += '\nheader+=\', \'' + self.formula.function_name
        # code_str += '\ndata = []\ndata.append(' + self.formula.var_name + ')\n'
        # if self.check_valid_input(self.formula.set_var_name):
        #     code_str += 'for setConst in ' + self.formula.set_var_name + ':\n   '
        # code_str += 'data.append(f(' + self.formula.var_name
        # if self.check_valid_input(self.formula.set_var_name):
        #     code_str += ', setConst'
        # for constSet in self.formula.constants:
        #     code_str += ', ' + constSet[0] + ')'
        # code_str += ')'
        # code_str += '\ndata = np.transpose(data)'
        # code_str += '\nwith open(\'' + filename + '.csv\', \'w\', newline=\'\') as f:'
        # code_str += '\n    code_str += (header+\'\\n\')'
        # code_str += '\n    writer = csv.writer(f)'
        # code_str += '\n    writer.writerows(data)'

        return code_str

    def check_const_validity(self):
        """Checks the validity of defined constants

        Returns:
            bool: True if all constants are valid, false otherwise

        Note:
            Constants need to have at least a name and a value
        """

        valid = True

        for const_def in self.formula.constants:
            if const_def["Const. name"] in ["", None]:
                valid = False
            if const_def["Value"] in ["", None]:
                valid = False

        return valid

    def plot(self):
        """
        plots the function, if code is valid

        Returns:
            tuple: Consisting of:

                * list: Error codes
                * list: Error logs
        """

        # check if constants are defined correctly - need to have at least name and value
        # const_valid = self.check_const_validity()

        error_codes, error_logs = self.check_code()

        if len(error_codes) > 0:
            warnings.warn("Errors in plot code observed - returning error codes and logs. No plot created.")
            for i, code in enumerate(error_codes):
                print("Error code:", code, "-", self.error_codes[code])
                for log in error_logs[i]:
                    print("   ", log)
            return error_codes, error_logs
        else:
            code_str = self.combine_code()
            code = Code(code_str=code_str)
            code.print_code_lines()
            # plt.figure()    # create a new figure for each plot
            try:
                exec(code_str)
            except Exception as e:
                return [7], [[str(e)]]
            return None, None

    def save_project(self, filename):
        """
        saves project object to JSON file
        """
        if ".json" not in filename:
            filename += ".json"

        with open(filename, 'w') as f:
            f.write(jsonpickle.encode(self))

        print('Project saved to '+filename)

    def load_project(self, filename):
        """
        loads a project from JSON file
        """
        with open(filename, 'r') as f:
            read_data = f.read()

        json_data = json.loads(read_data)

        formula_args = json_data["formula"]
        del formula_args["py/object"]
        plot_args = json_data["plot_data"]
        del plot_args["py/object"]
        self.formula = Formula(**formula_args)
        self.plot_data = PlotData(**plot_args)

        # removed jsonpickle decode to maintain backwards compatibility!

        # JSONimport = jsonpickle.decode(read_data)
        # self.formula = JSONimport.formula
        # self.plotData = JSONimport.plotData
        print('Project loaded from ' + filename)
