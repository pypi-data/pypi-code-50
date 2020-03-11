import unittest
from jbs import ir


class TestIr(unittest.TestCase):
    def setUp(self):
        ir.set_endpoint(uri='http://tdk-jbs.cs.technion.ac.il:8890/sparql', graph='http://jbs.technion.ac.il')
        self.scope = ir.Scope()
        self.scope.clear()

    def test_scope_add_book(self):
        self.scope.add_book('שמונה קבצים')
        df = ir.fetch(self.scope)
        self.assertEqual(2822, len(df))

        self.scope.clear()

        self.scope.add_book('תנ"ך')
        df = ir.fetch(self.scope)
        self.assertEqual(23206, len(df))

        self.scope.clear()

        self.scope.add_book('תנ"ך')
        self.scope.add_book('שמונה קבצים')
        df = ir.fetch(self.scope)
        self.assertEqual(26028, len(df))

        self.scope.clear()
        self.scope.add_book('שמות')
        df = ir.fetch(self.scope)
        self.assertEqual(1210, len(df))

        self.scope.clear()
        self.scope.add_book('מדרש רבה')
        df = ir.fetch(self.scope)
        self.assertTrue(len(df) > 0)

    def test_scope_set_type(self):
        self.scope.set_type('jbo:WikiArticle')
        self.scope.add_property('rdfs:label')
        df = ir.fetch(self.scope)
        self.assertEqual(6199, len(df))

    def test_scope_add_author(self):
        self.scope.add_author('הרב אברהם יצחק הכהן קוק')
        df = ir.fetch(self.scope)
        self.assertTrue(len(df) >= 2822)  # at least shemonakevatzim...

    def test_add_section(self):
        self.scope.add_book('שמות')
        self.scope.add_section('שמות א')
        df = ir.fetch(self.scope)
        self.assertEqual(22, len(df))

        self.scope.clear()
        self.scope.add_book('שמות')
        self.scope.add_section('פרשת שמות')
        df = ir.fetch(self.scope)
        self.assertEqual(124, len(df))

        # This text fails because section 'bereshit' has jbo:within for 'tanach'
        # ir.scope_clear()
        # ir.scope_add_book('תנ"ך')
        # ir.scope_add_section('פרשת בראשית')
        # df = ir.fetch()
        # self.assertEqual(146, len(df))

    def test_default_properties(self):
        self.scope.add_book('תנ"ך')
        self.scope.add_properties(ir.PROPERTIES_TEXT)
        df = ir.fetch(self.scope)
        self.assertEqual(23206, len(df))
        # check columns, which columns do we expect? uri, rdfs:label, jbo:text, jbo:position
        self.assertEqual(4, len(df.columns))
        self.assertTrue('uri' in df.columns)
        self.assertTrue('label' in df.columns)
        self.assertTrue('position' in df.columns)
        self.assertTrue('text' in df.columns)

    def test_properties(self):
        self.scope.add_book('רש"י')
        df = ir.fetch(self.scope)
        self.assertEqual(1, len(df.columns))

        self.scope.add_property('jbo:interprets')
        df = ir.fetch(self.scope)
        self.assertEqual(2, len(df.columns))

    def test_nested2_properties(self):
        self.scope.add_book('תנ"ך')
        self.scope.add_property('jbo:within#rdfs:label')
        df = ir.fetch(self.scope)
        self.assertEqual(2, len(df.columns))
        self.assertTrue('within_label' in df.columns)

    def test_nested3_properties(self):
        self.scope.add_book('רבנו חננאל')
        self.scope.add_property('jbo:interprets#jbo:within#rdfs:label')
        df = ir.fetch(self.scope)
        self.assertEqual(2, len(df.columns))
        self.assertTrue('interprets_within_label' in df.columns)

    def test_nested_properties_with_aliases(self):
        self.scope.add_book('רבנו חננאל')
        self.scope.add_properties(['jbo:interprets#rdfs:label[pasuk_label]',
                                   'jbo:interprets#jbo:within#rdfs:label[section_label]'])
        df = ir.fetch(self.scope)
        self.assertEqual(3, len(df.columns))
        self.assertTrue('pasuk_label' in df.columns)
        self.assertTrue('section_label' in df.columns)

    def test_filters(self):
        self.scope.set_type('jbo:PerushTorah')
        self.scope.add_property('jbo:interprets#jbo:within#rdfs:label(פרשת בראשית)[parasha]')
        df = ir.fetch(self.scope)
        # check that we have only parashat bereshit commentaries
        self.assertTrue(len(df) > 0)
        self.assertEqual(0, len(df[df.parasha != 'פרשת בראשית']))

    def test_nested4_properties(self):
        self.scope.set_type('jbo:Match')
        self.scope.add_property('jbo:source#jbo:interprets#jbo:within#rdfs:label')
        df = ir.fetch(self.scope)
        self.assertEqual(2, len(df.columns))
        self.assertTrue('source_interprets_within_label' in df.columns)

    def test_run_query(self):
        query = """SELECT ?uri WHERE {?uri a jbo:Book. ?uri rdfs:label "שמונה קבצים"}"""
        df = ir.run_query(query)
        self.assertEqual(1, len(df))

    def test_get_properties_for_type(self):
        props = ir.get_properties_for_type('jbo:Text')
        self.assertTrue('jbo:text' in props)
        self.assertTrue('rdfs:label' in props)
        self.assertTrue('jbo:position' in props)
        self.assertTrue('jbo:book' in props)
        self.assertTrue('jbo:within' in props)

    def test_get_tanach_perushim(self):
        df = ir.get_tanach_perushim(section_heb='פרשת בהר')
        self.assertEqual(0, len(df[df.section != 'פרשת בהר']))
