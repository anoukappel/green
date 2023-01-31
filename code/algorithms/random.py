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

    costs = []
    first_loop = True
    while (len(costs) != amount_valid_solutions):
        model_test = Model(district_test)
        solution = random_assignment(model_test)

        sum = solution.return_total_costs()

        if solution.is_solution() is False:
            continue

        if solution.is_solution() is not False:
            costs.append(sum)

        if first_loop:
            smallest_solution = solution

        if sum < smallest_solution.return_total_costs():
            smallest_solution = solution

        first_loop = False
    return smallest_solution, costs
