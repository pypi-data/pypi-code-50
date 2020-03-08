from datacode import VariableCollection

import transforms_fin

import pandas as pd
from pandas.util.testing import assert_frame_equal

from tests.base import TransformTest


class TransformLogTest(TransformTest):
    expect_df_no_shift = pd.DataFrame(
        data=[
            (0.0, 0.6931471805599453, 'd'),
            (1.0986122886681098, 1.3862943611198906, 'd'),
            (1.6094379124341003, 1.791759469228055, 'd'),
            (1.9459101490553132, 2.0794415416798357, 'd'),
            (2.1972245773362196, 2.302585092994046, 'e'),
            (2.3978952727983707, 2.4849066497880004, 'e'),
            (2.5649493574615367, 2.6390573296152584, 'e'),
            (2.70805020110221, 2.772588722239781, 'e'),
            (2.833213344056216, 2.8903717578961645, 'e'),
        ], columns = ['Ln(A)', 'Ln(B)', 'C']
    )

    expect_df_shift = pd.DataFrame(
        data=[
            (0.6931471805599453, 1.0986122886681098, 'd'),
            (1.3862943611198906, 1.6094379124341003, 'd'),
            (1.791759469228055, 1.9459101490553132, 'd'),
            (2.0794415416798357, 2.1972245773362196, 'd'),
            (2.302585092994046, 2.3978952727983707, 'e'),
            (2.4849066497880004, 2.5649493574615367, 'e'),
            (2.6390573296152584, 2.70805020110221, 'e'),
            (2.772588722239781, 2.833213344056216, 'e'),
            (2.8903717578961645, 2.9444389791664403, 'e'),
        ], columns = ['Ln(A)', 'Ln(B)', 'C']
    )


    def assert_variable_names_and_symbols(self, vc: VariableCollection):
        assert str(vc.a.log().symbol) == r'\text{Ln}(\text{A})'
        assert str(vc.b.log().symbol) == r'\text{Ln}(\text{B})'
        assert vc.a.log().name == 'Ln(A)'
        assert vc.b.log().name == 'Ln(B)'


class TestLogTransform(TransformLogTest):

    def test_log_no_shift(self):
        vc, a, b, c = self.create_variable_collection()
        self.create_csv()
        all_cols = self.create_columns()
        load_variables = [
            vc.a.log(),
            vc.b.log(),
            c
        ]
        ds = self.create_source(df=None, columns=all_cols, load_variables=load_variables)
        assert_frame_equal(ds.df, self.expect_df_no_shift)
        self.assert_variable_names_and_symbols(vc)

    def test_log_with_shift(self):
        vc, a, b, c = self.create_variable_collection()
        self.create_csv()
        all_cols = self.create_columns()
        load_variables = [
            vc.a.log(1),
            vc.b.log(shift=1),
            c
        ]
        ds = self.create_source(df=None, columns=all_cols, load_variables=load_variables)
        assert_frame_equal(ds.df, self.expect_df_shift)
        self.assert_variable_names_and_symbols(vc)
