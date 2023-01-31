from code.classes import battery, district, house, model
from code.algorithms import random
from code.solutions import save_solution
from code.visualisatie import histogram, scatterplot
from code.experiments import simulatedannealing_experiment

from statistics import mean

import matplotlib.pyplot as plt
import numpy as np

from code.algorithms import hillclimber, simulatedannealing, housecounter

import subprocess
import time

if __name__ == "__main__":
    """ creation of district object """
    file = "data/Huizen&Batterijen/district_1"
    # object district aanmaken bestaande uit batteries en huizen data
    district_test = district.District(file)

    # #housecounter
    # list_cable_lengths = []
    # for i in range(1000):
    #     smallest_solution = model.Model(district_test)
    #     while smallest_solution.is_solution() is False:
    #         housecount = housecounter.Housecounter(smallest_solution)
    #         smallest_solution = housecount.run_housecounter()
    #     list_cable_lengths.append(smallest_solution.return_total_costs())
    # histogram.plotting_histogram(list_cable_lengths)


    # simulatedannealing_experiment.random_simulated_an(district_test, 1, 1, 1, 1000, 10, 25)
    simulatedannealing_experiment.house_counter_simulated_an(district_test, 5, 1, 100, 10, 25)





    # smallest_solution, list_cable_lengths = random.run(10, district_test)
    #
    # print(len(smallest_solution.cables))
    #
    # # Plotting histogram greedy + random
    # histogram.plotting_histogram(list_cable_lengths)


    #
    # average = mean(list_cable_lengths)
    # print(f"Average sum of cables using random + greedy algorithm is: {average}" )

    # Showing plot of all batteries
    # scatterplot.show_scatterplot(smallest_solution, multiple_plots = False)
    # # Showing a plot of each battery
    # scatterplot.show_scatterplot(smallest_solution)

    # """ Hillclimber algortihm """
    # model_test = model.Model(district_test)
    #

    # smallest_solution = model.Model(district_test)
    # while smallest_solution.is_solution() is False:
    # #     # smallest_solution, list_cable_lengths = random.run(10, district_test)
    # # # list_cable_lengths = []
    #     housecount = housecounter.Housecounter(smallest_solution)
    #     # housecount.fill_blocks()
    #     smallest_solution = housecount.run_housecounter()


    # for i in range(50):
    #     housecount.fill_blocks()
    #     smallest_solution = housecount.connect_all_blocks()
    #     # if smallest_solution.is_solution() == True:
    #     best_costs = smallest_solution.return_total_costs()
    #     list_cable_lengths.append(best_costs)
    # print(list_cable_lengths)


            # smallest_solution = random.random_assignment(smallest_solution)
    # print(len(smallest_solution.cables))
    # print(smallest_solution.return_total_costs())
    # scatterplot.show_scatterplot(smallest_solution, multiple_plots = False)

    # Showing a plot of each battery
    # scatterplot.show_scatterplot(smallest_solution)
        # model_2 = model.Model(district_test)
        # model_test = random.random_assignment(model_2)
    # print(len(smallest_solution.cables))

    # print(len(model_test.cables))
    # print(f"totale kosten voor HillClimber: {model_test.get_total_costs()}")
    # print("hillclimber is beginning:")
    # hill_algo = hillclimber.HillClimber(model_test)
    # hill_algo.switch_random_houses_from_battery()
    #

    # start = time.time()
    # n_runs = 0
    #
    # while time.time() - start < 120:
    # list_cable_lengths = []
    # # for i in range(10):
    # while smallest_solution.is_solution() is False:
    #     smallest_solution, list_cable_length = random.run(1, district_test)
    # print("run SA")
    # sa = simulatedannealing.SimulatedAnnealing(smallest_solution, 10)
    # sa.run_hillclimber(10000, 1)
    # best_model = sa.model_temp
    # best_costs = best_model.return_total_costs()
    # print(best_costs)
    # print(sa.lowest_value)
    # list_cable_lengths.append(best_costs)
    #
    # # histogram.plotting_histogram(list_cable_lengths)
    #
    #
    #
    #
    # #
    # plt.plot(range(10000), sa.y)
    # plt.show()
    # # plt.savefig('RG, 500, 1000 (10b).jpg')



from code.algorithms import random, simulatedannealing, housecounter
import matplotlib.pyplot as plt
import copy
import csv
from code.solutions import save_solution
from code.classes import model
from code.visualisatie import histogram
from code.experiments import random_experiment


def simulated_an(number_of_switch, iterations, solution, start_temp, raise_temp):
    """ run simulated annealing, given number of houses to switch and number of iterations """
    sa = simulatedannealing.SimulatedAnnealing(solution, start_temp, raise_temp)
    print("Running the simulated annealing...")
    print(f"Costs before simulated annealing: {sa.model_temp.return_total_costs()}")
    sa.run_hillclimber(iterations, number_of_switch)

    lowest_costs = sa.best_model.return_total_costs()
    best_model = sa.best_model

    print(f"Costs after simulated annealing: {lowest_costs}")

    return best_model, lowest_costs

def house_counter_simulated_an(district, runs, number_of_switch, iterations, start_temp, raise_temp):
    smallest_solution = model.Model(district)
    while smallest_solution.is_solution() is False:
        housecount = housecounter.Housecounter(smallest_solution)
        smallest_solution = housecount.run_housecounter()

    start_cost = 40000
    cost = []
    for i in range(runs):
        best_model, lowest_costs = simulated_an(number_of_switch, iterations, smallest_solution, start_temp, raise_temp)
        if start_cost > best_model.return_total_costs():
            start_cost = best_model.return_total_costs()
            optimal_model = best_model
            cost.append(lowest_costs)
    letters = "HC SA"

    saving_plots(runs, cost, letters, start_temp, raise_temp)



def random_simulated_an(district, random_runs, runs, number_of_switch, iterations, start_temp, raise_temp):
    start_cost = 40000
    cost = []
    for i in range(runs):
        random_solution, costs = random.run(random_runs, district)
        best_model, lowest_costs = simulated_an(number_of_switch, iterations, random_solution, start_temp, raise_temp)
        if start_cost > best_model.return_total_costs():
            start_cost = best_model.return_total_costs()
            cost.append(lowest_costs)
    letters = "RG SA"

    saving_plots(runs, cost, letters, start_temp, raise_temp)





def saving_plots(runs, cost, letters, start_temp, raise_temp):

    histogram.plotting_histogram(cost)
    plt.savefig(f'hist: {letters}, start_temp: {start_temp}, raise_temp: {raise_temp}.jpg')
    plt.show()

    # plt.plot(range(runs), sa.values)
    # # plt.savefig('RG, 500, 1000 (10b).jpg')
    #
    #
    # best_model, lowest_costs = hillclimber(district)
    #
    # histogram
    #
    # plaatje grid
