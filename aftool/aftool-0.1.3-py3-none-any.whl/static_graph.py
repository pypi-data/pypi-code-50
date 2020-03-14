# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     static_graph
   Description :
   Author :       23mofang
   date：          2020/3/14
-------------------------------------------------
   Change Activity:
                   2020/3/14:
-------------------------------------------------
"""
__author__ = 'Asdil'
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid')


def scatter(df, x, y, label=None, size=10, shape=True, xy_limit=None, title=None,
            figsize=(16, 9), dpi=100, plot_dense=0, save_path=None):
    """scatter方法用于画散点图

    Parameters
    ----------
    df : pandas.DataFrame
        pandas DataFrame 对象
    x: str
        x数据列名
    y: str
        y数据列名
    label: str or None
        类标签列名
    size: int
        散点大小
    shape: bool
        不同类不同图形
    xy_limit: list
        xy轴坐标范围, example = [xmin, xmax, ymin, ymax]
    title: str or None
        标题
    figsize : tuple
        图形长宽比默认(16:9)
    plot_dense: int
        画出密度分布 0不画 1画密度分布圈图, 2画密度分布bar图
    dpi: int
        分辨率默认100
    save_path: str
        保存路径
    Returns
    ----------
    """
    # 设置长宽分辨率，坐标轴范围
    plt.figure(figsize=figsize, dpi=dpi)
    if xy_limit:
        plt.axis(xy_limit)
    legend = 'full' if label else None
    shape = label if shape else None
    ax = sns.scatterplot(x=x,
                         y=y,
                         s=[size]*len(df),
                         hue=label,
                         style=shape,
                         legend=legend,
                         data=df)
    if plot_dense == 1:
        sns.kdeplot(df[x], df[y], ax=ax)
    elif plot_dense == 2:
        sns.kdeplot(df[x], df[y], ax=ax)
        sns.rugplot(df[x], color="g", ax=ax)
        sns.rugplot(df[y], vertical=True, color="r", ax=ax)

    if legend:
        plt.legend(loc='best', bbox_to_anchor=(1.094, 1.01), fancybox=True, shadow=True)
    if title:
        plt.title(f'{title}', fontsize=20)
    if save_path:
        plt.savefig(f'{save_path}')