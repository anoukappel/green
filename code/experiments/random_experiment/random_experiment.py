from code.algorithms import random
import matplotlib.pyplot as plt
# import copy
# import csv
from code.solutions import save_solution
# from code.classes import model
from code.visualisatie import histogram, scatterplot
# from code.algorithms import random

def baseline(district, iterations):
    """
    Create solid solutions given a number of iterations and save solution, histogram, grid of this solution.
    """
    optimal_model, costs = random.run(iterations, district)
    save_solution.save(f"random_experiment/district_{district.district}_iterations_{iterations}.json", optimal_model)

    histogram.plotting_histogram(costs, "Total costs", "Frequency", f"Histogram Greedy + random ({iterations})")
    plt.savefig(f"code/experiments/random_experiment/histogram_district_{district.district}_iterations_{iterations}")

    scatterplot.show_scatterplot(optimal_model, multiple_plots = False)
    plt.savefig(f"code/experiments/random_experiment/grid_district_{district.district}_iterations_{iterations}")
