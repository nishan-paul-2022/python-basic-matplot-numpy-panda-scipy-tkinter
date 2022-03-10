import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook


def scatter_demo():
    price_data = cbook.get_sample_data('goog.npz', np_load=True)['price_data']
    price_data = price_data[-250:]  # get the most recent 250 trading days
    delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]
    volume = (15 * price_data.volume[:-2] / price_data.volume[0])**2  # Marker size in units of points^2
    close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]

    fig, ax = plt.subplots()
    ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)
    ax.set_xlabel(r'$\Delta_i$', fontsize=15)
    ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
    ax.set_title('Volume and percent change')
    ax.grid(True)
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    scatter_demo()

# Load a numpy record array from yahoo csv data with fields date, open, close, volume, adj_close from the
# C:\Users\Nishan Paul\Anaconda3\envs\m2021\Lib\site-packages\matplotlib\mpl-data\sample_data\E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter\goog.npz directory.
# The record array stores the date as an np.datetime64 with a day unit ('D') in the date column.

# https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html
