import numpy as np
import matplotlib.pyplot as plt
from code.classes.model import Model

def plotting_histogram(array_input):
    bins_list = 30
    plt.hist(array_input, bins = bins_list)
    plt.xlabel('Sum of cable length')
    plt.ylabel('Frequency')
    plt.title('Histogram random + greedy')
    plt.show()
    # plt.clear()
