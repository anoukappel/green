import numpy as np
import matplotlib.pyplot as plt
from code.classes.model import Model

def plotting_histogram(array_input, x_title, y_title, title):
    bins_list = 50
    plt.hist(array_input, bins = bins_list)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.title(title)
    # plt.show()
    # plt.savefig('graph_histo.png', dpi=300, bbox_inches='tight')
#     plt.close()
