from gradefast import logconfig
from gradefast.result import Result, ResultGroup

logger = logconfig.configure_and_get_logger(__name__)

# TODO(manjrekarom): An option to transform result_dict entirely
# This includes combining values from many parameters, excluding
# some parameters, changing names of parameters, etc. 
class Aggregate:
    """
    Contains method to group multiple :class:`~gradefast.result.ResultGroup` in different 
    ways

    Methods from this class may be used to combine results of same test, for instance, if 
    the submissions were sliced and results computed paralelly to save time. One can also
    concatenate results from different tests for aggregating it to form a final result. 
    Finally one can aggregate parameters of a test to form a final grade.

    For all such cases, use :class:`Aggregate`

    """
    # TODO: Throw error if compatible file_item_to_test or pkg_path are
    # encountered
    @staticmethod
    def combine(*result_groups):
        """
        Combine multiple :class:`ResultGroup` obtained from **same**
        :class:`~gradefast.test.GFTest` or :class:`~gradefad.GFCliTest`

        .. warning::

            When specifying result groups, please make sure they are supposed
            to be coming from same type of test. The function will combine even
            if they don't and **won't throw any error**.

        Parameters
        ----------
        results_groups: tuple
            As many result groups as you like to combine belonging to same test type

        Returns
        -------
        :class:`ResultGroup`
            Combined results groups

        Examples
        --------
        .. doctest::
        
            >>> # result groups obtained from the SAME TESTs but DIFFERENT SUBMISSIONs
            >>> result_group1 = ResultGroup(...) 
            >>> result_group2 = ResultGroup(...)
            >>> result_group3 = ResultGroup(...)
            >>> Aggregate.combine(result_group1, result_group2, result_group3)
            ResultGroup(...) 
            # result group with dict_of_results containing results from all 3 groups
        """
        final_dict = {}
        
        for group in result_groups:
            final_dict.update(group.dict_of_results)

        if len(result_groups) > 0: 
            combined_group = ResultGroup(result_groups[0].task_name, result_groups[0].theme_name,
            final_dict)
            logger.debug('Final result group: {}'.format(combined_group))
            return combined_group

        return None

    @staticmethod
    def add(*result_groups, average=False):
        """
        Add parameters in ``result_dict`` of all results present in :class:`ResultGroup`
        to form a final total

        Parameters
        ----------
        results_groups: tuple
            As many result groups as you like to combine belonging to same test type

        Returns
        -------
        :class:`ResultGroup`
            Combined results groups obtained after adding

        Examples
        --------
            >>> # result groups obtained from SAME TESTs but DIFFERENT SUBMISSIONs
            >>> result_group1 = ResultGroup(...) 
            >>> result_group2 = ResultGroup(...)
            >>> Aggregate.add(result_group1, result_group2)
            ResultGroup(...) 
            # result groups are first combined and then each result parameter is summed
            # to a total value. Output is a combined result_group having only 'total' field

        """
        return Aggregate.operate('add', *result_groups, average=average)

    @staticmethod
    def multiply(weightages, *result_groups):
        """
        Transform marks by multiplying parameters with weightages in ``result_dict``
        for all results present in :class:`ResultGroup`

        Parameters
        ----------
        results_groups: tuple
            As many result groups as you like to multiply with weightages

        Returns
        -------
        :class:`ResultGroup`
            Combined results groups obtained after multiplying

        Examples
        --------
            >>> # result groups obtained from SAME TESTs but DIFFERENT SUBMISSIONs
            >>> result_group1 = ResultGroup(...) 
            >>> result_group2 = ResultGroup(...)
            >>> weightages = {"param1": 2.5, "param2": 1/3.0, "param4": -5}
            >>> Aggregate.multiply(weightages, result_group1, result_group2)
            ResultGroup(...) 
            # result groups are first combined and then each result parameter is scaled
            # by value in weightage dictionary. Output is a combined result_group with 
            # all results scaled.

        """
        return Aggregate.operate('multiply', *result_groups, weightages=weightages)

    @staticmethod
    def flatten_test_cases(*result_groups, average=False):
        """
        Flatten test cases of ``result_dict`` for all results present in :class:`ResultGroup`

        Parameters
        ----------
        average: bool, optional
            Whether to simply add or average the list of marks in test cases. Default
            is False
        results_groups: tuple
            As many result groups as you like to combine belonging to same test type
        
        Returns
        -------
        :class:`ResultGroup`
            Combined results groups obtained after flattening test cases

        Examples
        --------
            >>> # result groups obtained from **same** tests but **different** submissions
            >>> result_group1 = ResultGroup(...) 
            >>> result_group2 = ResultGroup(...)
            >>> Aggregate.flatten_test_cases(result_group1, result_group2)
            ResultGroup(...) 
            # result groups are first combined and then each result parameter having value
            # of type list is flattened by adding (and/or averaging).

        """
        return Aggregate.operate('flatten_test_cases', *result_groups, average=average)

    @staticmethod
    def operate(method, *result_groups, weightages={}, average=False):
        if len(result_groups) > 0:
            combined_group = Aggregate.combine(*result_groups)
            final_result = {}
            for result in combined_group:
                if method == 'flatten_test_cases':
                    final_result[result.team_id] = result.flat_result()
                elif method == 'multiply':
                    final_result[result.team_id] = result.multiply(weightages)
                elif method == 'add':
                    final_result[result.team_id] = result.add(average=average)
            combined_group.dict_of_results = final_result
            return combined_group

    @staticmethod
    def join(*result_groups):
        """
        Concatenate multiple :class:`ResultGroup` performed on **same** 
        :class:`~gradefast.test.GFTest` or :class:`~gradefad.GFCliTest`

        Parameters
        ----------
        results_groups: tuple
            As many result groups as you like to combine belonging to same test type

        Returns
        -------
        :class:`ResultGroup`
            Joined result groups from different tests but of same teams  

        Examples
        --------
            >>> # result groups obtained from DIFFERENT tests but SAME submissions
            >>> result_group1 = ResultGroup(...) 
            >>> result_group2 = ResultGroup(...)
            >>> Aggregate.join(result_group1, result_group2)
            ResultGroup(...)
            # result in different result groups with same team_id are joined/concatenated to 
            # make a single result. The joined result contains parameters from both results. 
            # The output result_group's dict_of_results will contain such results for all team_ids. 

        """
        task_names = set(map(lambda group: group.task_name, result_groups))
        if len(task_names) > 1:
            raise Exception('Result groups you are joining should be for the same task')

        theme_names = set(map(lambda group: group.theme_name, result_groups))
        if len(theme_names) > 1:
            raise Exception('Result groups you are joining should be for the same theme')

        # select results with particular team_ids and run join method on them
        team_ids = set()
        for group in result_groups:
            team_ids = team_ids.union(set(map(lambda team_id: team_id, group.dict_of_results)))
            
        final_results_dict = {}
        for team_id in team_ids:
            joined_result = {}
            for group in result_groups:
                if joined_result == {}:
                    joined_result = Result.join(group[team_id])
                else:
                    joined_result = Result.join(group[team_id], joined_result)
            final_results_dict[team_id] = joined_result
        
        return ResultGroup(result_groups[0].task_name, result_groups[0].theme_name, final_results_dict)
