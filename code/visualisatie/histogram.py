import numpy as np
import matplotlib.pyplot as plt
from code.classes.model import Model

def plotting_histogram(array_input):
    bins_list = 30
    plt.hist(array_input, bins = bins_list)
    plt.xlabel('Total costs')
    plt.ylabel('Frequency')
    plt.title('Histogram random greedy(10x) + simulated annealing')
    plt.show()
    plt.close()
    # plt.clear()
