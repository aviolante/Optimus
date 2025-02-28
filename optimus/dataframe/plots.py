from pyspark.sql import DataFrame

from optimus import PYSPARK_NUMERIC_TYPES
from optimus.functions import plot_hist, plot_freq, plot_boxplot, plot_scatterplot, plot_correlation
from optimus.helpers.decorators import add_attr
from optimus.helpers.functions import parse_columns, check_column_numbers
from optimus.dataframe.extension import sample_n

import matplotlib.pyplot as plt

import statsmodels.api as sm


def plot(self):
    @add_attr(plot)
    def hist(columns=None, buckets=10, output=None, path=None):
        """
        Plot histogram
        :param columns: Columns to be printed
        :param buckets: Number of buckets
        :param output:
        :param path:
        :return:
        """
        columns = parse_columns(self, columns, filter_by_column_dtypes=PYSPARK_NUMERIC_TYPES)
        check_column_numbers(columns, "*")

        for col_name in columns:
            data = self.cols.hist(col_name, buckets)
            plot_hist({col_name: data}, output=output, path=path)

    @add_attr(plot)
    def scatter(columns=None, buckets=30, output=None, path=None):
        """
        Plot boxplot
        :param columns: columns to be printed
        :param buckets: number of buckets
        :param output:
        :param path:
        :return:
        """
        columns = parse_columns(self, columns, filter_by_column_dtypes=PYSPARK_NUMERIC_TYPES)
        check_column_numbers(columns, "*")

        data = self.cols.scatter(columns, buckets)
        plot_scatterplot(data, output=output, path=path)

    @add_attr(plot)
    def box(columns=None, output=None, path=None):
        """
        Plot boxplot
        :param columns: Columns to be printed
        :param output:
        :param path:
        :return:
        """
        columns = parse_columns(self, columns, filter_by_column_dtypes=PYSPARK_NUMERIC_TYPES)
        check_column_numbers(columns, "*")

        for col_name in columns:
            stats = self.cols.boxplot(col_name)
            plot_boxplot({col_name: stats}, output=output, path=path)

    @add_attr(plot)
    def frequency(columns=None, buckets=10, output=None, path=None):
        """
        Plot frequency chart
        :param columns: Columns to be printed
        :param buckets: Number of buckets
        :param output:
        :param path:
        :return:
        """
        columns = parse_columns(self, columns)

        for col_name in columns:
            data = self.cols.frequency(col_name, buckets)
            plot_freq(data, output=output, path=path)

    @add_attr(plot)
    def correlation(col_name, method="pearson", output=None, path=None):
        """
        Compute the correlation matrix for the input data set of Vectors using the specified method. Method
        mapped from pyspark.ml.stat.Correlation.
        :param col_name: The name of the column for which the correlation coefficient needs to be computed.
        :param method: String specifying the method to use for computing correlation. Supported: pearson (default),
        spearman.
        :return: Heatmap plot of the corr matrix using seaborn.
        """

        corr = self.correlation(col_name, method, output="array")
        plot_correlation(corr, output=output, path=path)

    return plot

    @add_attr(plot)
    def qqplots(dataframe=data, grid_rows=3, grid_cols=3, n_obs=100):
        """
        QQ Plots
        :param dataframe: spark dataframe
        :param grid_rows: number of rows to include in plotting grid
        :param grid_cols: number of columns to include in plotting grid
        :param n_obs: number of observations (sample) to plot
        """

        sample_data = sample_n(dataframe, n=n_obs, random=True)
        feature_list = parse_columns(sample_data, cols_args='*', filter_by_column_dtypes='int')

        fig = plt.figure(figsize=(12, 5))

        for feature, num in zip(feature_list, range(1, len(feature_list))):
            ax = fig.add_subplot(grid_rows, grid_cols, num)

            sm.qqplot(sample_data.toPandas()[feature], line='q', ax=ax, color='C0', alpha=0.3)
            ax.set_xlabel('')
            ax.set_ylabel('')
            ax.set_title(feature.upper())

        plt.tight_layout()

DataFrame.plot = property(plot)
