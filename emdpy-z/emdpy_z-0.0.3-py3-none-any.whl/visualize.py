'''
    可视化
'''

import matplotlib.pyplot as plt


def plot_imfs(imfs, res, col=1):

    subplot_num = len(imfs)+1
    # IMF
    for i in range(len(imfs)):
        plt.subplot(subplot_num, col, i+1)
        plt.plot(imfs[i][0], imfs[i][1])
        plt.xlabel('IMF' + str(i + 1))
        plt.ylabel('y')
        plt.xlim(imfs[i][0][0], imfs[i][0][-1])
    if res.shape != (2,):
        # residual
        plt.subplot(subplot_num, col, len(imfs)+1)
        plt.plot(res[0], res[1])
        plt.xlabel('residual')
        plt.ylabel('y')
        plt.xlim(res[0][0], res[0][-1])
    plt.show()