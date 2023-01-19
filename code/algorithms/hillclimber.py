import copy
import random

from .randomise import random_assignment
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
        self.value = model.get_total_costs()

    def switch_random_houses_from_battery(self):
        """
        Switch two houses from battery.
        """
        ### take two random batteries:
        random_batteries = random.sample(range(5), 2)

        ### get two houses from different batteries
            ## choose two random batteries
        batterij_1 = self.model.district.batteries[random_batteries[0]]
        batterij_2 = self.model.district.batteries[random_batteries[1]]
            ## cal number of routes (houses) connected to this battery
        index_1 = len(self.model.battery_cable[batterij_1])
        index_2 = len(self.model.battery_cable[batterij_2])
            ## get random index to select random house (so skip index 0)
        index_1 = random.randint(1, index_1)
        index_2 = random.randint(1, index_2)

        route_1 = self.model.battery_cable[batterij_1][index_1]
        route_2 = self.model.battery_cable[batterij_2][index_2]
            ## find the house objects related to these routes
        house_1 = self.model.return_a_house_given_a_position(route_1[0])
        house_2 = self.model.return_a_house_given_a_position(route_2[0])

        ### delete those routes from the list and from set.
        self.model.delete_a_route_from_house(index_1, batterij_1, route_1)
        self.model.delete_a_route_from_house(index_2, batterij_2, route_2)

        ### add battery capacity to battery where house is deleted from
        self.model.increase_capacity(batterij_1, house_1)
        self.model.increase_capacity(batterij_2, house_2)

        ### add the both houses to the other battery
        ## get the list of possible grids
        list_positions_1 = self.model.battery_positions[batterij_2]
        list_positions_2 = self.model.battery_positions[batterij_1]

        ### get closest position of other battery for both houses
        position_1 = house_1.get_closest_battery_or_cable(list_positions_1)
        position_2 = house_2.get_closest_battery_or_cable(list_positions_2)

        ### battery capacity reduction
        self.model.reduce_capacity(batterij_1, house_2)
        self.model.reduce_capacity(batterij_2, house_1)


        ## add other routes to
        self.model.add_route_from_house_to_battery(batterij_2, house_1, position_1)
        self.model.add_route_from_house_to_battery(batterij_1, house_2, position_2)

        # add to solution
        self.model.solution[house_1] = batterij_2
        self.model.solution[house_2] = batterij_1
         # position = house_1.get_closest_battery_or_cable(set_with_positions[batterij_2])

    def check_solution(self, new_model):
        """
        Check if new solution is an improvement.
        """
        new_value = new_model.get_total_costs()
        old_value = self.value
        if new_model.is_solution()
            if new_value <= old_value:
                self.model = new_model
                self.value = new_value

    def run_hillclimber(self, iterations):
        """
        Runs the hillclimber algorithm for a number of iterations,
        each time switching one house.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            new_model = self.model.copy()

            self.switch_random_houses_from_battery()

            self.check_solution(new_model)
            print(self.value)
