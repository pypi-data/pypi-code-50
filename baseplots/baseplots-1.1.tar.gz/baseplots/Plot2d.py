import matplotlib.pyplot as plt
import seaborn as sns
from .Generalplot import Generalplot

class Plot2d(Generalplot):
    """ Generic plotting class for visualizing data based on two variables.

    Attributes:
        variable_list (list of strings) respresenting variable names
        title (string) representing the title of the plot (optional)
        """

    def __init__(self, df, variable_list, title=None):

        Generalplot.__init__(self, title)

        assert len(variable_list) > 1

        self.variable_list = variable_list[:2]

        self.df = df

    def scatterplot(self):
        """
        Function to output a scatterplot of the two first variables or
        variable_list, interpreted as x and y, using
		seaborn and matplotlib pyplot libraries.

        Args:
			None

		Returns:
			None
        """
        plt.subplots(figsize = [self.width, self.height])

        x_var = self.variable_list[0]
        y_var = self.variable_list[1]

        sns.regplot(data = self.df, x = x_var, y = y_var, fit_reg = False,
           y_jitter = 0, x_jitter = 0, scatter_kws = {'alpha' : 1/2});

        plt.xlabel(x_var)
        plt.ylabel(y_var)
        if self.title:
            plt.title(self.title)
        else:
            plt.title("Scatterplot: {} vs. {}".format(x_var, y_var))

    def boxplot(self):
        """
        Function to output a box of the two first variables of
        variable_list, interpreted as x (categorical) and y (numeric), using
		seaborn and matplotlib pyplot libraries.

        Args:
			None

		Returns:
			None
        """
        base_color = sns.color_palette()[0]

        plt.subplots(figsize = [self.width, self.height])

        x_var = self.variable_list[0]
        y_var = self.variable_list[1]

        sns.boxplot(data = self.df, x = x_var, y = y_var, color=base_color)

        plt.xlabel(x_var)
        plt.ylabel(y_var)
        if self.title:
            plt.title(self.title)
        else:
            plt.title("Boxplot: '{}' distribution per '{}'".format(y_var, x_var))
