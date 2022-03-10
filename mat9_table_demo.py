import numpy as np
import matplotlib.pyplot as plt


def table_demo():
    data = [[66386, 174296, 75131, 577908, 32015],
            [58230, 381139, 78045, 99308, 160454],
            [89135, 80552, 152558, 497981, 603535],
            [78415, 81858, 150656, 193263, 69638],
            [139361, 331509, 343164, 781380, 52269]]

    columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
    rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]

    values = np.arange(0, 2500, 500)
    value_increment = 1000

    # Get some pastel shades for the colors
    colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
    n_rows = len(data)

    index = np.arange(len(columns)) + 0.3
    bar_width = 0.4

    y_offset = np.zeros(len(columns))  # Initialize the vertical-offset for the stacked bar chart.

    cell_text = []  # Plot bars and create text labels for the table
    for row in range(n_rows):
        plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
        y_offset = y_offset + data[row]
        cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])

    colors = colors[::-1]  # Reverse colors and text labels to display the last value at the top.
    cell_text.reverse()

    # Add a table at the bottom of the axes
    the_table = plt.table(cellText=cell_text, rowLabels=rows, rowColours=colors, colLabels=columns, loc='bottom')

    plt.subplots_adjust(left=0.2, bottom=0.2)  # Adjust layout to make room for the table:
    plt.ylabel("Loss in ${0}'s".format(value_increment))
    plt.yticks(values * value_increment, ['%d' % val for val in values])
    plt.xticks([])
    plt.title('Loss by Disaster')
    plt.show()


if __name__ == '__main__':
    table_demo()

# https://matplotlib.org/stable/gallery/misc/table_demo.html