from code.classes import battery, district, house, model
from code.algorithms import random, hillclimber
from code.solutions import save_solution
from code.visualisatie import histogram, scatterplot
from code.experiments.random_experiment import random_experiment
from code.experiments.hillclimber_experiment import hillclimber_experiment
from code.experiments.simulated_annealing_experiments import simulatedannealing_experiment
from code.experiments.housecounter_experiments import housecounter_experiments

from statistics import mean

import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    """ creation of district object """
    district_number = 1
    file = f"data/Huizen&Batterijen/district_{district_number}"
    # object district consisting of batteries and houses data
    district = district.District(file, district_number)


    """ The experiments """
    """ Random algoritme """
    iteraties = 10
    # random_experiment.baseline(district, iteraties)


    """ Housecounter algorithm"""
    # parameters used in the housecounter, if changed and algorithm is runned again than new plots will be saved
    runs = 1

    # running the algorithm
    # housecounter_experiments.run_housecounter(district, runs)


    """ Hillclimber algortihm """
    # parameters used in the hillclimber, if changed and algorithm is runned again than new plots will be saved
    number_of_runs = 1
    houses_to_switch = 1
    iterations = 10000
    random_runs = 10

    # run the algorithm using the best of a number of random solutions as a starting point
    # hist_hill_random = hillclimber_experiment.multiple_runs(district, number_of_runs, houses_to_switch, iterations, random_runs)
    # run the algorithm using house_counter solution as a starting point
    hist_hill_house = hillclimber_experiment.house_counter_hillclimb(district, number_of_runs,  houses_to_switch, iterations)


    """ Simulated annealing """
    # parameters used in simulated annealing algorithm, if changed and algorithm is runned again than new plots will be saved
    number_of_runs = 1
    houses_to_switch = 1
    iterations = 10000
    start_temp = 20
    raise_temp = 10
    random_runs = 1
    iterations_without_change = 500

    # run the algorithm using house_counter solution as a starting point
    #hist_SA_housecounter = simulatedannealing_experiment.house_counter_simulated_an(district, number_of_runs, houses_to_switch, iterations, start_temp, raise_temp, iterations_without_change)

    # run the algorithm using the best of a number of random solutions as a starting point
    #hist_SA_random = simulatedannealing_experiment.random_simulated_an(district, random_runs, number_of_runs, houses_to_switch, iterations, start_temp, raise_temp, iterations_without_change)


    """ Saving the histogram for all algorithms into one histogram. """

    # code voor histogram
    # smallest_solution, costs_rg = random.run(15, district)
    # smallest_solution_2, costs_test = random.run(30, district)
    #
    # best_model, costs_hi = hill_climber_experiment.hillclimb(district, 2, 15)
    # histogram.multiple_histograms(costs_rg, "random + greedy", costs_hi, "hillclimber", costs_ar_3 = costs_test, name_3 ="Test")


    # histogram.multiple_histograms(hist_hill_random, "hillclimber + random", hist_hill_house, "hillclimber + housecounter")
    #
    # plt.savefig(f"code/experiments/histogram_multiple_algoritms/{hist_hill_random}_{hist_hill_house}")
    # plt.close()
