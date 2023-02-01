
from code.algorithms import random, simulatedannealing, housecounter
import matplotlib.pyplot as plt
import copy
import csv
from code.solutions import save_solution
from code.classes import model
from code.visualisatie import histogram, scatterplot
from code.experiments import random_experiment


def simulated_an(number_of_switch, iterations, solution, start_temp, raise_temp, iterations_without_change):
    """ run simulated annealing, given number of houses to switch and number of iterations """
    sa = simulatedannealing.SimulatedAnnealing(solution, start_temp, raise_temp, iterations_without_change)
    print("Running the simulated annealing...")
    print(f"Costs before simulated annealing: {sa.model_temp.return_total_costs()}")
    sa.run(iterations, number_of_switch)

    lowest_costs = sa.best_model.return_total_costs()
    best_model = sa.best_model
    costs_flow = sa.values
    print(f"Costs after simulated annealing: {lowest_costs}")

    return best_model, lowest_costs, costs_flow

def house_counter_simulated_an(district, runs, number_of_switch, iterations, start_temp, raise_temp, iterations_without_change):
    smallest_solution = model.Model(district)
    while smallest_solution.is_solution() is False:
        housecount = housecounter.Housecounter(smallest_solution)
        smallest_solution = housecount.run_housecounter()

    start_cost = 40000
    cost = []
    for i in range(runs):
        best_model, lowest_costs, costs = simulated_an(number_of_switch, iterations, smallest_solution, start_temp, raise_temp, iterations_without_change)
        if start_cost > best_model.return_total_costs():
            start_cost = best_model.return_total_costs()
            optimal_model = best_model
            costs_flow = costs
            cost.append(lowest_costs)
    letters = "HC_SA"

    saving_plots(district, runs, number_of_switch, iterations, costs_flow, cost, start_temp, raise_temp, optimal_model, letters)




def random_simulated_an(district, random_runs, runs, number_of_switch, iterations, start_temp, raise_temp, iterations_without_change):
    start_cost = 40000
    cost = []
    for i in range(runs):
        random_solution, costs = random.run(random_runs, district)
        best_model, lowest_costs, costs = simulated_an(number_of_switch, iterations, random_solution, start_temp, raise_temp, iterations_without_change)
        if start_cost > best_model.return_total_costs():
            start_cost = best_model.return_total_costs()
            costs_flow = costs
            cost.append(lowest_costs)
            optimal_model = best_model
    letters = "RG_SA"

    saving_plots(district, runs, number_of_switch, iterations, costs_flow, cost, start_temp, raise_temp, optimal_model, letters)



def saving_plots(district, runs, number_of_switch, iterations, costs_flow, total_costs_hist, start_temp, raise_temp, optimal_model, start_model):

    # save scatterplot of best solution
    scatterplot.show_scatterplot(optimal_model, multiple_plots = False)
    plt.savefig(f"code/experiments/simulated_annealing_experiments/grid_district_{district.district}_iterations_{iterations}")
    plt.close()

    # save x, y plot showing convergence of algoritme of the best solution
    plt.plot(range(len(costs_flow)), costs_flow)
    plt.xlabel("Iterations")
    plt.ylabel("Total costs")
    plt.title(f"Best solution of simulated annealing in combination with {start_model}.")
    plt.savefig(f"code/experiments/simulated_annealing_experiments/{start_model}_runs_{runs}_starttemp_{start_temp}_raise_temp_{raise_temp}")
    plt.close()

    # save histogram of all outcomes after running simulated annealing  on start_model
    histogram.plotting_histogram(total_costs_hist, "Total costs", "Frequency", f"{start_model} ({iterations})")
    plt.savefig(f"code/experiments/simulated_annealing_experiments/histogram_{start_model}_district_{district.district}_starttemp_{start_temp}_raise_temp_{raise_temp}")
    plt.close()

    # save solution in json format
    save_solution.save(f"simulated_annealing_experiments/{start_model}_district_{district.district}_starttemp_{start_temp}_raise_temp_{raise_temp}.json", optimal_model)
