import matplotlib.pyplot as plt
import seaborn as sns
from .Generalplot import Generalplot

class Plot1d(Generalplot):
    """ Generic plotting class for visualizing data based on one variable.

    Attributes:
        variable (string) respresenting variable name
        title (string) representing the title of the plot (optional)
        """

    def __init__(self, df, variable, title=None):

        Generalplot.__init__(self, title)

        self.variable = variable
        self.df = df



    def histplot(self):
        """
        Function to output a histogram of the instance variable data using
		matplotlib pyplot library.

        Args:
			None

		Returns:
			None
        """
        plt.subplots(figsize = [self.width, self.height])

        plt.hist(self.df[self.variable], bins = 50)

        plt.xlabel(self.variable)
        plt.ylabel("Frequency")
        if self.title:
            plt.title(self.title)
        else:
            plt.title("Histogram of variable '{}'".format(self.variable))

    def barplot(self):
        """
        Function to output a bar plot of the instance variable data using
		seaborn and matplotlib pyplot libraries.

        Args:
			None

		Returns:
			None
        """
        base_color = sns.color_palette()[0]

        plt.subplots(figsize = [self.width, self.height])

        sns.countplot(data = self.df, x = self.variable, color = base_color)

        plt.xlabel(self.variable)
        plt.ylabel("Frequency")
        if self.title:
            plt.title(self.title)
        else:
            plt.title("Barplot of variable '{}'".format(self.variable))
