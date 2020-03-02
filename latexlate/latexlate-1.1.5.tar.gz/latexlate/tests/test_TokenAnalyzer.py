import pytest

from .. import Template
from .. import TokenAnalyzer


class TestAnalyzers:
    def setup_method(self, method):
        try:
            self.t
        except AttributeError as e:
            self.t = TokenAnalyzer.TokenAnalizer()

    def test_if(self):
        response = self.t.analyze('if', 'if x in list(range(6))')
        assert response.lines_to_add == 'if x in list(range(6)):'
        assert response.indent_after == True

    def test_if2(self):
        assert 5 == 5

    def test_if3(self):
        assert 5 == 5


class TestTemplate:
    def test_if_1(self):
        text = '''[- if True == True -]test_1[- endif -]'''
        t = Template(text, {})
        assert t.render() == 'test_1'

    def test_else_1(self):
        text = '''[- if False -]hui[-else-]huilo[-endif-]'''
        t = Template(text, {})
        assert t.render() == 'huilo'
    def test_if_context_1(self):
        text = '''[- if cond1 -]test_1[- endif -][- if cond2 -]test_2[- endif -]'''
        t = Template(text, {'cond1': True, 'cond2': False})
        assert t.render() == 'test_1'

    def test_for_1(self):
        text = '''[- for x in range(3) -]test_1[- endfor -]'''
        t = Template(text, {})

        assert t.render() == 'test_1test_1test_1'

    def test_for_context_1(self):
        text = '''[- for x in table -][[x]][- endfor -]'''
        t = Template(text, {'table': [1, 2, 3, 4]})
        assert t.render() == '1234'

    def test_context_1(self):
        text = '[[fuck]][[test_1]][[test_2]]'
        t = Template(text, {'_test': 1, 'fuck': 2, 'test_1': 3, 'test_2': 4})
        assert t.render() == '234'
        assert str(t.code).index('fuck') != -1
        assert str(t.code).index('test_1') != -1
        assert str(t.code).index('test_2') != -1
        with pytest.raises(ValueError):
            str(t.code).index('_test')

    def test_context_2(self):
        class Test:
            def __init__(self, x):
                self.x = x

        tests = [Test(x) for x in range(3)]
        text = '[-for test in tests -][[test.x]][-endfor -]'
        t = Template(text, {'tests': tests})
        assert t.render() == '012'

    def test_define_1(self):
        text = '[-for i in range(6) -][[i**2]][-endfor -]'
        t = Template(text, {})
        assert t.render() == "01491625"

    def test_wolfram_1(self):
        text = '[#f[x_]:=x^2;f[5]#]'
        t = Template(text, {})
        print(t.render())
        print(t.code)
        assert t.render() == '25'

    def test_wolfram_2(self):
        text = 'f(5)=[#f[x_]:=x^2;f[5]#]'
        t = Template(text, {})
        print(t.render())
        assert t.render() == 'f(5)=25'
    def test_wolfram_3(self):
        text = '[#f[x_]:=x^2;#]'
        t = Template(text, {})
        print(t.render())
        assert t.render() == ''
    def test_wolfram_4(self):
        text = '[#x="234";x#]'
        t = Template(text, {})
        print(t.render())
        assert t.render() == '234'



class TestFilters:
    def test_upper(self):
        text = '[[test|upper]]'
        t = Template(text, {'test': 'abc'})
        assert t.render() == 'ABC'

    def test_prec_noargs(self):
        text = '[[test|prec]]'
        t = Template(text, {'test': 5.012345})
        assert t.render() == '5.012'

    def test_prec_withargs(self):
        text = '[[test|prec(3)]]'
        t = Template(text, {'test': 50.123})
        assert t.render() == '50.1'

    def test_prec_1(self):
        text = '[[test|prec(3)]]'
        t = Template(text, {'test': 1.05432e-05})
        assert t.render() == '1.05\.10^{-5}'

    def test_prec_2(self):
        text = '[[test|prec(3)]]'
        t = Template(text, {'test': 5120000})
        assert t.render() == '5.12\.10^{6}'

    def test_custom_filters_noargs_1(self):
        text = '[[test|filt]]'
        t = Template(text, {'test': 5})
        t.add_filter(lambda x: 'abc', 'filt')
        assert t.render() == 'abc'

    def test_custom_filters_args_1(self):
        text = '[[test|filt(5)]]'
        t = Template(text, {'test': 5})
        t.add_filter(lambda x, y: 'a' * y, 'filt')
        assert t.render() == 'aaaaa'

    def test_auto_prec_1(self):
        text = '[[x]]'
        t = Template(text, {'x': 3.01234})
        print(t.render())
        assert t.render() == '3.012'



class TestView:
    def test_float_1(self):
        text = '[[x]]+[[y]]'
        t = Template(text, {'x': 5.010169, 'y': 1e-05})
        assert t.render() == '5.01+1\\.10^{-5}'
