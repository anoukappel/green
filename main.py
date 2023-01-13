from code.classes import battery, district, house, model
from code.algorithms import random

if __name__ == "__main__":
    """ creation of district object """
    file = "data/Huizen&Batterijen/district_1"
    district_test = district.District(file)

    """ Random assignment of house to battery, when solution invalid run again. """
    model_test = model.Model(district_test)
    solution = random.random_assignment(model_test)
    while solution.is_solution() is False:
        test = district.District(file)
        model_2 = model.Model(test)
        solution = random.random_assignment(model_2)

    print(f"Every house had a connection to a battery: {solution.is_solution()}")

    sum = 0
    for house in solution.houses:
        sum += house.distance_to_battery

    print(f"Total number of cables needed: {sum}")
