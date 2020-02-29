"""Module that provides ability to solve LP problems from command line
Basic syntax of statement file is described with PROBLEM_STATEMENT grammar

GRAMMAR :

FUNCTION_NAME := [a-zA-Z]*?
VARIABLE_NAME := [A-Za-z_][A-Za-z_0-9]*
VARIABLE  := (DECIMAL [*]) VARIABLE_NAME
VARIABLE_SEQUENCE := VARIABLE | VARIABLE [+|-|/|*] VARIABLE_SEQUENCE
GOAL_FUNCTION := [MAX|MIN] FUNCTION_NAME = VARIABLE_SEQUENCE
CONSTRAINT := VARIABLE_SEQUENCE [<=|>=] VARIABLE_SEQUENCE
PROBLEM_STATEMENT := "GOAL" NEWLINE GOAL_FUNCTION NEWLINE "SUBJECT TO" NEWLINE CONSTRAINT{+}
"""

import argparse
import logging
import os
import traceback
from typing import TextIO

import matplotlib.pyplot as plt
from pandas import ExcelWriter

import lpp_solver.lp_problem as lp_problem
from lpp_solver.logging_ import configure_logger, logger


def get_arguments():
    parser = argparse.ArgumentParser(description='Utility to solve linear programming problems')

    subparsers = parser.add_subparsers(help='Select sub-command to start execution', dest='command', required=True)

    solution_parser = subparsers.add_parser('solve', help='Solves LP problem which must be contained in file'
                                                          'refer "example" for generation problem file')

    required = solution_parser.add_argument_group('required')
    required.add_argument('file', type=argparse.FileType('r'),
                          help='Reads input information from structured file')

    optional = solution_parser.add_argument_group('optional')
    optional.add_argument('-d', '--debug', action='store_true', dest='debug',
                          help='Enables debug mode')
    optional.add_argument('--report', dest='report', default=None,
                          help='Path to generated analysis file')
    optional.add_argument('-v', '--variables_view', dest='variables', action='store_true',
                          help='Enables variables visualization mode')
    optional.add_argument('-c', '--constraints_view', dest='constraints', action='store_true',
                          help='Enables constraints analysis visualization mode')
    optional.add_argument('--log_file', default=None, dest='log_file',
                          help='Path to file where to store logs')

    solution_parser.set_defaults(function=start_solution_process)

    example_generation_parser = subparsers.add_parser('example', help='Generates example problem statement file')
    required = example_generation_parser.add_argument_group('required')
    required.add_argument('file', type=argparse.FileType('w'),
                          help='Writes example problem to file at provided path')
    example_generation_parser.set_defaults(function=generate_example)

    return parser.parse_args()


def solve_problem(file: TextIO):
    logging.info('Generating problem from file')
    try:
        problem = lp_problem.LPProblem.create_from_file(file)
        logger.info('Finished generation, solving problem')
        problem.solve()
        logger.info('Problem solved successfully, generating view')
        return problem
    except lp_problem.ProblemParsingError as error:
        logger.error('Failed to generate problem, seems like is invalidated')
        logger.debug(str(error))
    except Exception:
        logger.debug(traceback.format_exc())


def visualize_constraints(solution: lp_problem.LPProblem):
    logger.info('Visualizing solution constraints information')
    constraints = solution.constraints_information()
    logger.debug(f'Extracted constraints information :\n{constraints}')
    constraints.plot(x='Constraint')
    plt.show()


def visualize_variable_values(solution: lp_problem.LPProblem):
    logger.info('Visualizing solution variables information')
    variables = solution.solution_information()
    logger.debug(f'Extracted variables information :\n{variables}')
    variables.plot(x='Name', y='Value', kind='bar')
    plt.show()


def export_solution_to_excel(solution: lp_problem.LPProblem,
                             excel_file_path: str):
    """Creates .xlsx file with 2 sheets 'Solution variables' and 'Constraints'"""
    logger.info(f'Exporting data to excel document to file at {os.path.abspath(excel_file_path)}')
    logger.info('Collecting data from solution')
    objective = solution.get_objective_function_value()
    variables = solution.solution_information().append({'Name': 'Objective function', 'Value': objective},
                                                       ignore_index=True)
    constraints = solution.constraints_information()
    sheets_data = [variables, constraints]
    sheets_headings = ['Solution variables', 'Constraints']
    try:
        with ExcelWriter(excel_file_path, engine='openpyxl', mode='w') as writer:
            for data, heading in zip(sheets_data, sheets_headings):
                logger.debug(f'Writing data frame to excel sheet with name "{heading}"')
                data.to_excel(writer, sheet_name=heading)
                writer.save()
        logger.info('Successfully written .xlsx file with solution information')
    except Exception:
        logger.info('Failed to export solution to excel')
        logger.debug(traceback.format_exc())


def start_solution_process(arguments):
    """Solves problem which is stated in arguments.file
    and manipulates program workflow"""
    configure_logger(arguments.debug, arguments.log_file)

    solution = solve_problem(arguments.file)
    objective = solution.get_objective_function_value()
    logger.info(f'Objective function value = {objective}')

    if arguments.constraints:
        visualize_constraints(solution)
    if arguments.variables:
        visualize_variable_values(solution)
    if arguments.report:
        export_solution_to_excel(solution, arguments.report)


def generate_example(arguments):
    """Writes example LPP to file entered in arguments"""
    content = """There you can write description of solved LPP
GOAL
MAX FUNCTION = 10 * A
SUBJECT TO
A <= 100, Constraint_name
A >= 0"""
    arguments.file.write(content)


def main():
    arguments = get_arguments()
    arguments.function(arguments)
