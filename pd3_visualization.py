import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def data_visualization():
    df1 = pd.read_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd3_df1.csv', index_col=0)
    df2 = pd.read_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd3_df2.csv')

    df1['A'].hist(), plt.title('hist'), plt.show()
    plt.style.use('bmh'), df1['A'].hist(), plt.title('bmh'), plt.show()
    plt.style.use('fivethirtyeight'), df1['A'].hist(), plt.title('fivethirtyeight'), plt.show()
    plt.style.use('dark_background'), df2.plot.area(alpha=0.4), plt.title('dark_background'), plt.show()
    df2.plot.bar(), plt.title('bar'), plt.show()
    df2.plot.bar(stacked=True), plt.title('bar'), plt.show()
    df1['A'].plot.hist(bins=50), plt.title('hist'), plt.show()
    df1.plot.scatter(x='A', y='B'), plt.title('scatter'), plt.show()
    df1.plot.scatter(x='A', y='B', c='C', cmap='coolwarm'), plt.title('scatter'), plt.show()
    df1.plot.scatter(x='A', y='B', s=df1['C'] * 200), plt.title(''), plt.title('scatter'), plt.show()
    df2.plot.box(), plt.title('box'), plt.show()
    df2['a'].plot.kde(), plt.title('kde'), plt.show()
    df2.plot.density(), plt.title('density'), plt.show()

    df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
    df.plot.hexbin(x='a', y='b', gridsize=25, cmap='Oranges'), plt.title('hexbin'), plt.show()


def box_plot():
    df = pd.read_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd3_tips.csv')
    df.boxplot(by='day', column=['total_bill']), plt.title('boxplot'), plt.show()
    df.boxplot(by='size', column=['tip'], grid=False), plt.title('boxplot'), plt.show()


data_visualization()
box_plot()

# https://www.geeksforgeeks.org/pandas-built-in-data-visualization-ml/
# https://www.geeksforgeeks.org/box-plot-visualization-with-pandas-and-seaborn/