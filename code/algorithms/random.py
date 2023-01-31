from code.classes.model import Model
from code.classes.district import District
import random

def random_assignment(model):
    """
    Assign (randomly) every house to a battery which is closest and available.
    """
    random.shuffle(model.district.houses)

    for house in model.district.houses:
        ## sets connection between house and closest battery with available capacity
        model.set_connection(house, model.district.batteries)

    return model

def run(amount_valid_solutions, district_test):

    list_cable_lengths = []
    first_loop = True
    while (len(list_cable_lengths) != amount_valid_solutions):
        model_test = Model(district_test)
        solution = random_assignment(model_test)

        sum = len(solution.cables)

        if solution.is_solution() is not False:
            list_cable_lengths.append(sum)

        if first_loop:
            smallest_solution = solution

        if sum < len(smallest_solution.cables):
            smallest_solution = solution

        first_loop = False
    return smallest_solution, list_cable_lengths
#
# def run_random_iterated(iterations, model):
#     model_sol = 400000
#     best_model = model
#     for i in range(iterations):
#         model_test = random_assignment(model)
#         while model_test.is_solution() is False:
#             model_2 = model.Model(district_test)
#             model_test = random.random_assignment(model_2)
#         if model_test.return_total_costs() < model_sol:
#             model_sol = model_test.return_total_costs()
#             best_model = model_test
#     return best_model
