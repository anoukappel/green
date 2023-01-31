
from code.algorithms import random, hillclimber, housecounter
import matplotlib.pyplot as plt
import copy
import csv
from code.solutions import save_solution
from code.classes import model
from code.visualisatie import histogram
from code.experiments import random_experiment


def hillclimb(number_of_switch, iterations, solution):
    """ run hillclimber, given number of houses to switch and number of iterations """
    # find best random solution out of 100 runs
    # random_solution, costs = random.run(1, district)
    # print(random_solution.is_solution())
    climber = hillclimber.HillClimber(solution)
    # running the hillclimber
    print("Running the hillclimber...")
    print(f"Costs before hillclimber: {climber.model.return_total_costs()}")
    climber.run_hillclimber(iterations, number_of_switch)
    costs = climber.values

    best_model = climber.model

    print(f"Costs after hillclimber: {climber.model.return_total_costs()}")

    return best_model, costs
    # print(climber.model.return_total_costs())

def house_counter_hillclimb(district, runs, number_of_switch, iterations):
    smallest_solution = model.Model(district)
    while smallest_solution.is_solution() is False:
        housecount = housecounter.Housecounter(smallest_solution)
        smallest_solution = housecount.run_housecounter()

    start_cost = 40000
    for i in range(runs):
        best_model, costs = hillclimb(number_of_switch, iterations, smallest_solution)
        if start_cost > best_model.return_total_costs():
            start_cost = best_model.return_total_costs()
            optimal_model = best_model
            cost = costs

    histogram.plotting_histogram(cost)



def multiple_runs(district, runs, number_of_switch, iterations):
    start_cost = 40000
    for i in range(runs):
        random_solution, costs = random.run(1, district)
        best_model, costs = hillclimb(number_of_switch, iterations, random_solution)
        if start_cost > best_model.return_total_costs():
            start_cost = best_model.return_total_costs()
            optimal_model = best_model
            cost = costs
            
    histogram.plotting_histogram(cost)





def saving_plots(district):

    best_model, costs = hillclimber(district)

    # histogram

    # plaatje grid
