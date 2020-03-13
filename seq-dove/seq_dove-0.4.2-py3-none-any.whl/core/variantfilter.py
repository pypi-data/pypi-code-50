# -*- coding: utf-8 -*-
__author__ = 'bars'

import sys
import pandas as pd
from dove.utils.vcf import Vcf
from dove.utils.bed import Bed


class VariantFilter:

    """Docstring for VariantFilter. """

    def __init__(self, df, file_type, filter_columns=None, drop_duplicates=None, columns=None, bed_file=None, logic_gate='&&'):
        self.df = df
        self.df_orig = df
        self.file_type = file_type
        self.filter_columns = filter_columns
        self.drop_duplicates = drop_duplicates
        self.columns = columns
        self.bed_file = bed_file
        self.logic_gate = logic_gate

    def filter_variants(self):
        filtered_dfs = []

        if self.bed_file is not None:
            self.df = self.filter_with_bed()
            if self.logic_gate in self.logic_gates('_os'):
                filtered_dfs.append(self.df)
                self.df = self.df_orig

        if self.filter_columns is not None:
            filter_columns = [
                {
                    'filter_column': filter_column[0],
                    'filter_option': filter_column[1].lower(),
                    'filter_args': filter_column[2:],
                } for filter_column in self.filter_columns
            ]

            for filter_column in filter_columns:
                self.df = self.filter_with_column(filter_column)
                if self.logic_gate in self.logic_gates('_os'):
                    filtered_dfs.append(self.df)
                    self.df = self.df_orig

        self.conjuct(filtered_dfs)

        if self.drop_duplicates is not None:
            self.df.drop_duplicates(self.drop_duplicates, inplace=True)

        if self.columns is not None:
            self.drop_keep()

        return self.df

    def conjuct(self, filtered_dfs):
        if self.logic_gate in self.logic_gates('_os'):
            self.df = pd.concat(filtered_dfs)

    def filter_with_column(self, filter_column):
        try:
            if filter_column['filter_option'] in self.in_ex_options():
                return self.includes_excludes(
                    filter_column['filter_column'], filter_column['filter_option'], filter_column['filter_args'])
            elif filter_column['filter_option'] in self.eq_ne_options():
                return self.equals_notequals(
                    filter_column['filter_column'], filter_column['filter_option'], filter_column['filter_args'])
            elif filter_column['filter_option'] in self.l_g_options():
                return self.less_greater(
                    filter_column['filter_column'], filter_column['filter_option'], filter_column['filter_args'])
        except KeyError as e:
            sys.stderr.write('Please fix here: \033[4;31m{}\033[0m\n'.format(
                str(e)
            ))
            sys.exit()
        else:
            sys.stderr.write('Option cannot be "{}". Possible options are: {}\n'.format(
                filter_column['filter_option'],
                ', '.join(self.in_ex_options() + self.eq_ne_options() + self.l_g_options())
            ))
            sys.exit()

    def filter_with_bed(self):
        bed = Bed(self.bed_file)
        df_bed = bed.from_file()

        if self.file_type == 'annotation':
            self.df['POS'] = self.df['LOC'].str.split('-').str[0]
            self.df['POS'] = self.df['POS'].apply(pd.to_numeric)

        idx = pd.IntervalIndex.from_arrays(
            df_bed['START'], df_bed['END'], closed='both')
        df_bed.set_index(idx, inplace=True)
        if self.file_type == 'annotation':
            mask = self.df.apply(lambda x: [
                                 x['POS'] in y for y in df_bed.loc[df_bed.CHR == x.CHR, ].index], axis=1)
        if self.file_type == 'vcf':
            mask = self.df.apply(lambda x: [
                                 x['POS'] in y for y in df_bed.loc[df_bed.CHR == x.CHROM, ].index], axis=1)
        mask = mask.apply(lambda x: sum(x)) > 0
        self.df = self.df[mask]

    def equals_notequals(self, column, filter_option, filter_args):
        df_filter = pd.DataFrame(filter_args, columns=[column])
        if filter_option in self.eq_ne_options('eq'):
            if filter_args[0].lower() in ['none', 'null', 'nan']:
                return self.df[self.df[column].isnull()]
            return self.df[self.df[column].isin(df_filter[column])]
        if filter_option in self.eq_ne_options('ne'):
            if filter_args[0].lower() in ['none', 'null', 'nan']:
                return self.df[~self.df[column].isnull()]
            return self.df[~self.df[column].isin(df_filter[column])]

    def less_greater(self, column, filter_option, filter_args):
        if filter_option in self.l_g_options('lt'):
            return self.df[pd.to_numeric(self.df[column], downcast='float') < float(filter_args[0])]
        if filter_option in self.l_g_options('le'):
            return self.df[pd.to_numeric(self.df[column], downcast='float') <= float(filter_args[0])]
        if filter_option in self.l_g_options('gt'):
            return self.df[pd.to_numeric(self.df[column], downcast='float') > float(filter_args[0])]
        if filter_option in self.l_g_options('ge'):
            return self.df[pd.to_numeric(self.df[column], downcast='float') >= float(filter_args[0])]

    def includes_excludes(self, column, filter_option, filter_args):
        if filter_option in self.in_ex_options('in'):
            filter_option = True
        if filter_option in self.in_ex_options('ex'):
            filter_option = False

        return self.df[self.df[column].str.contains('|'.join(filter_args), case=False, na=False) == filter_option]

    def drop_keep(self):
        column_option = self.columns[0]
        columns = self.columns[1:]
        try:
            if column_option in self.drop_keep_options('keep'):
                self.df = self.df[self.keep_columns]
            elif column_option in self.drop_keep_options('drop'):
                self.df.drop(columns, axis=1, inplace=True)
        except KeyError as e:
            sys.stderr.write('Please fix here: \033[0;31m\033[4m{}\033[0m\n'.format(
                str(e)
            ))
            sys.exit()
        else:
            sys.stderr.write('Option cannot be "{}". Possible options are: {}\n'.format(
                column_option,
                self.drop_keep_options()
            ))
            sys.exit()

    def eq_ne_options(self, option=None):
        eqs = ['eq', 'equal', 'equals']
        nes = ['ne', 'notequals', 'not_equals']
        if option == 'eq':
            return eqs
        elif option == 'ne':
            return nes
        else:
            return eqs + nes

    def l_g_options(self, option=None):
        lts = ['lt', 'lessthan', 'less_than']
        les = ['le', 'lessequal', 'less_equals',
               'lessthanorequals', 'less_than_or_equals']
        gts = ['gt', 'greaterthan', 'greater_than']
        ges = ['ge', 'greaterequals', 'greater_equals',
               'greaterthanorequals', 'greater_than_or_equals']
        if option == 'lt':
            return lts
        elif option == 'le':
            return les
        elif option == 'gt':
            return gts
        elif option == 'ge':
            return ges
        else:
            return lts + les + gts + ges

    def in_ex_options(self, option=None):
        ins = ['in', 'include', 'includes']
        exs = ['ex', 'exclude', 'excludes']
        if option == 'in':
            return ins
        elif option == 'ex':
            return exs
        else:
            return ins + exs

    def drop_keep_options(self, option=None):
        ks = ['k', 'keep']
        ds = ['d', 'drop']
        if option == 'k':
            return ks
        elif option == 'd':
            return ds
        else:
            return ks + ds

    def logic_gates(self, option=None):
        _as = ['and', '&', '&&', '∧']
        _os = ['or', '|', '||', '∨']
        if option == 'as':
            return _as
        elif option == '_os':
            return _os
        else:
            return _as + _os


def main(args):
    input_file = args.input
    output_file = args.output
    bed_file = args.bed_file
    filter_columns = args.filter_column
    drop_duplicates = args.drop_duplicates
    columns = args.columns
    logic_gate = args.logic_gate

    if input_file.endswith('.tsv'):
        df = pd.read_csv(input_file, sep='\t', low_memory=False)
        VF = VariantFilter(df, 'annotation', filter_columns, drop_duplicates,
                           columns, bed_file, logic_gate)
        df = VF.filter_variants()
        df.to_csv(output_file, sep='\t', index=False)
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file, low_memory=False)
        VF = VariantFilter(df, 'annotation', filter_columns, drop_duplicates,
                           columns, bed_file, logic_gate)
        df = VF.filter_variants()
        df.to_csv(output_file, index=False)
    if input_file.endswith(('.vcf', '.vcf.gz')):
        with Vcf(input_file) as vcf:
            VF = VariantFilter(vcf.vdf, 'vcf', filter_columns, drop_duplicates,
                               columns, bed_file, logic_gate)
            vcf.vdf = VF.filter_variants()
            vcf.to_vcf(output_file)
