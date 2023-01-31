
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
    plt.savefig(f'hist:{letters}, start_temp:{start_temp}, raise_temp:{raise_temp}.jpg')
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
