import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp
import numpy as np
import random


def bubblesort(a, l, r):
    swapped = True
    for i in range(r):
        if not swapped:
            return
        swapped = False
        for j in range(r - i):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
            yield a


def insertionsort(a, l, r):
    for j in range(l+1, r+1):
        key = a[j]
        i = j - 1

        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
            yield a  # yield the current position of elements in a

        a[i + 1] = key
        yield a


def quicksort(a, l, r):
    if l >= r:
        return
    x = a[l]
    j = l

    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
        yield a

    a[l], a[j] = a[j], a[l]
    yield a
    yield from quicksort(a, l, j - 1)  # yield from statement used to yield the array after dividing
    yield from quicksort(a, j + 1, r)


def mergesort(A, start, end):
    if end <= start:
        return
    mid = start + ((end - start + 1) // 2) - 1

    yield from mergesort(A, start, mid)  # yield from statement is used to yield the array from the merge function
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)


def merge(A, start, mid, end):  # function to merge the array
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i in range(len(merged)):
        A[start + i] = merged[i]
        yield A


def show_graph_3d(fname):

    # animation function to be repeatedly called
    def animate(A, rects, iteration):
        # to clear the bars from the Poly3DCollection object
        ax.collections.clear()
        ax.bar3d(range(len(a)), A, z, dx, dy, dz, color=color_map(data_normalizer(range(n))))
        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0]))

    n = 100  # for random unique values
    a = [i for i in range(1, n + 1)]
    random.shuffle(a)
    generator = fname(a, 0, len(a) - 1)  # generator object returned by the function

    plt.style.use('fivethirtyeight')  # style of the chart
    data_normalizer = mp.colors.Normalize()  # set colors of the bars
    color_map = mp.colors.LinearSegmentedColormap(
        "my_map", {
            "red": [(0, 1.0, 1.0), (1.0, .5, .5)],
            "green": [(0, 0.5, 0.5), (1.0, 0, 0)],
            "blue": [(0, 0.50, 0.5), (1.0, 0, 0)]
        }
    )

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    z = np.zeros(n)  # z values and positions of the bars
    dx = np.ones(n)
    dy = np.ones(n)
    dz = [i for i in range(len(a))]

    rects = ax.bar3d(range(len(a)), a, z, dx, dy, dz, color=color_map(data_normalizer(range(n))))  # Poly3dCollection returned into variable rects

    # setting and x and y limits equal to the length of the array
    ax.set_xlim(0, len(a))
    ax.set_ylim(0, int(1.1 * len(a)))
    ax.set_title(str(fname))

    # text to plot on the chart
    text = ax.text2D(0.1, 0.95, "", horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, color="#E4365D")
    iteration = [0]

    # animate function is called here and the generator object is passed
    anim = FuncAnimation(fig, func=animate, fargs=(rects, iteration), frames=generator, interval=50, repeat=False)
    plt.show()


def show_graph_2d(fname):

    # function to be called repeatedly to animate
    def animate(A, rects, iteration):
        # setting the size of each bar equal to the value of the elements
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0]))

    n = 100  # input the size of the array (list here) and shuffle the elements to create a random list
    a = [i for i in range(1, n + 1)]
    random.shuffle(a)

    generator = fname(a, 0, len(a) - 1)  # generator object returned by the function
    data_normalizer = mp.colors.Normalize()  # to set the colors of the bars.
    color_map = mp.colors.LinearSegmentedColormap(
        "my_map", {
            "red": [(0, 1.0, 1.0), (1.0, .5, .5)],
            "green": [(0, 0.5, 0.5), (1.0, 0, 0)],
            "blue": [(0, 0.50, 0.5), (1.0, 0, 0)]
        }
    )

    fig, ax = plt.subplots()
    rects = ax.bar(range(len(a)), a, align="edge", color=color_map(data_normalizer(range(n))))  # the bar container

    ax.set_xlim(0, len(a))  # setting the view limit of x and y axes
    ax.set_ylim(0, int(1.1 * len(a)))
    ax.set_title(str(fname))

    # the text to be shown on the upper left indicating the number of iterations transform indicates the position with relevance to the axes coordinates.
    text = ax.text(0.01, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    anim = FuncAnimation(fig, func=animate, fargs=(rects, iteration), frames=generator, interval=50, repeat=False)
    plt.show()


if __name__ == '__main__':
    show_graph_2d(bubblesort)
    show_graph_2d(insertionsort)
    show_graph_3d(insertionsort)
    show_graph_3d(quicksort)
    show_graph_3d(mergesort)

# https://www.geeksforgeeks.org/insertion-sort-visualization-using-matplotlib-in-python/
# https://www.geeksforgeeks.org/3d-visualisation-of-insertion-sort-using-matplotlib-in-python/
# https://www.geeksforgeeks.org/3d-visualisation-of-quick-sort-using-matplotlib-in-python/
# https://www.geeksforgeeks.org/3d-visualisation-of-merge-sort-using-matplotlib/
