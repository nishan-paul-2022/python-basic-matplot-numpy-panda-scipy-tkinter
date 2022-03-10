import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook


def date():
    years = mdates.YearLocator()   # every year
    months = mdates.MonthLocator()  # every month
    years_fmt = mdates.DateFormatter('%Y')

    data = cbook.get_sample_data('goog.npz', np_load=True)['price_data']
    fig, ax = plt.subplots()
    ax.plot('date', 'adj_close', data=data)

    # format the ticks
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)
    ax.xaxis.set_minor_locator(months)

    # round to nearest years.
    datemin = np.datetime64(data['date'][0], 'Y')
    datemax = np.datetime64(data['date'][-1], 'Y') + np.timedelta64(1, 'Y')
    ax.set_xlim(datemin, datemax)

    # format the coords message box
    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax.format_ydata = lambda x: '$%1.2f' % x  # format the price.
    ax.grid(True)

    fig.autofmt_xdate()  # rotates and right aligns the x labels, and moves the bottom of the axes up to make room for them
    plt.show()


if __name__ == '__main__':
    date()

# Load a numpy record array from yahoo csv data with fields date, open, close, volume, adj_close from the
# C:\Users\Nishan Paul\Anaconda3\envs\kgf\Lib\site-packages\matplotlib\mpl-data\sample_data\E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter\goog.npz directory.
# The record array stores the date as an np.datetime64 with a day unit ('D') in the date column.

# https://matplotlib.org/stable/gallery/text_labels_and_annotations/date.html