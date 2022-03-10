import numpy as np
import matplotlib.pyplot as plt


def legend():
    # Make some fake data.
    a = b = np.arange(0, 3, .02)
    c = np.exp(a)
    d = c[::-1]

    # Create plots with pre-defined labels.
    fig, ax = plt.subplots()
    ax.plot(a, c, 'k--', label='Model length')
    ax.plot(a, d, 'k:', label='Data length')
    ax.plot(a, c + d, 'k', label='Total message length')

    legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('C0')  # Put a nicer background color on the legend.
    plt.show()


if __name__ == '__main__':
    legend()

# https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend.html