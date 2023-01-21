from code.classes import battery, district, house, model
from code.algorithms import random
from code.solutions import save_solution
from code.visualisatie import histogram, scatterplot

from statistics import mean

import matplotlib.pyplot as plt
import numpy as np

from code.algorithms import greedy

if __name__ == "__main__":
    """ creation of district object """
    file = "data/Huizen&Batterijen/district_1"
    # object district aanmaken bestaande uit batteries en huizen data
    district_test = district.District(file)

    smallest_solution, list_cable_lengths = random.run(10, district_test)

    # print(len(smallest_solution.cables))

    # Plotting histogram greedy + random
    histogram.plotting_histogram(list_cable_lengths)

    # average = mean(list_cable_lengths)
    # print(f"Average sum of cables using random + greedy algorithm is: {average}" )

    # Showing plot of all batteries
    scatterplot.show_scatterplot(smallest_solution, multiple_plots = False)
    # Showing a plot of each battery
    scatterplot.show_scatterplot(smallest_solution)

    """ Hillclimber algortihm """
    model_test = model.Model(district_test)

    while model_test.is_solution() is False:
        model_2 = model.Model(district_test)
        model_test = random.random_assignment(model_2)

    print(len(model_test.cables))
    print(f"totale kosten voor HillClimber: {model_test.get_total_costs()}")
    print("hillclimber is beginning:")
    hill_algo = hillclimber.HillClimber(model_test)
    # hill_algo.switch_random_houses_from_battery()
    #
    print("Running the Hill Climber")
    hill_algo.run_hillclimber(1000, 1)
    # print(f"totale kosten na HillClimber: {hill_algo.value}")

    smallest_solution = hill_algo.model
    # print(len(smallest_solution.cables))
