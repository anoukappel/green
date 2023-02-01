from code.algorithms import housecounter
import matplotlib.pyplot as plt
import copy
import csv
from code.solutions import save_solution
from code.classes import model
from code.visualisatie import histogram, scatterplot


def run_housecounter(district, runs):
    """
    Runs the housecounter algorithm for x times. Keeps track of all the cost of
    each run.
    """
    cost = []
    for i in range(runs):
        solution = model.Model(district)
        while solution.is_solution() is False:
            housecount = housecounter.Housecounter(solution)
            solution = housecount.run_housecounter()
            costs = solution.return_total_costs()
            cost.append(costs)

    saving_plots(district, runs, solution, cost)


def saving_plots(district, runs, solution, cost):
    """
    Plots a grid of all connections of houses and batteries. A histogram of de frequency
    and the scores. And a json file with all the connections.
    """
    # save scatterplot of best solution
    scatterplot.show_scatterplot(solution, multiple_plots = False)
    plt.savefig(f"code/experiments/housecounter_experiments/grid_district_{district.district}_runs_{runs}")
    plt.close()

    # save histogram of all outcomes after running simulated annealing  on start_model
    histogram.plotting_histogram(cost, "Total costs", "Frequency", f"House counter ({runs})")
    plt.savefig(f"code/experiments/housecounter_experiments/histogram_district_{district.district}_runs_{runs}.png")
    plt.close()

    # save solution in json format
    save_solution.save(f"housecounter_experiments/_district_{district.district}_runs_{runs}.json", solution)