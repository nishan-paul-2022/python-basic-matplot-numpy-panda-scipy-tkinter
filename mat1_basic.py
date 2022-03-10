import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm


def line_plot_1():
    x = [10, 20, 30, 40]  # data for plotting
    y = [20, 30, 40, 50]

    plt.plot(x, y)  # plotting the data
    plt.xlabel('x-axis')  # Adding the labels
    plt.ylabel('y-axis')
    plt.title('Simple Plot')  # Adding the title
    plt.show()


def line_plot_2():
    t = np.arange(0.0, 2.0, 0.01)  # data for plotting
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
    # ax.grid()
    # fig.savefig('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/imatplot.png')
    plt.show()


def multiple_subplots():
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)

    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle('A tale of Two subplots')

    ax1.plot(x1, y1, 'o-')
    ax1.set_ylabel('Damped oscillation')

    ax2.plot(x2, y2, '.-')
    ax2.set_xlabel('time (s)')
    ax2.set_ylabel('Undamped')

    plt.show()


def multiple_plot_types():  # Many plot types can be combined in one figure to create powerful and flexible representations of data.
    data = np.random.randn(2, 100)

    fig, axs = plt.subplots(2, 2, figsize=(5, 5))
    axs[0, 0].hist(data[0])
    axs[0, 1].plot(data[0], data[1])
    axs[1, 0].scatter(data[0], data[1])
    axs[1, 1].hist2d(data[0], data[1])
    plt.show()


def image_demo():
    delta = 0.025
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(- X ** 2 - Y ** 2)
    Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)
    Z = (Z1 - Z2) * 2

    fig, ax = plt.subplots()
    ax.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn, origin='lower', extent=[-3, 3, -3, 3], vmax=abs(Z).max(), vmin=-abs(Z).max())
    plt.show()


if __name__ == '__main__':
    line_plot_1()
    line_plot_2()
    multiple_subplots()
    multiple_plot_types()
    image_demo()


# https://matplotlib.org/stable/gallery/images_contours_and_fields/image_demo.html