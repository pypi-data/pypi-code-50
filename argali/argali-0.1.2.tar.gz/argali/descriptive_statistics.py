import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np


class Univariate:
    """
    Useful Resources: https://www.andrews.edu/~calkins/math/webtexts/statall.pdf

    x = [1, 2, 3, 4, 3, 4, 5, 6, 7, 6, 7, 8, 7, 8, 8, 6, 5, 44, 3, 4, 5, 6, 7, 8, 9, 33, 22, 11, -1]
    x_summary = Univariate(data=x)
    x_summary.descriptive_summary()

    """
    def __init__(self, data):
        self.data = data

    def unique_value_list(self):
        unique_values = []
        for i in sorted(self.data):
            if i not in unique_values:
                unique_values.append(i)

        return unique_values

    def unique_value_count(self):
        return len(self.unique_value_list())

    def unique_value_frequency(self):
        unique_values = self.unique_value_list()

        value_count_list = []
        for x in unique_values:
            value_count = 0
            for i in sorted(self.data):
                if x == i:
                    value_count += 1
            value_count_list.append(value_count)

        return value_count_list

    def mean(self):
        mean = sum(self.data) / len(self.data)
        return mean

    def geometric_mean(self):
        product = 1
        for x in self.data:
            product = product * x

        geometric_mean = product ** (1/len(self.data))

        return geometric_mean

    def harmonic_mean(self):
        reciprocal = []
        for i in self.data:
            reciprocal.append(i ** -1)
        harmonic_mean = sum(reciprocal)/len(reciprocal)

        return harmonic_mean

    def quadratic_mean(self):
        squared = []
        for i in self.data:
            squared.append(i ** 2)
        quadratic_mean = ((1/len(squared)) * sum(squared)) ** 0.5
        return quadratic_mean

    def median(self):
        pass

    def mode(self):
        pass

    def range(self):
        return max(self.data) - min(self.data)

    def quartiles(self):
        pass

    def absolute_deviation(self):
        pass

    def variance(self):
        pass

    def z_score(self):
        pass

    def upper_hinge(self):
        pass

    def lower_hinge(self):
        pass

    def percentiles(self):
        pass

    def deviation_from_mean_list(self):
        mean = self.mean()
        deviation_from_mean_list = []
        for i in sorted(self.data):
            deviation_from_mean_list.append(i - mean)

        return deviation_from_mean_list

    def deviation_squared_list(self):
        deviation_squared = []
        for i in self.deviation_from_mean_list():
            deviation_squared.append(i ** 2)

        return deviation_squared

    def variance(self):
        sum_deviations = sum(self.deviation_squared_list())
        variance = sum_deviations / len(self.deviation_squared_list())

        return variance

    def standard_deviation(self):
        sqrt = self.variance() ** 0.5

        return sqrt

    def unique_value_distribution(self):
        fig2 = plt.figure(constrained_layout=True, figsize=(16, 10))
        spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig2)

        f2_ax1 = fig2.add_subplot(spec2[0, 0])
        plt.hist(sorted(self.data))
        plt.plot(self.unique_value_list(),
                 self.unique_value_frequency(),
                 label='Occurrence Count', marker='o')
        plt.xlabel('Unique Value')
        plt.ylabel('Frequency')
        plt.title("Unique Value Frequency Distribution")

        f2_ax2 = fig2.add_subplot(spec2[0, 1])
        plt.boxplot(self.data, notch=True, vert=False)
        plt.xlabel('Unique Value')
        plt.title("Box Plot")

        f2_ax3 = fig2.add_subplot(spec2[1, 0])
        num_bins = round(self.unique_value_count() / 3)
        sigma = self.standard_deviation()
        mu = self.mean()
        n, bins, patches = plt.hist(self.data, num_bins, density=1)
        y = ((1 / (((2 * np.pi) ** 0.5) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
        plt.plot(bins, y, '--')
        plt.xlabel('Bin')
        plt.ylabel('Frequency')
        plt.title("Frequency Distribution")

        f2_ax4 = fig2.add_subplot(spec2[1, 1])
        plt.plot(self.deviation_squared_list())
        plt.xlabel('Unique Value')
        plt.ylabel('Squared Difference')
        plt.title("Squared Difference Plot")

        return fig2

    def descriptive_summary(self):
        print("Descriptive Summary")
        print("-----------------")
        print("Number of Unique Values: ", self.unique_value_count())
        print("Mean: ", self.mean())
        print("Geometric Mean: ", self.geometric_mean())
        print("Harmonic Mean: ", self.harmonic_mean())
        print("Quadratic Mean: ", self.quadratic_mean())
        print("Range: ", self.range())
        print("-----------------")
        self.unique_value_distribution()
        plt.show()

class Bivariate:
    pass

class Multivariate:
    pass

x = [1, 2, 3, 4, 3, 4, 5, 6, 7, 6, 7, 8, 7, 8, 8, 6, 5, 44, 3, 4, 5, 6, 7, 8, 9, 33, 22, 11, -1]
x_summary = Univariate(data=x)
x_summary.descriptive_summary()