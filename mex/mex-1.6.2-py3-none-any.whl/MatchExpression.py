# -*- coding: utf-8 -*-

import nwae.utils.Log as lg
from inspect import getframeinfo, currentframe
import re
import nwae.utils.StringUtils as su
import mex.MexBuiltInTypes as mexbuiltin
import pandas as pd
import nwae.utils.Profiling as prf


#
# A Layer of Abstraction above Regular Expressions
#
# Human Level Description of extracting parameters from sentence
# WITHOUT technical regular expression syntax.
#
# Higher Level Abstraction to re.match() to extract parameters
# Never allow user to specify their own regex, this is the idea of this
# abstraction or simplification - always keep it simple, support a new
# var type if need.
#
# For details, see README.md
#
class MatchExpression:
    MEX_OBJECT_VARS_TYPE = 'type'
    MEX_OBJECT_VARS_EXPRESIONS_FOR_LEFT_MATCHING = 'expressions_for_left_matching'
    # This might come with postfixes (e.g. 'is') attached to expressions
    MEX_OBJECT_VARS_EXPRESIONS_FOR_RIGHT_MATCHING = 'expressions_for_right_matching'
    MEX_OBJECT_VARS_LENGTH_RANGE = 'length_range'
    MEX_OBJECT_VARS_PREFERRED_DIRECTION = 'preferred_direction'

    # Separates the different variables definition. e.g. 'm, float, mass & m   ;   c, float, light & speed'
    MEX_VAR_DEFINITION_SEPARATOR = ';'
    # Separates the description of the same variable. e.g. 'm, float, mass & m'
    MEX_VAR_DESCRIPTION_SEPARATOR = ','
    # Separates the names of a variable. e.g. 'mass / m'. Accept either '/' or '&'
    MEX_VAR_EXPRESSIONS_SEPARATORS = ['/','&']

    TERM_LEFT = mexbuiltin.MexBuiltInTypes.TERM_LEFT
    TERM_RIGHT = mexbuiltin.MexBuiltInTypes.TERM_RIGHT

    def __init__(
            self,
            pattern,
            map_vartype_to_regex = None,
            case_sensitive       = False,
            lang                 = None,
            do_profiling         = False
    ):
        self.pattern = pattern
        self.case_sensitive = case_sensitive
        self.lang = lang
        self.map_vartype_to_regex = map_vartype_to_regex
        self.do_profiling = do_profiling
        if self.map_vartype_to_regex is None:
            self.map_vartype_to_regex = mexbuiltin.MexBuiltInTypes.get_mex_built_in_types()
            lg.Log.debug(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Using default mex built-in types'
            )
        lg.Log.debug(
            str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno) \
            + ': Pattern "' + str(self.pattern) + '", case sensitive = ' + str(self.case_sensitive)
            + ', lang = ' + str(self.lang) + '.'
        )
        #
        # Decode the model variables
        #
        self.mex_obj_vars = self.decode_match_expression_pattern(
            lang = self.lang
        )
        lg.Log.info(
            str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno) \
            + ': Model Object vars: ' + str(self.mex_obj_vars)
        )
        return

    def get_mex_var_names(
            self
    ):
        return list(self.mex_obj_vars.keys())

    def get_mex_var_type(
            self,
            var_name
    ):
        if var_name in self.mex_obj_vars:
            return self.mex_obj_vars[var_name][MatchExpression.MEX_OBJECT_VARS_TYPE]
        return None

    def get_mex_var_expressions(
            self,
            var_name,
            side = 'left'
    ):
        if var_name in self.mex_obj_vars:
            if side == 'left':
                return self.mex_obj_vars[var_name][MatchExpression.MEX_OBJECT_VARS_EXPRESIONS_FOR_LEFT_MATCHING]
            else:
                return self.mex_obj_vars[var_name][MatchExpression.MEX_OBJECT_VARS_EXPRESIONS_FOR_RIGHT_MATCHING]
        return None

    #
    # Extract from string encoding
    #   'm, float , mass / m   ;   c, float, light / speed'
    # into something like:
    #   {
    #      'm': {
    #         'type': 'float',
    #         'expressions_for_left_matching': ['mass', 'm'],
    #         'expressions_for_right_matching': ['mass is', 'mass', 'm is', 'm']
    #      },
    #      'c': {
    #         'type': 'float',
    #         'expressions_for_left_matching': ['speed', 'light'],
    #         'expressions_for_right_matching': ['speed is', 'speed', 'light is', 'light']
    #      }
    #   }
    #
    def decode_match_expression_pattern(
            self,
            lang
    ):
        try:
            var_encoding = {}

            # Use our own split function that will ignore escaped built-in separator
            # Here we split "m,float,mass&m;c,float,light&speed" into ['m,float,mass&m', 'c,float,light&speed']
            str_encoding = su.StringUtils.split(
                string     = self.pattern,
                split_word = MatchExpression.MEX_VAR_DEFINITION_SEPARATOR
            )
            for unit_mex_pattern in str_encoding:
                unit_mex_pattern = su.StringUtils.trim(unit_mex_pattern)
                if unit_mex_pattern == '':
                    continue
                # Use our own split function that will ignore escaped built-in separator
                # Here we split 'm,float,mass&m' into ['m','float','mass&m']
                var_desc = su.StringUtils.split(
                    string     = unit_mex_pattern,
                    split_word = MatchExpression.MEX_VAR_DESCRIPTION_SEPARATOR
                )

                if len(var_desc) < 3:
                    raise Exception(
                        'Mex pattern must have at least 3 parts, got only ' + str(len(unit_mex_pattern))
                        + ' for unit mex pattern "' + str(unit_mex_pattern)
                        + '" from mex pattern "' + str(self.pattern)
                    )

                lg.Log.debugdebug('Pattern "' + str(unit_mex_pattern) + '" split to: ' + str(var_desc))

                part_var_id = su.StringUtils.trim(var_desc[0])
                part_var_type = su.StringUtils.trim(var_desc[1])
                part_var_expressions = su.StringUtils.trim(var_desc[2])
                part_var_len_range = None
                if len(var_desc) >= 4:
                    try:
                        part_var_len_range = su.StringUtils.trim(var_desc[3]).lower().split('-')
                        len_arr= len(part_var_len_range)
                        if len_arr == 0:
                            part_var_len_range = None
                        elif len_arr == 1:
                            part_var_len_range.append(part_var_len_range[0])
                        for i in range(len(part_var_len_range)):
                            part_var_len_range[i] = int(part_var_len_range[i])
                    except Exception as ex_var_len:
                        lg.Log.error(
                            str(MatchExpression.__name__) + ' ' + str(getframeinfo(currentframe()).lineno)
                            + ': Exception "' + str(ex_var_len)
                            + '" processing expressions length part "' + str(var_desc[3])
                            + '", set to None.'
                        )
                        part_var_len_range = None
                part_var_preferred_direction = MatchExpression.TERM_LEFT
                if len(var_desc) >= 5:
                    part_var_preferred_direction = su.StringUtils.trim(var_desc[4]).lower()

                try:
                    expressions_arr_for_left_matching = \
                        MatchExpression.process_expressions_for_var(
                            mex_expressions = part_var_expressions,
                            for_left_or_right_matching = MatchExpression.TERM_LEFT,
                            lang = lang
                        )
                except Exception as ex_left:
                    raise Exception(
                        'Exception "' + str(ex_left) + '" processing left expressions for "'
                        + str(part_var_expressions) + '" for var "' + str(part_var_id) + '".'
                    )

                try:
                    # For right matching, we add common postfixes to expressions
                    expressions_arr_for_right_matching = \
                        MatchExpression.process_expressions_for_var(
                            mex_expressions = part_var_expressions,
                            for_left_or_right_matching = MatchExpression.TERM_RIGHT,
                            lang = lang
                        )
                except Exception as ex_right:
                    raise Exception(
                        'Exception "' + str(ex_right) + '" processing right expressions for "'
                        + str(part_var_expressions) + '" for var "' + str(part_var_id) + '".'
                    )

                var_encoding[part_var_id] = {
                    # Extract 'float' from ['m','float','mass / m','left']
                    MatchExpression.MEX_OBJECT_VARS_TYPE: part_var_type,
                    # Extract ['mass','m'] from 'mass / m'
                    MatchExpression.MEX_OBJECT_VARS_EXPRESIONS_FOR_LEFT_MATCHING: expressions_arr_for_left_matching,
                    MatchExpression.MEX_OBJECT_VARS_EXPRESIONS_FOR_RIGHT_MATCHING: expressions_arr_for_right_matching,
                    MatchExpression.MEX_OBJECT_VARS_LENGTH_RANGE: part_var_len_range,
                    # Extract 'left'
                    MatchExpression.MEX_OBJECT_VARS_PREFERRED_DIRECTION: part_var_preferred_direction
                }
                lg.Log.info(
                    str(MatchExpression.__name__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                    + ': Successfully decoded vars object item "'
                    + str(part_var_id) + '": ' + str(var_encoding[var_desc[0]])
                )
            return var_encoding
        except Exception as ex:
            errmsg = str(MatchExpression.__name__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                     + ': Failed to get var encoding for mex pattern "' \
                     + str(self.pattern) + '". Exception ' + str(ex) + '.'
            lg.Log.error(errmsg)
            raise Exception(errmsg)

    #
    # Some processing we need to do:
    #   - Append common postfixes to expressions (creating another one) based on language
    #   - Sort by longest to shortest expressions
    #
    @staticmethod
    def process_expressions_for_var(
            mex_expressions,
            for_left_or_right_matching,
            lang
    ):
        mex_expressions = su.StringUtils.trim(mex_expressions)
        if len(mex_expressions) > 1:
            for expr_sep in MatchExpression.MEX_VAR_EXPRESSIONS_SEPARATORS:
                # If mex expression has an ending '/', we remove it, but not for escaped '\\/'
                mex_expressions = re.sub(
                    pattern = '[^\\\\]' + str(expr_sep) + '$',
                    repl    = '',
                    string  = mex_expressions
                )

        # We try to split by several separators for backward compatibility
        expressions_arr_raw_no_postfix = None
        for exp_sep in MatchExpression.MEX_VAR_EXPRESSIONS_SEPARATORS:
            expressions_arr_raw_no_postfix = su.StringUtils.split(
                string     = mex_expressions,
                split_word = exp_sep
            )
            # TODO Remove this code when we don't need backward compatibility
            #  to support both '&' and '/'. '&' will be removed.
            if len(expressions_arr_raw_no_postfix) > 1:
                break

        expressions_arr_raw = expressions_arr_raw_no_postfix.copy()
        #
        # For right matching, we add common postfixes to expressions
        #
        if for_left_or_right_matching == MatchExpression.TERM_RIGHT:
            #
            # If no expressions are specified, then there is no need to match
            # the right side, as we are only looking for the regex, and this is
            # handled correctly on the left side but not on the right side.
            # For example if we are looking for an email 'email@gmail.com', the
            # right side will return only 'l@gmail.com'
            #
            if ''.join(expressions_arr_raw) != '':
                postfix_list_for_right_matching = mexbuiltin.MexBuiltInTypes.DEFAULT_EXPRESSION_POSTFIXES
                if lang in mexbuiltin.MexBuiltInTypes.COMMON_EXPRESSION_POSTFIXES.keys():
                    postfix_list_for_right_matching = \
                        mexbuiltin.MexBuiltInTypes.COMMON_EXPRESSION_POSTFIXES['all'] + \
                        mexbuiltin.MexBuiltInTypes.COMMON_EXPRESSION_POSTFIXES[lang]
                for expr in expressions_arr_raw_no_postfix:
                    for postfix in postfix_list_for_right_matching:
                        expressions_arr_raw.append(expr + postfix)

        sort_via_length = True
        len_expressions_arr_raw = []
        for i in range(len(expressions_arr_raw)):
            len_expressions_arr_raw.append(len(expressions_arr_raw[i]))

        lg.Log.debug(
            str(MatchExpression.__name__) + ' ' + str(getframeinfo(currentframe()).lineno)
            + ': Raw Expressions for ' + str(for_left_or_right_matching) + ' matching: '
            + str(expressions_arr_raw)
            # + '. Len ' + str(len_expressions_arr_raw)
        )

        #
        # Now we need to sort by longest to shortest.
        # Longer names come first
        # If we had put instead "이름 / 이름은", instead of detecting "김미소", it would return "은" instead
        # 'mex': 'kotext, str-ko, 이름은 / 이름   ;'
        #
        expressions_arr = expressions_arr_raw
        if len(expressions_arr_raw) > 1:
            try:
                if sort_via_length:
                    df_expressions = pd.DataFrame({
                        'expression': expressions_arr_raw,
                        'len': len_expressions_arr_raw
                    })
                    df_expressions = df_expressions.sort_values(by=['len'], ascending=False)
                    expressions_arr = df_expressions['expression'].tolist()
                else:
                    # Normal alphabetical sorting in reverse (so that longer appear first if initial
                    # alphabets are the same)
                    # This sorted() function is TWICE SLOWER than pandas sort by length!!!!
                    expressions_arr = sorted(
                        expressions_arr_raw,
                        reverse = True
                    )
                lg.Log.debug(
                    str(MatchExpression.__name__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                    + ': Sorted (sort by length=' + str(sort_via_length)
                    + ' Expressions ' + str(expressions_arr_raw)
                    + ' to \n\r' + str(expressions_arr)
                )
            except Exception as ex_sort:
                lg.Log.error(
                    str(MatchExpression.__name__) + ' ' + str(getframeinfo(currentframe()).lineno)
                    + ': Failed to sort ' + str(expressions_arr_raw)
                    + ', len arr ' + str(len_expressions_arr_raw)
                    + '. Exception ' + str(ex_sort) + '.'
                )
                expressions_arr = expressions_arr_raw

        corrected_expressions_arr = []
        # Bracket characters that are common regex key characters,
        # as they are inserted into regex later on
        for expression in expressions_arr:
            expression = su.StringUtils.trim(expression)
            corrected_expression = ''
            #
            # We now need to escape common characters found in regex patterns
            # if found in the expression. So that when inserted into regex patterns,
            # the expression will retain itself.
            #
            for i in range(len(expression)):
                if expression[i] in mexbuiltin.MexBuiltInTypes.COMMON_REGEX_CHARS:
                    corrected_expression = corrected_expression + '[' + expression[i] + ']'
                else:
                    corrected_expression = corrected_expression + expression[i]
            corrected_expressions_arr.append(corrected_expression)

        return corrected_expressions_arr

    def handle_length_range(
            self,
            value_left,
            value_right,
            # e.g. [2,5]
            var_len_range
    ):
        if var_len_range and (type(value_left) is str):
            if len(value_left) < var_len_range[0]:
                value_left = None
            elif len(value_left) > var_len_range[1]:
                value_left = value_left[0:var_len_range[1]]
        if var_len_range and (type(value_right) is str):
            if len(value_right) < var_len_range[0]:
                value_right = None
            elif len(value_right) > var_len_range[1]:
                value_right = value_right[0:var_len_range[1]]

        return (value_left, value_right)

    #
    # Extract variables from string
    #
    def extract_variable_values(
            self,
            sentence
    ):
        lg.Log.debug(
            str(MatchExpression.__name__) + ' ' + str(getframeinfo(currentframe()).lineno) \
            + ': Extracting vars from "' + str(sentence) + '", using mex encoding ' + str(self.mex_obj_vars)
        )

        var_values = {}

        # Look one by one
        for var in self.mex_obj_vars.keys():
            # Left and right values
            var_values[var] = (None, None)
            # Get the names and join them using '|' for matching regex
            var_expressions_for_left_matching = \
                '|'.join(self.mex_obj_vars[var][MatchExpression.MEX_OBJECT_VARS_EXPRESIONS_FOR_LEFT_MATCHING])
            var_expressions_for_right_matching = \
                '|'.join(self.mex_obj_vars[var][MatchExpression.MEX_OBJECT_VARS_EXPRESIONS_FOR_RIGHT_MATCHING])
            var_len_range = self.mex_obj_vars[var][MatchExpression.MEX_OBJECT_VARS_LENGTH_RANGE]

            data_type = self.mex_obj_vars[var][MatchExpression.MEX_OBJECT_VARS_TYPE]

            #
            # Default to search the front value first
            # TODO Make this more intelligent
            #
            value_left = self.get_var_value(
                sentence        = sentence,
                var_name        = var,
                var_expressions = var_expressions_for_left_matching,
                data_type       = data_type,
                left_or_right   = MatchExpression.TERM_LEFT
            )
            value_right = self.get_var_value(
                sentence        = sentence,
                var_name        = var,
                var_expressions = var_expressions_for_right_matching,
                data_type       = data_type,
                left_or_right   = MatchExpression.TERM_RIGHT
            )

            if value_left or value_right:
                lg.Log.debug(
                    str(MatchExpression.__name__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                    + ': For var "' + str(var) + '" found values ' + str([value_left, value_right])
                )
                try:
                    if data_type not in self.map_vartype_to_regex.keys():
                        raise Exception('Unrecognized type "' + str(data_type) + '".')
                    elif data_type == mexbuiltin.MexBuiltInTypes.MEX_TYPE_INT:
                        if value_left:
                            value_left = int(value_left)
                        if value_right:
                            value_right = int(value_right)
                        var_values[var] = (value_left, value_right)
                    elif data_type == mexbuiltin.MexBuiltInTypes.MEX_TYPE_FLOAT:
                        if value_left:
                            value_left = float(value_left)
                        if value_right:
                            value_right = float(value_right)
                        var_values[var] = (value_left, value_right)
                    else:
                        if value_left:
                            value_left = str(value_left)
                        if value_right:
                            value_right = str(value_right)
                        var_values[var] = (value_left, value_right)
                except Exception as ex_int_conv:
                    errmsg = str(MatchExpression.__name__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                             + ': Failed to extract variable "' + str(var) \
                             + '" from sentence "' + str(sentence) \
                             + '". Exception ' + str(ex_int_conv) + '.'
                    lg.Log.warning(errmsg)

            #
            # Length Range Handling
            #
            # Put to None if length range not satisfied
            var_values[var] = self.handle_length_range(
                value_left    = var_values[var][0],
                value_right   = var_values[var][1],
                var_len_range = var_len_range
            )

        lg.Log.debug(
            str(MatchExpression.__name__) + ' ' + str(getframeinfo(currentframe()).lineno) \
            + ': For sentence "' + str(sentence) + '" var values ' + str(var_values)
        )

        return var_values

    def get_var_value_regex(
            self,
            sentence,
            patterns_list,
            var_name
    ):
        lg.Log.debug(
            str(MatchExpression.__name__) + ' ' + str(getframeinfo(currentframe()).lineno) \
            + ': For var "' + str(var_name)
            + '" using match patterns list ' + str(patterns_list)
        )
        if patterns_list is None:
            lg.Log.error(
                str(MatchExpression.__name__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                + ': No patterns list provided for string "' + str(sentence)
                + '", var name "' + str(var_name) + '".'
            )
            return None

        for pattern in patterns_list:
            m = re.match(pattern=pattern, string=sentence)
            if m:
                lg.Log.debug(
                    str(MatchExpression.__name__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                    + ': For var "' + str(var_name) + '" using pattern "' + str(pattern)
                    + '", found groups ' + str(m.groups())
                )
                return m
        return None

    def get_pattern_list(
            self,
            data_type,
            var_expressions,
            left_or_right
    ):
        if not self.case_sensitive:
            var_expressions = var_expressions.lower()

        patterns_list = []
        try:
            fix_list = self.map_vartype_to_regex[data_type][left_or_right]
            for pat in fix_list:
                if left_or_right == MatchExpression.TERM_LEFT:
                    patterns_list.append(
                        pat + '[ ]*(' + str(var_expressions) + ').*'
                    )
                else:
                    patterns_list.append(
                        '.*(' + var_expressions + ')[ ]*' + pat
                    )
            return patterns_list
        except Exception as ex:
            errmsg = str(MatchExpression.__class__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                     + ': Exception "' + str(ex) \
                     + '" getting ' + str(left_or_right) + ' pattern list for var expressions "' \
                     + str(var_expressions) + '", data type "' + str(data_type) + '".'
            lg.Log.error(errmsg)
            raise Exception(errmsg)

    def get_var_value(
            self,
            sentence,
            var_name,
            var_expressions,
            data_type,
            left_or_right
    ):
        var_expressions = var_expressions.lower()

        #
        # If no expressions are specified, then there is no need to match
        # the right side, as we are only looking for the regex, and this is
        # handled correctly on the left side but not on the right side.
        # For example if we are looking for an email 'email@gmail.com', the
        # right side will return only 'l@gmail.com'
        #
        if left_or_right == MatchExpression.TERM_RIGHT:
            if var_expressions == '':
                return None

        try:
            patterns_list = self.get_pattern_list(
                data_type       = data_type,
                var_expressions = var_expressions,
                left_or_right   = left_or_right
            )
        except Exception as ex:
            errmsg = str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                     + ': Exception "' + str(ex) \
                     + '" getting ' + str(left_or_right) + ' pattern list for var name "' + str(var_name) \
                     + '", sentence "' + str(sentence) + '", var expressions "' + str(var_expressions) \
                     + '", data type "' + str(data_type) + '".'
            lg.Log.error(errmsg)
            return None

        a = prf.Profiling.start()
        m = self.get_var_value_regex(
            sentence      = sentence,
            patterns_list = patterns_list,
            var_name      = var_name
        )
        if self.do_profiling:
            lg.Log.info(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                + ': Get var value took '
                + str(prf.Profiling.get_time_dif_str(start=a, stop=prf.Profiling.stop(), decimals=5))
                + ' secs. Var "' + str(var_name) + '", sentence "' + str(sentence)
                + ', pattern list ' + str(patterns_list)
            )

        group_position = 1
        if left_or_right == MatchExpression.TERM_RIGHT:
            group_position = 2

        if m:
            if len(m.groups()) >= group_position:
                return m.group(group_position)
            else:
                warn_msg = \
                    str(MatchExpression.__class__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                    + ': For ' + str(left_or_right) + ' match, expected at least ' + str(group_position) \
                    + ' match groups for var name "' + str(var_name) \
                    + '", string "' + str(sentence) + '", var expressions "' + str(var_expressions) \
                    + '", data type "' + str(data_type) + '" but got groups ' + str(m.groups()) + '.'
                lg.Log.warning(warn_msg)
        return None

    def get_params(
            self,
            sentence,
            return_one_value = True
    ):
        if not self.case_sensitive:
            sentence = str(sentence).lower()

        #
        # Extract variables from question
        #
        params_dict = {}
        try:
            params_dict = self.extract_variable_values(
                sentence = sentence
            )
        except Exception as ex:
            errmsg = str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)\
                     + ': Error extracting params from sentence "' + str(sentence)\
                     + '" using pattern "' + str(self.pattern) + '". Exception ' + str(ex) + '.'
            lg.Log.error(errmsg)
            raise Exception(errmsg)

        if return_one_value:
            for var in params_dict.keys():
                values = params_dict[var]
                preferred_direction = self.mex_obj_vars[var][MatchExpression.MEX_OBJECT_VARS_PREFERRED_DIRECTION]

                index_priority_order = (0, 1)
                if preferred_direction == MatchExpression.TERM_RIGHT:
                    index_priority_order = (1, 0)
                if values[index_priority_order[0]] is not None:
                    params_dict[var] = values[index_priority_order[0]]
                elif values[index_priority_order[1]] is not None:
                    params_dict[var] = values[index_priority_order[1]]
                else:
                    params_dict[var] = None

        return params_dict


if __name__ == '__main__':
    lg.Log.LOGLEVEL = lg.Log.LOG_LEVEL_DEBUG_2
    import nwae.utils.Profiling as prf
    a = prf.Profiling.start()
    print(MatchExpression(
        pattern = 'm, float, mass / 무게 / вес / 重 /  ;  d, datetime, ,8-12'
    ).get_params(
        sentence = 'My mass is 68.5kg on 2019-09-08',
        return_one_value = True
    ))
    print('Took ' + str(prf.Profiling.get_time_dif_str(start=a, stop=prf.Profiling.stop(), decimals=5)))

