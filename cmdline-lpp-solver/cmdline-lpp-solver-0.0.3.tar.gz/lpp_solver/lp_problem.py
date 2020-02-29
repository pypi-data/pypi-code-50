import re
from typing import Any, Dict, List, TextIO

import pandas as pd
import pulp

from lpp_solver.logging_ import logger

_VARIABLE_SEQUENCE_PATTERN = (r'([\+\-]?\s*((?:(?:(?:\d+(?:\.\d*)?)\s*\*)?\s*[a-zA-Z]+?\d*)|(?:\d*(?:\.\d*)?))(\s*'
                              r'[\+\-\/\*]\s*(?:(?:(?:(?:\d+(?:\.\d*)?)\s*\*)?\s*[a-zA-Z]+?\d*)|(?:\d*(?:\.\d*)?)))*)')
_GOAL_FUNCTION_VALIDATION_PATTERN = re.compile(rf'^(MIN|MAX)\s+([a-zA-Z]*?)\s*=\s*{_VARIABLE_SEQUENCE_PATTERN}$')
_CONSTRAINT_VALIDATION_PATTERN = re.compile(rf'^{_VARIABLE_SEQUENCE_PATTERN}\s*(<=|>=)\s*'
                                            rf'{_VARIABLE_SEQUENCE_PATTERN}(,\s*[a-zA-Z_][a-zA-Z_\d]*\s*)?$')
_VARIABLE_TOKENIZER_PATTERN = re.compile(r'[a-zA-Z]+?\d*')


class ProblemParsingError(ValueError):
    pass


def get_item_at(lst: List[Any], index: int):
    try:
        return lst[index]
    except IndexError:
        return None


def extract_goal_function(text_representation: List[str],
                          goal_function_header: str = 'GOAL'
                          ) -> str:
    logger.info('Extracting goal function from text representation')
    try:
        logger.debug(f'Searching for goal function header "{goal_function_header}"')
        goal_function_index = text_representation.index(goal_function_header) + 1
    except ValueError:
        raise ProblemParsingError(f'Unable to find goal function header "{goal_function_header}"')
    goal_function_string = get_item_at(text_representation, goal_function_index)
    if not goal_function_string:
        raise ProblemParsingError(f'Unable to find goal function under header "{goal_function_header}"')
    if re.fullmatch(_GOAL_FUNCTION_VALIDATION_PATTERN, goal_function_string):
        logger.info(f'Goal function extracted, "{goal_function_string}"')
        return goal_function_string
    else:
        raise ProblemParsingError(f'Unable to parse goal function string: "{goal_function_string}"')


def extract_constraints(text_representation: List[str],
                        constraints_header: str = 'SUBJECT TO'
                        ) -> List[str]:
    logger.info('Extracting constraints from text representation')
    logger.debug(f'Searching for constraints header, "{constraints_header}"')
    constraints_start_index = text_representation.index(constraints_header) + 1
    constraints_list = text_representation[constraints_start_index:]
    if constraints_list:
        def constraints_filter(constraint_string: str) -> bool:
            is_constraint = bool(constraint_string and re.fullmatch(_CONSTRAINT_VALIDATION_PATTERN, constraint_string))
            if not is_constraint:
                logger.warning(f'Unable to parse constraint: "{constraint_string}"')
            return is_constraint

        logger.info(f'Filtering {len(constraints_list)} possible constraints')
        constraints_list = list(filter(constraints_filter, constraints_list))
        if constraints_list:
            logger.info(f'Found {len(constraints_list)} valid constraints')
            return constraints_list

    logger.warning('Constraints not found !')
    return constraints_list


def read_file_lines(file: TextIO) -> List[str]:
    all_lines = (line.strip() for line in file.readlines())
    return list(filter(bool, all_lines))


class LPProblem:
    def __init__(self, function_name: str, target_function: str):
        lp_function = {'MIN': pulp.LpMinimize,
                       'MAX': pulp.LpMaximize}[target_function]
        self.model: pulp.LpProblem = pulp.LpProblem(function_name, lp_function)
        self.variables: Dict[str, pulp.LpVariable] = dict()

    def add_to_model(self, string_with_variables: str):
        statement_tokens = string_with_variables.split(',')
        variable_names = re.findall(_VARIABLE_TOKENIZER_PATTERN, statement_tokens[0])
        logger.debug(f'Found such variables in statement {variable_names}')
        for variable_name in variable_names:
            if variable_name not in self.variables:
                logger.debug(f'Variable "{variable_name}" not found in knowledge base, adding information')
                self.variables[variable_name] = pulp.LpVariable(variable_name, cat=pulp.LpContinuous)
        executed_statement = re.sub(_VARIABLE_TOKENIZER_PATTERN, r'self.variables["\g<0>"]', statement_tokens[0])
        if len(statement_tokens) > 1:
            logger.debug(f'Setting name "{statement_tokens[1].strip()}" to statement')
            name_token = re.sub(r'[A-Za-z_][A-Za-z_\d]*', r',"\g<0>"', statement_tokens[1])
            self.model += eval(f'{executed_statement}{name_token}')
        else:
            self.model += eval(executed_statement)

        logger.info('Model successfully updated')

    @classmethod
    def create_from_file(cls, file: TextIO):
        text_representation = read_file_lines(file)
        logger.info(f'Initializing math model from file with {len(text_representation)} non empty lines')
        goal_function_statement = extract_goal_function(text_representation)
        goal_formalization, goal_exec_statement = goal_function_statement.split('=')
        target_function, function_name = goal_formalization.split()
        logger.info(f'Setting target function to "{target_function}"')
        logger.info(f'Settings problem name to "{function_name}"')
        problem = cls(function_name, target_function)
        constraints = extract_constraints(text_representation)
        logger.info(f'Settings model goal function to "{goal_exec_statement.strip()}"')
        problem.add_to_model(goal_exec_statement.strip())
        for constraint in constraints:
            logger.info(f'Adding constraint to model, "{constraint}"')
            problem.add_to_model(constraint.strip())
        logger.info('Successfully constructed math model')
        return problem

    def solve(self):
        self.model.solve()

    def constraints_information(self) -> pd.DataFrame:
        logger.info('Extracting shadow price and slack information about constraints')
        data = [{'Constraint': name, 'Shadow price': constraint.pi, 'Slack': constraint.slack}
                for name, constraint in self.model.constraints.items()]
        logger.info('Constructing data frame')
        return pd.DataFrame(data)

    def get_objective_function_value(self) -> float:
        logger.info('Extracting problem detailed solution')
        return self.model.objective.value()

    def solution_information(self) -> pd.DataFrame:
        logger.info('Extracting variables information')
        data = [{'Name': variable.name, 'Value': variable.varValue} for
                variable in self.model.variables()]
        logger.info('Constructing data frame')
        return pd.DataFrame(data)
