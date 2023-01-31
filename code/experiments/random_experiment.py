from code.algorithms import random
import matplotlib.pyplot as plt
import copy
import csv
from code.solutions import save_solution
from code.classes import model
from code.visualisatie import histogram

def baseline(district):
    """ model is a correct solution """
    results = []
    correct_models = []
    random_solution = model.Model(district)
    while random_solution.is_solution() is False:
        random_model = model.Model(district)
        random_solution = random.random_assignment(random_model)

    results.append(random_solution.return_total_costs())
    correct_models.append(random_solution.is_solution())
    counter = 0
    number_of_solutions = 1
    best_model = random_solution
    while counter < number_of_solutions:
        # print(i)
        random_model = model.Model(district)
        random_solution = random.random_assignment(random_model)
        if random_solution.is_solution() is True:
            counter += 1
            results.append(random_solution.return_total_costs())
            correct_models.append(random_solution.is_solution())
            if best_model.return_total_costs() > random_model.return_total_costs():
                best_model = random_model
    return best_model, results


def save_histogram(district):
    model, costs = baseline(district)
    histogram.plotting_histogram(costs)
    # plt.savefig('histogram.png')
    # print(best_model.return_total_costs())
        # print(random_solution.is_solution())





    # save_solution.save("random", best_model)
    # print(results)
    # print(test)

        #     model_test = model.Model(district_test)
        #     for i in range(1):
        #         while model_test.is_solution() is False:
        #             model_2 = model.Model(district_test)
        #             model_test = random.random_assignment(model_2)

    # with open("results/random/baseline.csv",'w', newline='') as output_file:
    #     result_writer = csv.writer(output_file, delimiter=',')
    #     for result in results:
    #         result_writer.writerow(result)
