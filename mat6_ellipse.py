import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse


def ellipse_demo():
    NUM = 250
    ells = [Ellipse(xy=np.random.rand(2) * 10, width=np.random.rand(), height=np.random.rand(), angle=np.random.rand() * 360) for i in range(NUM)]
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

    for e in ells:
        ax.add_artist(e)
        e.set_clip_box(ax.bbox)
        e.set_alpha(np.random.rand())
        e.set_facecolor(np.random.rand(3))

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    plt.show()


def ellipse_rotated():
    angle_step = 45  # degrees
    angles = np.arange(0, 360, angle_step)
    ax = plt.subplot(aspect='equal')

    for angle in angles:
        ellipse = Ellipse((0, 0), 4, 2, angle=angle, alpha=0.1)
        ax.add_artist(ellipse)

    plt.xlim(-2.2, 2.2)
    plt.ylim(-2.2, 2.2)
    plt.show()


if __name__ == '__main__':
    ellipse_demo()
    ellipse_rotated()

# https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_demo.html