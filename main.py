from code.classes import battery, district, house, model
from code.algorithms import random, hillclimber
from code.solutions import save_solution
from code.visualisatie import histogram, scatterplot
from code.experiments.random_experiment import random_experiment
from code.experiments.hillclimber_experiment import hillclimber_experiment


from statistics import mean

import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    """ creation of district object """
    file = "data/Huizen&Batterijen/district_1"
    # object district aanmaken bestaande uit batteries en huizen data
    district_test = district.District(file)

    """ random algoritme """
    # random_experiment.baseline(district_test, 1000)


    """ Hillclimber algortihm """
    # hillclimber_experiment.hillclimb(district_test)
    hillclimber_experiment.multiple_runs(district_test, 1, 1, 1000)
    # hillclimber_experiment.house_counter_hillclimb(district_test, 1,  1, 1000)

    """ housecounter algoritme """

    """ simulated annealing """





    # plt.plot(range(1101), smallest_model.values)
    # plt.show()

    # histogram.plotting_histogram(list_costs)
    # scatterplot.show_scatterplot(smallest_solution, multiple_plots = False)
    # print(len(smallest_solution.cables))
    # print(smallest_solution.return_total_costs())

    # print(len(smallest_solution.cables))
