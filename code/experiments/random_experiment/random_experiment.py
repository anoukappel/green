from code.algorithms import random
import matplotlib.pyplot as plt
from code.solutions import save_solution
from code.visualisatie import histogram, scatterplot
from code.classes.district import District
from code.solutions import save_solution

def baseline(district: District, iterations: int):
    """
    Create solid solutions given a number of iterations and save solution, histogram, grid of this solution.
    """
    optimal_model, costs = random.run(iterations, district)
    save_solution.save(f"random_experiment/district_{district.district}_iterations_{iterations}.json", optimal_model)

    histogram.plotting_histogram(costs, "Total costs", "Frequency", f"Histogram Greedy + random ({iterations})")
    plt.savefig(f"code/experiments/random_experiment/histogram_district_{district.district}_iterations_{iterations}")

    scatterplot.show_scatterplot(optimal_model, multiple_plots = False)
    plt.savefig(f"code/experiments/random_experiment/grid_district_{district.district}_iterations_{iterations}")

    save_solution.save(f"random_experiment/baseline_district_{district.district}_iterations__{iterations}")
