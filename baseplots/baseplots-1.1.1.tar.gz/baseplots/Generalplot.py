import pandas as pd

class Generalplot:

    """ Generic plotting class for visualizing data

    Attributes:
        var_list (list of strings) respresenting variable name(s)
        title (string) representing the title of the plot
        width (float) representing the width of the plot in inches
        height (float) representing the height of the plot in inches
        """

    def __init__(self, title, width=11.69, height=8.27):

        self.var_list = []
        self.title = title
        self.width = width
        self.height = height
        self.df = pd.DataFrame()


    def read_data_file(self, file_name):

        """Function to read in data from a csv file. The csv file should have
        headers (variable names) and consistent data type per column.

        Args:
            file_name (string): name of a file to read from

        Returns:
            None

        """

        self.df = pd.read_csv(r'.\{}'.format(file_name))
