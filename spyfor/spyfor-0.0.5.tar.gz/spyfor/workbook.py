import pandas as pd
import xlsxwriter as xl

from .Format_Regression_Output import PrintRegressions as PrintRegressions
from .Format_Regression_Output import PrintCorrelations as PrintCorrelations
from .Format_Regression_Output import PrintDescriptive as PrintDescriptive
from .Reg_Obj import RegObject as RegObject
from .Stata_Reg_Obj import res_obj as res_obj
from .Stata_Reg_Obj import spearman_obj as spearman_obj
from .Stata_Reg_Obj import pearson_obj as pearson_obj
from .Stata_Reg_Obj import summary_line


class tableWorkBook:
    def __init__(self, print_directory, appendix=None):
        if type(appendix) == str:
            try:
                self.df_appendix = pd.read_csv(filepath_or_buffer=appendix)
            except UnicodeDecodeError:
                try:
                    self.df_appendix = pd.read_csv(filepath_or_buffer=appendix, encoding="ISO-8859-1")
                except:
                    self.df_appendix = None
                    print("Error Loading Appendix.  Proceeding with no Appendix")
        elif isinstance(appendix, pd.DataFrame):
            self.df_appendix = appendix
        else:
            self.df_appendix = None
            print("No Appendix Loaded")
        # the nan option means that the code will print infinitives instead of erroring out the code.
        self.workbook = xl.Workbook(print_directory, {'nan_inf_to_errors': True})
        self.res_list = []
        self.sheet_counter = 1
        self.printer = None

        self.pearson = None
        self.spearman = None

        self.summary_list = []

    def capture_des(self, var_name):
        self.summary_list.append(summary_line(var_name))

    def compile_des(self, sheet_title="Table A", sheet_sub_title="Descriptive Statistics", mean=True,
                    median=True, per_25=False, per_5=False, per_1=False, min_max=False, kurtosis=False, skewness=False,
                    sd=True, var=False, obs=True, des_order=None):

        format_list = ['var_name']
        if obs:
            format_list.append('obs')
        if mean:
            format_list.append("mean")
        if median:
            format_list.append("median")
        if sd:
            format_list.append('sd')
        if var:
            format_list.append('var')
        if per_25:
            format_list.append("p25")
            format_list.append("p75")
        if per_5:
            format_list.append("p5")
            format_list.append("p95")
        if per_1:
            format_list.append("p1")
            format_list.append("p99")
        if min_max:
            format_list.append("min")
            format_list.append("max")
        if kurtosis:
            format_list.append('kurtosis')
        if skewness:
            format_list.append('skewness')

        des_list_of_list = []
        for variable in self.summary_list:
            des_list_of_list.append(variable.get_line())

        df_descriptives = pd.DataFrame(des_list_of_list, columns=summary_line.get_header())
        # This limits the descriptives to the elements that the user has requested
        df_descriptives = df_descriptives[format_list]

        des_printer = PrintDescriptive(workbook=self.workbook, df_descriptive=df_descriptives, sheet_title=sheet_title,
                                       sheet_sub_title=sheet_sub_title, df_appendix=self.df_appendix,
                                       des_order=des_order)


    def capture_regression_information(self):
        """"Captures regression information from Stata and stores information in Python"""
        self.res_list.append(res_obj())

    def capture_pearson(self):
        self.pearson = pearson_obj()

    def capture_spearman(self):
        """ Captures the spearman matrix from stata.  The user needs to use pwcorr , sig for this comman to work"""
        self.spearman = spearman_obj()

    def compile_corr(self, sheet_title="Table B", sheet_sub_title="Correlations", top='pearson'):
        if self.pearson is None:
            print("No pearson correlations collected")
        if self.spearman is None:
            print("No spearman correlations collected")
        corr_printer = PrintCorrelations(workbook=self.workbook, pearson_obj=self.pearson, sheet_title=sheet_title, sheet_sub_title=sheet_sub_title,
                                              spearman_obj=self.spearman, top=top, df_appendix=self.df_appendix)

    def compile_worksheet(self, sheet_title=None, sheet_sub_title=None, display_control=True, display_se=False,
                          interest_variables=[], control_variables=[]):
        """Compiles information from regressions into a worksheet and clears temporary regression storage"""
        if sheet_title is None:
            sheet_title = "Table " + str(self.sheet_counter)
        if sheet_sub_title is None:
            sheet_sub_title = "Insert Table Description Here"
        regression_object = RegObject(self.res_list, interest_variables, control_variables)
        self.printer = PrintRegressions(reg_obj=regression_object, print_workbook=self.workbook, sheet_title=sheet_title,
                         sheet_sub_title=sheet_sub_title, df_appendix=self.df_appendix,
                         display_control=display_control, display_se=display_se)
        # adds 1 to the sheet counter in case the user does not specifiy table names
        self.sheet_counter += 1

        # clears out the results list so that the list of specifications does not keep growing.
        self.res_list = []

    def print_workbook(self):
        """Prints the excel workbook to the specified filename"""
        self.workbook.close()



