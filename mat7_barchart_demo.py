import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


def attach_ordinal(num):
    suffixes = {str(i): v for i, v in enumerate(['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th'])}
    v = str(num)

    if v in {'11', '12', '13'}:  # special case early teens
        return v + 'th'
    return v + suffixes[v[-1]]


def format_score(score, test):
    unit = test_units[test]
    if unit:
        return f'{score}\n{unit}'
    else:  # If no unit, don't include a newline, so that label stays centered.
        return score


def format_ycursor(y):
    y = int(y)
    if y < 0 or y >= len(test_names):
        return ''
    else:
        return test_names[y]


def plot_student_results(student, scores, cohort_size):
    fig, ax1 = plt.subplots(figsize=(9, 7))  # Create the figure
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')

    pos = np.arange(len(test_names))
    rects = ax1.barh(pos, [scores[k].percentile for k in test_names], align='center', height=0.5, tick_label=test_names)

    ax1.set_title(student.name)
    ax1.set_xlim([0, 100])
    ax1.xaxis.set_major_locator(MaxNLocator(11))
    ax1.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)
    ax1.axvline(50, color='grey', alpha=0.25)  # Plot a solid vertical gridline to highlight the median position

    ax2 = ax1.twinx()  # Set the right-hand Y-axis ticks and labels
    ax2.set_yticks(pos)  # Set the tick locations
    ax2.set_ylim(ax1.get_ylim())  # Set equal limits on both yaxis so that the ticks line up
    ax2.set_yticklabels([format_score(scores[k].score, k) for k in test_names])  # Set the tick labels
    ax2.set_ylabel('Test Scores')

    xlabel = 'Percentile Ranking Across {grade} Grade {gender}s \n Cohort Size: {cohort_size}'
    ax1.set_xlabel(xlabel.format(grade=attach_ordinal(student.grade), gender=student.gender.title(), cohort_size=cohort_size))

    rect_labels = []  # Lastly, write in the ranking inside each bar to aid in interpretation
    for rect in rects:
        # Rectangle widths are already integer-valued but are floating type, so it helps to remove the trailing decimal point and 0 by converting width to int type
        width = int(rect.get_width())
        rank_str = attach_ordinal(width)
        # The bars aren't wide enough to print the ranking inside
        if width < 40:
            xloc = 5  # Shift the text to the right side of the right edge
            clr = 'black'  # Black against white background
            align = 'left'
        else:
            xloc = -5  # Shift the text to the left side of the right edge
            clr = 'white'  # White on magenta
            align = 'right'

        # Center the text vertically in the bar
        yloc = rect.get_y() + rect.get_height() / 2
        label = ax1.annotate(rank_str, xy=(width, yloc), xytext=(xloc, 0), textcoords="offset points", horizontalalignment=align, verticalalignment='center', color=clr, weight='bold', clip_on=True)
        rect_labels.append(label)

    ax2.fmt_ydata = format_ycursor  # Make the interactive mouse over give the bar title
    return {'fig': fig, 'ax': ax1, 'ax_right': ax2, 'bars': rects, 'perc_labels': rect_labels}  # Return all of the artists created


Student = namedtuple('Student', ['name', 'grade', 'gender'])
Score = namedtuple('Score', ['score', 'percentile'])

# GLOBAL CONSTANTS
test_names = ['Pacer Test', 'Flexed Arm Hang', 'Mile Run', 'Agility', 'Push Ups']
test_units = dict(zip(test_names, ['laps', 'sec', 'min:sec', 'sec', '']))

student = Student('Johnny Doe', 2, 'boy')
scores = dict(zip(test_names, (Score(v, p) for v, p in zip(['7', '48', '12:52', '17', '14'], np.round(np.random.uniform(0, 100, len(test_names)), 0)))))
cohort_size = 62  # The number of other 2nd grade boys

arts = plot_student_results(student, scores, cohort_size)
plt.show()

# https://matplotlib.org/stable/gallery/statistics/barchart_demo.html