from code.classes import battery, district, house, model
from code.algorithms import random, hillclimber
from code.solutions import save_solution
from code.visualisatie import histogram, scatterplot
from code.experiments import random_experiment

from statistics import mean

import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    """ creation of district object """
    file = "data/Huizen&Batterijen/district_1"
    # object district aanmaken bestaande uit batteries en huizen data
    district_test = district.District(file)

    """ random algoritme """
    random_experiment.baseline(district_test)
    # list_costs = []
    # for i in range(1):
    #     best_solution = 400000
    #     model_test = model.Model(district_test)
    #     for i in range(1):
    #         while model_test.is_solution() is False:
    #             model_2 = model.Model(district_test)
    #             model_test = random.random_assignment(model_2)
    #
    # print(model_test.is_solution())
    # save_solution.save("random_output", model_test)
            # if best_solution > model_test.return_total_costs():
            #     print(True)
            #     best_model = model_test
            #     print(model_test.return_total_costs())
            #     best_solution = model_test.return_total_costs()

        # list_costs.append(model_test.return_total_costs())
    #     # print(model_test.return_total_costs())
    # print(best_model.return_total_costs())
    # print(len(best_model.cables))


    """ Hillclimber algortihm """
    # list_costs = []
    # counter = 0
    # solution = 40000


    # # for i in range(20):
    #     best_solution = 400000
    #     model_test = model.Model(district_test)
    #     for i in range(100):
    #         while model_test.is_solution() is False:
    #             model_2 = model.Model(district_test)
    #             model_test = random.random_assignment(model_2)
    #         if best_solution > model_test.return_total_costs():
    #             best_model = model_test
    #             best_solution = model_test.return_total_costs()
    #
    #     model_test = best_model
    #     # model_test, cables = random.run(20, district_test)
    #
    #
    #     print(f"aantal cabels: {len(model_test.cables)}")
    #     print(f"totale kosten voor HillClimber: {model_test.return_total_costs()}")
    #     print("hillclimber is beginning:")
    #     hill_algo = hillclimber.HillClimber(model_test)
    #     # hill_algo.switch_random_houses_from_battery()
    #     #
    #     print("Running the Hill Climber")
    #     hill_algo.run_hillclimber(1100, 1)
    #     # print(f"totale kosten na HillClimber: {hill_algo.value}")
    #
    #     # plt.plot(range(1000), hill_algo.values)
    #     # print(len(hill_algo.values))
    #     # print(len(range(11)))
    #
    #     print(f"Total costs are: {hill_algo.model.return_total_costs()}")
    #     print(f"aantal cabels: {len(hill_algo.model.cables)}")
    #     list_costs.append(hill_algo.model.return_total_costs())
    #     if hill_algo.model.return_total_costs() < solution:
    #         smallest_solution = hill_algo.model
    #         smallest_model = hill_algo



    # plt.plot(range(1101), smallest_model.values)
    # plt.show()

    # histogram.plotting_histogram(list_costs)
    # scatterplot.show_scatterplot(smallest_solution, multiple_plots = False)
    # print(len(smallest_solution.cables))
    # print(smallest_solution.return_total_costs())

    # print(len(smallest_solution.cables))
