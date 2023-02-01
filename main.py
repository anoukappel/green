from code.classes import battery, district, house, model
from code.algorithms import random, hillclimber
from code.solutions import save_solution
from code.visualisatie import histogram, scatterplot
from code.experiments.random_experiment import random_experiment
from code.experiments.hillclimber_experiment import hillclimber_experiment
from code.experiments.simulated_annealing import simulatedannealing_experiment

from statistics import mean

import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    """ creation of district object """
    wijk = 1
    file = f"data/Huizen&Batterijen/district_{wijk}"
    # object district aanmaken bestaande uit batteries en huizen data
    district_test = district.District(file)

    """ The experiments """
    """ random algoritme """
    # random_experiment.baseline(district_test, 1000)


    """ Hillclimber algortihm """
    #parameters used in the hillclimber, if changed and algorithm is runned again than new plots will be saved
    number_of_runs = 50
    houses_to_switch = 1
    iterations = 2000
    random_runs = 10

    # run the algorithm using the best of a number of random solutions as a starting point
    # hillclimber_experiment.multiple_runs(district_test, number_of_runs, houses_to_switch, iterations, random_runs)
    # run the algorithm using house_counter solution as a starting point
    hillclimber_experiment.house_counter_hillclimb(district_test, number_of_runs,  houses_to_switch, iterations)

    """ simulated annealing """
    # # parameters used in simulated annealing algorithm, if changed and algorithm is runned again than new plots will be saved
    number_of_runs = 1
    houses_to_switch = 1
    iterations = 1000
    start_temp = 50
    raise_temp = 20
    random_runs = 10
    #
    # # run the algorithm using house_counter solution as a starting point
     # simulatedannealing_experiment.house_counter_simulated_an(district_test, number_of_runs, houses_to_switch, iterations, start_temp, raise_temp)
    #
    # # run the algorithm using the best of a number of random solutions as a starting point
    # simulatedannealing_experiment.random_simulated_an(district, random_runs, number_of_runs, houses_to_switch, iterations, start_temp, raise_temp)
