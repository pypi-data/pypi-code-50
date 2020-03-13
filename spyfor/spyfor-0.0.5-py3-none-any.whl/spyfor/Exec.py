from sfi import SFIToolkit as tool
from sfi import Data


class Exec:
    def __init__(self):
        pass

    @staticmethod
    def summary_statistics(workbook, var_list=None):
        # gets a list of all of the variables within the dataset
        all_list = []
        column_count = Data.getVarCount()
        for i in range(0, column_count):
            all_list.append(Data.getVarName(i))
        if var_list is None:
            var_list = all_list

        # ensuring that all of the variables that the user passed to the function are present within the data
        for var in var_list:
            if var not in all_list:
                print(var, " was not present within the dataset and has been removed from summary statistics")
                var_list.remove(var)
            else:
                tool.stata("summarize " + var + ", detail", echo=True)
                workbook.capture_des(var)
