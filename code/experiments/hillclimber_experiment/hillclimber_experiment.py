from code.algorithms import random, hillclimber, housecounter
import matplotlib.pyplot as plt
from code.solutions import save_solution
from code.classes import model
from code.visualisatie import histogram, scatterplot


def hillclimb(number_of_switch, iterations, solution):
    """ run hillclimber, given number of houses to switch and number of iterations """
    climber = hillclimber.HillClimber(solution)

    print("Running the hillclimber...")
    print(f"Costs before hillclimber: {climber.model.return_total_costs()}")
    climber.run(iterations, number_of_switch)
    all_costs = climber.values

    best_model = climber.model

    print(f"Costs after hillclimber: {climber.model.return_total_costs()}")

    return best_model, all_costs


def house_counter_hillclimb(district, runs, number_of_switch, iterations):
    smallest_solution = model.Model(district)
    lowest_costs_hist = []
    while smallest_solution.is_solution() is False:
        housecount = housecounter.Housecounter(smallest_solution)
        smallest_solution = housecount.run_housecounter()

    lowest_costs_hist.append(smallest_solution.return_total_costs())
    start_cost = 40000
    for i in range(runs):
        best_model, costs = hillclimb(number_of_switch, iterations, smallest_solution)
        lowest_costs_hist.append(best_model.return_total_costs())
        print(best_model.return_total_costs())
        if start_cost > best_model.return_total_costs():
            start_cost = best_model.return_total_costs()
            optimal_model = best_model
            cost = costs

    # saving_plots(district, runs, number_of_switch, iterations, cost, lowest_costs_hist, optimal_model, "housecounter")
    return lowest_costs_hist



def multiple_runs(district, runs, number_of_switch, iterations, random_runs):
    start_cost = 40000
    lowest_costs_hist = []
    for i in range(runs):
        random_solution, costs = random.run(random_runs, district)
        best_model, costs = hillclimb(number_of_switch, iterations, random_solution)
        lowest_costs_hist.append(best_model.return_total_costs())
        if start_cost > best_model.return_total_costs():
            start_cost = best_model.return_total_costs()
            optimal_model = best_model
            cost = costs

    # saving_plots(district, runs, number_of_switch, iterations, cost, lowest_costs_hist, optimal_model, "random_+_greedy")
    return lowest_costs_hist



def saving_plots(district, runs, number_of_switch, iterations, costs_flow, total_costs_hist, optimal_model, start_model):
    # save scatterplot of best solution
    scatterplot.show_scatterplot(optimal_model, multiple_plots = False)
    plt.savefig(f"code/experiments/hillclimber_experiment/grid_district_{district.district}_iterations_{iterations}")
    plt.close()

    # save plot showing convergence of algoritme of the best solution
    plt.plot(range(iterations + 1), costs_flow)
    plt.xlabel("Iterations")
    plt.ylabel("Total costs")
    plt.title(f"Best solution of hillclimber in combination with {start_model}.")
    plt.ylim(30300, 32000)
    plt.savefig(f"code/experiments/hillclimber_experiment/{start_model}_runs_{runs}_iterations_{iterations}")
    plt.close()

    # save histogram of all outcomes after running hillclimber on start_model
    histogram.plotting_histogram(total_costs_hist, "Total costs", "Frequency", f"Hill climber with start solution from: {start_model} ({iterations})")
    plt.savefig(f"code/experiments/hillclimber_experiment/histogram_{start_model}_district_{district.district}_iterations_{iterations}")
    plt.close()

    # save best solution in json file
    save_solution.save(f"hillclimber_experiment/{start_model}_district_{district.district}_iterations_{iterations}.json", optimal_model)
