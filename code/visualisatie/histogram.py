import numpy as np
import matplotlib.pyplot as plt
from code.classes.model import Model

def plotting_histogram(array_input, x_title: str, y_title: str, title: str) -> None:
    """
    Plots a single histogram.
    """
    bins_list = 50
    plt.hist(array_input, bins = bins_list)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.title(title)


def multiple_histograms(costs_ar_1, name_1, costs_ar_2, name_2, costs_ar_3 = False, name_3 = '', costs_ar_4 = False, name_4 = '') -> None:
    """
    Plots mutiple histograms in one plot.
    """
    fig, ax = plt.subplots()
    ax.hist(costs_ar_1, 10, None, ec='red', fc='none', lw=1.5, histtype='step', label= name_1)
    ax.hist(costs_ar_2, 10, None, ec='green', fc='none', lw=1.5, histtype='step', label= name_2)
    if costs_ar_3:
        ax.hist(costs_ar_3, 10, None, ec='blue', fc='none', lw=1.5, histtype='step', label= name_3)
    if costs_ar_4:
        ax.hist(costs_ar_4, 10, None, ec='yellow', fc='none', lw=1.5, histtype='step', label= name_4)

    ax.legend(loc='upper right')
