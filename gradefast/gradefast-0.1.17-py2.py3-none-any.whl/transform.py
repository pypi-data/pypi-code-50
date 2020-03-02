"""
Utilities for transforming a given result group. Result group transformation takes
place to ignore/exclude some of the result dictionary parameters or if to rename 
some fields to another. You'll need this mostly to format the results before uploading
them to portal
"""
from copy import deepcopy
from gradefast.result import Result, ResultGroup

class Transform:
    """
    Transformations a given result group which include changing names of the parameters,
    and including or excluding some parameters from the result dictionary.
    """
    @staticmethod
    def rename(mapping: dict, result_group):
        renamed_results = []
        for result in result_group:
            renamed_result = Result.rename(mapping, result)
            renamed_results.append(renamed_result)
        return ResultGroup(result_group.task_name, result_group.theme_name, renamed_results)

    @staticmethod
    def include(parameters: list, result_group):
        transformed_result_group = deepcopy(result_group)
        for result in result_group:
            for key in result.result_dict.keys():
                if key not in parameters:
                    transformed_result_group[result.team_id].result_dict.pop(key)
        return transformed_result_group
    
    @staticmethod
    def exclude(parameters: list, result_group):
        transformed_result_group = deepcopy(result_group)
        for result in transformed_result_group:
            for key in parameters:
                if key in result.result_dict:
                    transformed_result_group[result.team_id].result_dict.pop(key)
        return transformed_result_group
