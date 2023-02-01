from code.classes import battery, district, house, model
from code.algorithms import random
from code.solutions import save_solution
from code.visualisatie import histogram, scatterplot

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
    #
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

    """ Hillclimber algortihm """
    # model_test = model.Model(district_test)
    #

    smallest_solution = model.Model(district_test)
    while smallest_solution.is_solution() is False:
        # smallest_solution, list_cable_lengths = random.run(1, district_test)
    # list_cable_lengths = []
        housecount = housecounter.Housecounter(smallest_solution)
    #     # housecount.fill_blocks()
        smallest_solution = housecount.run_housecounter()

    # for i in range(50):
    #     housecount.fill_blocks()
    #     smallest_solution = housecount.connect_all_blocks()
    #     # if smallest_solution.is_solution() == True:
    #     best_costs = smallest_solution.return_total_costs()
    #     list_cable_lengths.append(best_costs)
    # print(list_cable_lengths)


            # smallest_solution = random.random_assignment(smallest_solution)

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
    # for i in range(10):
    # while smallest_solution.is_solution() is False:
    #     smallest_solution, list_cable_length = random.run(1, district_test)
    print("run SA")
    sa = simulatedannealing.SimulatedAnnealing(smallest_solution, 20, 10)
    sa.run_hillclimber(10000, 1)
    best_model = sa.best_model
    best_costs = best_model.return_total_costs()
    print(best_costs)
    print(sa.lowest_value)
    # list_cable_lengths.append(best_costs)

    # histogram.plotting_histogram(list_cable_lengths)




    #
    plt.plot(range(10000), sa.values)
    # plt.savefig('RG, 500, 1000 (10b).jpg')
    plt.show()
    plt.plot(range(10000), sa.temps)
    plt.show()
