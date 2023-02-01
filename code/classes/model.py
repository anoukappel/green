import copy
import operator as op
from code.classes.district import District
from code.classes.battery import Battery
from code.classes.house import House
from typing import Any, Union, Optional, Dict

class Model(object):
    def __init__(self, district: District):
        self.district = district
        self.solution = {house: None for house in self.district.houses}
        self.cables = []
        self.battery_cable = self.fill_battery_cable()
        self.battery_positions = self.fill_battery_positions()
        self.battery_capacity = self.fill_battery_capacity()
        self.positive_capacities = True


    def fill_battery_capacity(self) -> Dict[Battery, int]:
        """
        Loads the initial battery capacities into the Model.
        """
        capacities = {}
        for battery in self.district.batteries:
            capacities[battery] = battery.capacity
        return capacities


    def fill_battery_cable(self) -> Dict[Battery, list[list[int, int]]]:
        """
        Loads the battery position as cable into the Model.
        """
        batteries_cable = {}
        for battery in self.district.batteries:
            batteries_cable[battery] = [[[battery.x_position, battery.y_position]]]
        return batteries_cable


    def fill_battery_positions(self) -> Dict[Battery, list[list[int, int]]]:
        """
        Loads the battery position into the Model.
        """
        battery_positions = {}
        for battery in self.district.batteries:
            list = []
            list.append([battery.x_position, battery.y_position])
            battery_positions[battery] = list
        return battery_positions


    def return_total_costs(self) -> int:
        """
        Returns the total costs of batteries and cables.
        """
        battery_costs = 5000 * len(self.district.batteries)
        cable_costs = 0
        for battery in self.district.batteries:
            [cable_costs := cable_costs + len(x) - 1 for x in self.battery_cable[battery]]
        cable_costs = cable_costs * 9
        return cable_costs + battery_costs


    def reduce_capacity(self, battery: Battery, house: House)-> None:
        """
        Reduce a batteries capacity with the given maxoutput of the house, also checks if
        a battery's capacity becomes negative.
        """
        self.battery_capacity[battery] = self.battery_capacity[battery] - house.maxoutput
        if self.battery_capacity[battery] < 0:
            self.positive_capacities = False


    def increase_capacity(self, battery: Battery, house: House):
        """
        Increases the battery capacity with the max output of the house.
        """
        self.battery_capacity[battery] = self.battery_capacity[battery] + house.maxoutput


    def return_a_house_given_a_position(self, position: list[int]) -> Union[bool, House]:
        """
        Returns the house object on a given position or returns False if there is no
        house on this position.
        """
        for house in self.district.houses:
            if position[0] == house.x_position and position[1] == house.y_position:
                return house
        return False


    def is_solution(self) -> bool:
        """
        Returns True if every house is connected to a battery.
        """
        for house in self.district.houses:
            if not self.has_connection(house):
                return False

        return self.positive_capacities


    def has_connection(self, house: House) -> bool:
        """
        Returns whether the house has an assigned battery.
        """
        return self.solution[house] is not None


    def set_connection(self, house: House, houses: list[House]) -> None:
        """
        Set the connection between house and battery.
        """
        if self.get_available_batteries(house) != []:
            list_grids, list_batteries = self.get_available_batteries(house)
            position = house.get_closest_battery_or_cable(list_grids)

            battery = None
            for key in list_batteries:
                for list in self.battery_cable[key]:
                    for item in list:
                        if item == position:
                            battery = key
                            break

            # battery is None when it was not possible to connect the house to a battery
            if battery is not None:
                self.reduce_capacity(battery, house)
                house_position = [house.x_position, house.y_position]
                self.add_route_from_house_to_battery(battery, house_position, position)
            self.solution[house] = battery


    def set_connection_given_battery(self, house: House, battery: Battery) -> None:
        """
        Sets the connection between house and battery.
        """
        position = house.get_closest_battery_or_cable(self.battery_positions[battery])
        self.reduce_capacity(battery, house)
        house_position = [house.x_position, house.y_position]
        self.add_route_from_house_to_battery(battery, house_position, position)
        self.solution[house] = battery


    def set_connection_block_given_battery(self, house: House, position: list[int], list_batteries: list[Battery]) -> bool:
        """
        Sets the connection between block and a given battery.
        """
        battery = None
        for key in list_batteries:
            for list in self.battery_cable[key]:
                for item in list:
                    if item == position:
                        battery = key
                        return False
                        break

        if self.check_capacity(house, battery) == False:
            return False

        # battery is None when it was not possible to connect the house to a battery
        elif battery is not None:
            self.reduce_capacity(battery, house)
            house_position = [house.x_position, house.y_position]
            self.add_route_from_house_to_battery(battery, house_position, position)
            self.solution[house] = battery
            return True
        return False


    def get_closest_position(self, house: House) -> tuple[list[int], list[Battery]]:
        """
        Finds the closest position of a cable or battery where this house can be connected to,
        returns this position and a list of available batteries.
        """
        if self.get_available_batteries(house) != []:
            list_grids, list_batteries = self.get_available_batteries(house)
            position = house.get_closest_battery_or_cable(list_grids)
            return position, list_batteries


    def get_distance(self, house: House, position: list[int]) -> int:
        """
        Returns the distance between the house and a given position.
        """
        distance = house.get_distance_to_battery_or_cable(position[0], position[1])
        return distance


    def check_capacity(self, house: House, battery: Battery) -> bool:
        """
        Returns True if the max capacity of the house is less than the available
        capacity of the given battery.
        """
        if self.battery_capacity[battery] > house.maxoutput:
            return True
        return False


    def get_available_batteries(self, house: House) -> tuple[list[list[int]], list[Battery]]:
        """
        Returns gridpoints batteries and cables that are available.
        """
        list_grids = []
        list_batteries = []
        for battery in self.district.batteries:
            if self.battery_capacity[battery] > house.maxoutput:
                list_batteries.append(battery)
                for item in self.battery_positions[battery]:
                    list_grids.append(item)
        return list_grids, list_batteries


    def add_cable(self, x_position: int, y_position: int) -> None:
        """
        Add postition of cable to the object House.
        """
        self.cables.append([x_position,y_position])


    def connect_battery_to_cable(self, battery: Battery, route: list[list[int]]) -> None:
        """
        Add route between cable and battery.
        """
        self.battery_cable[battery].append(route)


    def add_horizontal_steps(self, position: list[int], house_position: list[int], route: list[list[int]], battery: Battery) -> list[list[int]]:
        """
        Adding the horizontal steps towards the battery.
        """
        if house_position[0] < position[0]:
            steps = position[0] - house_position[0]
            for i in range(steps + 1):
                self.add_cable(house_position[0] + i, house_position[1])
                route.append([house_position[0] + i, house_position[1]])
                self.battery_positions[battery].append([house_position[0] + i, house_position[1]])
        else:
            steps = house_position[0] - position[0]
            for i in range(steps + 1):
                self.add_cable(house_position[0] - i, house_position[1])
                route.append([house_position[0] - i, house_position[1]])
                self.battery_positions[battery].append([house_position[0] - i, house_position[1]])
        return route


    def add_vertical_steps(self, position: list[int], house_position: list[int], route: list[list[int]], battery: Battery) -> list[list[int]]:
        """
        Adding the vertical steps towards the battery, from postition of latest cable.
        """
        if house_position[1] < position[1]:
            steps = position[1] - house_position[1]
            for i in range(steps):
                self.add_cable(position[0], house_position[1] + i + 1)
                route.append([position[0], house_position[1] + i + 1])
                self.battery_positions[battery].append([position[0], house_position[1] + i + 1])
        else:
            steps = house_position[1] - position[1]
            for i in range(steps):
                self.add_cable(position[0], house_position[1] - i - 1)
                route.append([position[0], house_position[1] - i - 1])
                self.battery_positions[battery].append([position[0], house_position[1] - i - 1])
        return route


    def remove_duplicates(self) -> int:
        """
        Removes duplicates in self.battery_positions.
        """
        for key in self.battery_positions:
            duplicates = self.battery_positions[key]
            tpls = [tuple(x) for x in duplicates]
            set1 = set(tpls)
            dup_free = [list(x) for x in set1]
            dup_free.sort()
            self.battery_positions[key] = dup_free


    def add_route_from_house_to_battery(self, battery: Battery, house_position: list[int], position: list[int]):
        """
        Add route of cables needed to go from house to battery.
        """
        route = []
        route = self.add_horizontal_steps(position, house_position, route, battery)
        route_with_coordinates = self.add_vertical_steps(position, house_position, route, battery)
        self.remove_duplicates()
        self.connect_battery_to_cable(battery, route_with_coordinates)


    def copy(self) -> Any:
        """
        Copies a model from itself.
        """
        new_model = copy.copy(self)
        new_model.solution = copy.copy(self.solution)
        return new_model
