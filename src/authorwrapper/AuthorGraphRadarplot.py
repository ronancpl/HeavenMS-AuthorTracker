# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import ceil
from math import pi

from authortrackwriter import AuthorGraphResultPrinter


def createYtickDict(ydiv_interval, max_val):
    ydiv_item_ticks = ceil(max_val / ydiv_interval)

    yticks_counts = []
    yticks_labels = []
    ylim = (0, ydiv_item_ticks * ydiv_interval)

    for i in range(1, ydiv_item_ticks):
        tick_value = i * ydiv_interval

        yticks_counts.append(tick_value)
        yticks_labels.append(str(tick_value))

    ret = {}
    ret['counts'] = yticks_counts
    ret['labels'] = yticks_labels
    ret['limits'] = ylim

    return ret


def calcYticksInterval(max_val):
    # Fetch ylabel interval from max value, must be conformant between all indexes
    base_intervals = [10, 25]
    max_ticks = 7
    interval_mod = 0.5

    max_val = float(max_val)

    intervals = []
    min_ticks_idx = -1
    min_ticks_count = 2147483647
    for itv_idx in range(len(base_intervals)):
        base_itv = base_intervals[itv_idx]

        i = 0
        while True:
            itv = ((1 + (i * interval_mod)) * base_itv)

            ydiv_item_ticks = ceil(max_val / itv)
            if (ydiv_item_ticks <= max_ticks):
                break

            i += 1

        if min_ticks_count > ydiv_item_ticks:
            min_ticks_idx = itv_idx
            min_ticks_count = ydiv_item_ticks

        intervals.append(itv)

    min_ticks_itv = intervals[min_ticks_idx]
    yticks_dict = createYtickDict(min_ticks_itv, max_val)

    return yticks_dict


def isZeroList(values):
    for v in values:
        if v != 0:
            return False

    return True


def plot(data, csv_filename):
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    min_obs = 2147483647
    max_val = 0
    for k, v in data.items():
        if type(v) is not list:
            v = [v]
            data[k] = v

        if len(v) < min_obs:
            min_obs = len(v)

        for i in v:
            if i > max_val:
                max_val = i

    yticks = calcYticksInterval(max_val)
    yticks_counts = yticks['counts']
    yticks_labels = yticks['labels']
    yticks_limits = yticks['limits']

    df = pd.DataFrame(data)

    for idx in range(min_obs):
        plot_img = grapher.fetchGraphFilename(csv_filename, idx)

        # Radar Chart -- from https://python-graph-gallery.com/390-basic-radar-chart/

        # number of variable
        categories = list(df)[1:]
        N = len(categories)

        # We are going to plot the first line of the data frame.
        # But we need to repeat the first value to close the circular graph:
        values = df.loc[idx].drop('group').values.flatten().tolist()
        values += values[:1]

        # Do not plot empty cases
        if isZeroList(values):
            continue

        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        fig = plt.figure(dpi=1000, figsize=(6.40, 7.00))
        # plt.xticks(rotation=90, fontsize=4, fontweight=25)

        # Initialise the spider plot
        ax = plt.subplot(111, polar=True)

        # Draw one axe per variable + add labels labels yet
        plt.xticks(angles[:-1], categories, color='grey', size=8)

        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks(yticks_counts, yticks_labels, color="grey", size=7)
        plt.ylim(yticks_limits[0], yticks_limits[1])

        # Plot data
        ax.plot(angles, values, linewidth=1, linestyle='solid')

        # Fill area
        ax.fill(angles, values, 'b', alpha=0.1)

        grapher.savePlot(fig, plot_img)
        # plt.show()
        plt.close(fig)
