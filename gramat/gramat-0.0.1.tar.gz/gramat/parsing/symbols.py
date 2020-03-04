import string

name_begin_chars = string.ascii_letters + '_'
name_other_chars = string.ascii_letters + string.digits + '_-'

soft_assignment_mark = ':'
hard_assignment_mark = '='
rule_debug_mark = '!'

group_begin_mark = '('
group_end_mark = ')'

repetition_begin_mark = '{'
repetition_end_mark = '}'
repetition_range_mark = ','
repetition_count_mark = ';'
repetition_separator_mark = '/'

optional_begin_mark = '['
optional_end_mark = ']'

literal_delimiter_char = '"'
predicate_delimiter_char = '`'
predicate_range_mark = '-'

alternation_mark = '|'
negation_mark = '!'

escape_char = '\\'

whitespace_chars = ' \t\r\n'
