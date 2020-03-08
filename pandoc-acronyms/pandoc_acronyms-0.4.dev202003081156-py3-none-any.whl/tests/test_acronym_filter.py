import unittest
from tests.test_tools import return_local_test_data, convert_to_json
from acronyms.acronym_filter import Filter
from acronyms.acronyms import Acronyms
import panflute
import io


class TestAcronymFilter(unittest.TestCase):
    def test_one_acronym(self):
        doc = self._loadJSONDocument("one_acronym.md")
        filter = Filter()
        filter.acronyms = self._createAcronymsDictionary(
            "two_basic_acronyms.json")
        filter.process_document(doc)
        self.assertEqual(filter.index.occurences('bba'), 1)
        self.assertEqual(filter.index.occurences('aba'), 0)

    # TODO Port to PyTest to use test parametrization
    def test_markup_expression(self):
        """This tests bisects a single markup expression and verifies that it is parsed correctly.""" 
        test_sets = {
            # id (description, unique)  : [ markup, valid?,     spec, valid?,       key, plural, uppercase, form]
            "a simple acronym"          : [ '[!bba]', True,     'bba', True,        'bba', False, False, None ],
            "a plural acronym"          : [ '[!+bba]', True,    '+bba', True,       'bba', True, False, None ],
            "plural, explained"         : [ '[!+bba!]', True,   '+bba!', True,      'bba', True, False, '!' ],
            "plural, short form"        : [ '[!+bba<]', True,   '+bba<', True,      'bba', True, False, '<' ],
            "plural, long form"         : [ '[!+bba>]', True,   '+bba>', True,      'bba', True, False, '>' ],
            "uppercase, plural, long"   : [ '[!+^bba>]', True,  '+^bba>', True,     'bba', True, True, '>' ],
            "an uppercase acronym"      : [ '[!^bba]', True,    '^bba', True,       'bba', False, True, None] ,
            "missing exclamation mark"  : [ '[^bba!]', False,   None, None,         None, None, None, None],
            "not an acronym at all"     : [ 'nonsense', False,  None, None,         None, None, None, None],
            "bad - key with dash"       : [ '[!-bad]', True,    '-bad', None,       None, None, None, None],
            "bad - multiple forms"      : [ '[!bad>!]', True,   'bad>!', None,      None, None, None, None],
            "bad - plural comes first"  : [ '[!^+bad]', True,   '^+bad', None,      None, None, None, None],
            "no content"                : [ '[!]', False,       None, None,         None, None, None, None],
        }

        for id, test_set in test_sets.items():
            self.assertEqual(len(test_set), 8) # just to be sure
            # ex_* describes expected values:
            [ expression, ex_expression_valid, ex_spec, ex_spec_valid, ex_key, ex_plural, ex_uppercase, ex_form ] = test_set
            match = Filter.acronym_markup_expression().match(expression)
            self.assertEqual(match is not None, ex_expression_valid, id)
            # abort here if the expression is (expectedly) not valid
            if not match: continue
            # verify the specification was extracted correctly
            spec = match.group(1)
            self.assertEqual(spec, ex_spec, id)
            match_attributes = Filter.return_acronym_match(spec)
            if not ex_spec_valid:
                self.assertFalse(match_attributes, id)
                continue
            # if the spec is valid, verify the parsing:
            [ key, plural, uppercase, form ] = match_attributes
            self.assertEqual(key, ex_key, id)
            self.assertEqual(plural, ex_plural, id)
            self.assertEqual(uppercase, ex_uppercase, id)
            self.assertEqual(form, ex_form, id)

    # TODO ? make test for acronym_replacer that simulates stepping through a document

    def test_expand_acronym(self):
        filter = Filter()
        filter.acronyms = self._createAcronymsDictionary(
            "two_basic_acronyms.json")
        acronym = filter.acronyms.get('bba')
        test_sets = {
            # id (descriptive)          : [ first use?  plural, uppercase, form,    result ]
            "first use of acronym"      : [ True,       False, False, None,         "beer brewing attitude (BBA)" ],
            "repeated use of acronym"   : [ False,      False, False, None,         "BBA" ],
            "first use, plural form"    : [ True,       True, False, None,          "beer brewing attitudes (BBAs)" ],
            "repeated use, plural form" : [ False,      True, False, None,          "BBAs" ],
            "first use, uppercase"      : [ True,       False, True, None,          "Beer brewing attitude (BBA)" ],
            "repeated use, uppercase"   : [ False,      False, True, None,          "BBA" ],
            "explicit longform"         : [ False,      False, False, '>',          "beer brewing attitude" ],
            "explicit longform upper"   : [ False,      False, True, '>',           "Beer brewing attitude" ],
            "explicit shortform"        : [ False,      False, True, '<',           "BBA" ],
            "explicit explained form"   : [ False,      False, False, '!',          "beer brewing attitude (BBA)" ],
            "explicit explained upper"  : [ False,      False, True, '!',           "Beer brewing attitude (BBA)" ],
            "expl expl upper plural"    : [ False,      True, True, '!',            "Beer brewing attitudes (BBAs)" ],
        }
        for key, test_set in test_sets.items():
            self.assertEqual(len(test_set), 5)
            [ firstuse, plural, uppercase, form, expected_result ] = test_set
            result = filter.expand_acronym(acronym, firstuse, plural, uppercase, form)
            self.assertEqual(result, expected_result, key)

    def test_process_string_token(self):
        # This replacer checks that the patterns are identified correctly:
        def maybe_replace_tester(pattern, matchtext):
            return "###{}###".format(matchtext)

        filter = Filter()
        filter.acronyms = self._createAcronymsDictionary(
            "two_basic_acronyms.json")

        tokens = {
            # a simple pattern
            "[!bba]": "###[!bba]###",
            # a pattern with no match
            "test": "test",
            # a multi-word pattern with no match
            "test-test test": "test-test test",
            # a pattern with multiple matches
            "[!bba]-related/[!aba]-based": "###[!bba]###-related/###[!aba]###-based"
        }
        for token, expected_result in tokens.items():
            result = filter.process_string_token(token, maybe_replace_tester)
            self.assertEqual(result, expected_result)

    def test_run_method(self):
        doc = self._loadJSONDocument("one_acronym.md")
        acronyms = return_local_test_data("two_basic_acronyms.json")
        filter = Filter()
        try:
            filter.run([acronyms], doc)
        except:
            self.fail("calling the run method should not fail")
        self.assertEqual(filter.index.occurences('bba'), 1)

    def test_run_method_no_acronymns(self):
        doc = self._loadJSONDocument("one_acronym.md")
        filter = Filter()
        try:
            filter.run([], doc)
        except:
            self.fail("calling the run method should not fail")
        self.assertEqual(filter.index.occurences('bba'), 0)

    def test_run_method_undefined_acronym(self):
        doc = self._loadJSONDocument("sample-text.md")
        acronyms = return_local_test_data("two_basic_acronyms.json")
        filter = Filter()
        filter.run([acronyms], doc)
        # try:
        #     filter.run([acronyms], doc)
        # except:
        #     self.fail("calling the run method should not fail")
        self.assertEqual(filter.index.occurences('bba'), 2)
        self.assertEqual(filter.index.occurences('undef'), 0)

    def test_check_for_suggestions(self):
        pattern = "A BBA is helpful, but BBA-requirements are not."
        doc = self._loadJSONDocument("sample-text.md")
        acronyms = return_local_test_data("two_basic_acronyms.json")
        filter = Filter()
        filter.run([acronyms], doc)
        result = filter.check_for_suggestions(pattern)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], 'NOTE: "BBA" in "A BBA is helpful, but BBA-requirements are not." could be an acronym. Consider replacing it with [!bba].')

    def _createAcronymsDictionary(self, filename):
        with open(return_local_test_data(filename), "r") as handle:
            return Acronyms.Read(handle)

    def _loadJSONDocument(self, filename):
        data = convert_to_json(return_local_test_data(filename))
        doc = panflute.load(io.StringIO(data))
        return doc


if __name__ == '__main__':
    unittest.main()
