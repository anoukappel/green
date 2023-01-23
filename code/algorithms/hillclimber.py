# import copy
import random

from .random import random_assignment
from code.classes.model import Model

class HillClimber:
    """
    The HillClimber class switches the connected battery of two random houses.
    If this change is an improvement and still valid, than the solution is saved.
    """
    def __init__(self, model):
        if not model.is_solution():
            raise Exception("Please provide a complete solution.")

        self.model = model.copy()
        self.new_model = None

    def returns_house_to_switch(self, house, battery, new_model):
        ### bereken capaciteit beschikbaar wanneer house is verwijdert
        available_capacity = new_model.battery_capacity[battery] + house.maxoutput
        ### huizen die hieraan verbonden kunnen worden
        houses_to_switch = []
        for item in new_model.district.houses:
            ## check if this house can be connected
            if item.maxoutput <= available_capacity and new_model.solution[item] != battery:
                ## check of other house can be connected to this battery
                possible_battery = new_model.solution[item]
                if new_model.battery_capacity[possible_battery] + item.maxoutput > house.maxoutput:
                    houses_to_switch.append(item)
        if len(houses_to_switch) != 0:
            return random.choice(houses_to_switch)
        else:
            return False

    def switch_random_house_and_battery_in_solution(self, new_model):
        """ picks a random house from a random battery """
        battery = new_model.district.batteries[random.randint(0, 4)]
        ## find random house given this battery
        index = len(new_model.battery_cable[battery])
        index = random.randint(1, index - 1)
        route = new_model.battery_cable[battery][index]
        house = new_model.return_a_house_given_a_position(route[0])

        ## find an other random house from other battery to switch
        if self.returns_house_to_switch(house, battery, new_model) is not False:
            house_switch = self.returns_house_to_switch(house, battery, new_model)
            battery_switch = new_model.solution[house_switch]

            ## switch both batterys in solution
            new_model.solution[house] = battery_switch
            new_model.solution[house_switch] = battery

            new_sol = new_model.solution

            self.fill_solution(new_sol, new_model)


    def fill_solution(self, new_sol, new_model):
        new_model = Model(new_model.district)
        for house in new_model.district.houses:
            new_model.set_connection_given_battery(house, new_sol[house])

        self.new_model = new_model


    def check_solution(self, new_model):
        """
        Check if new solution is an improvement.
        """
        new_value = len(self.new_model.cables)
        old_value = len(self.model.cables)
        if new_model.is_solution():
            if new_value < old_value:
                print("the model is improved")
                self.model = self.new_model


    def run_hillclimber(self, iterations, number_of_switch):
        """
        Runs the hillclimber algorithm for a number of iterations,
        each time switching one house.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            new_model = self.model.copy()
            for i in range(number_of_switch):
                self.switch_random_house_and_battery_in_solution(new_model)
            self.check_solution(new_model)