import copy
import operator as op

class Model(object):
    def __init__(self, district):
        self.district = district
        self.solution = {house: None for house in self.district.houses}
        self.cables = []
        self.battery_cable = self.fill_battery_cable()
        self.battery_positions = self.fill_battery_positions()
        self.battery_capacity = self.fill_battery_capacity()
        self.positive_capacities = True

    def return_total_costs(self):
        """ returns the total costs of batteries and cables """
        battery_costs = 5000 * len(self.district.batteries)
        cable_costs = 0
        for battery in self.district.batteries:
            [cable_costs := cable_costs + len(x) - 1 for x in self.battery_cable[battery]]
        cable_costs = cable_costs * 9
        return cable_costs + battery_costs


    def fill_battery_capacity(self):
        capacities = {}
        for battery in self.district.batteries:
            capacities[battery] = battery.capacity
        return capacities

    def fill_battery_cable(self):
        batteries_cable = {}
        for battery in self.district.batteries:
            batteries_cable[battery] = [[[battery.x_position, battery.y_position]]]
        return batteries_cable

    def fill_battery_positions(self):
        battery_positions = {}
        for battery in self.district.batteries:
            list = []
            list.append([battery.x_position, battery.y_position])
            battery_positions[battery] = list
        return battery_positions


    def reduce_capacity(self, battery, house):
        """
        Reduce a batteries capacity with the given maxoutput of the house, also checks if
        a battery's capacity becomes negative.
        """
        self.battery_capacity[battery] = self.battery_capacity[battery] - house.maxoutput
        if self.battery_capacity[battery] < 0:
            self.positive_capacities = False

    def increase_capacity(self, battery, house):
        self.battery_capacity[battery] = self.battery_capacity[battery] + house.maxoutput

    def return_a_house_given_a_position(self, position: list[int]):
        for house in self.district.houses:
            if position[0] == house.x_position and position[1] == house.y_position:
                return house
        return False


    def is_solution(self):
        """
        Returns True if every house is connected to a battery.
        """
        for house in self.district.houses:
            if not self.has_connection(house):
                return False

        return self.positive_capacities


    # def get_houses(self):
    #     """
    #     Return the list of houses available in the model.
    #     """
    #     return list(self.solutions.keys())


    def has_connection(self, house):
        """
        Returns whether the house has an assigned battery.
        """
        return self.solution[house] is not None


    def set_connection(self, house, batteries):
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

    def set_connection_given_battery(self, house, battery):
        """
        Sets the connection between house and battery.
        """
        position = house.get_closest_battery_or_cable(self.battery_positions[battery])
        self.reduce_capacity(battery, house)
        house_position = [house.x_position, house.y_position]
        self.add_route_from_house_to_battery(battery, house_position, position)
        self.solution[house] = battery

    def set_connection_block_given_battery(self, house, position, list_batteries):
        """
        Sets the connection between block and a given battery.
        """
        battery = None
        for key in list_batteries:
            for list in self.battery_cable[key]:
                for item in list:
                    if item == position:
                        battery = key
                        break

        if self.check_capacity(house, battery) == False:
            return False

        elif battery is not None:
            self.reduce_capacity(battery, house)
            house_position = [house.x_position, house.y_position]
            self.add_route_from_house_to_battery(battery, house_position, position)
            self.solution[house] = battery
            return True


    def get_closest_position(self, house):
        if self.get_available_batteries(house) != []:
            list_grids, list_batteries = self.get_available_batteries(house)
            position = house.get_closest_battery_or_cable(list_grids)
            return position, list_batteries

    def get_distance(self, house, position):
        distance = house.get_distance_to_battery_or_cable(position[0], position[1])
        return distance

    def check_capacity(self, house, battery):
        check = False
        if self.battery_capacity[battery] > house.maxoutput:
            check = True
        return check

    def get_battery_positions(self):
        """
        Returns a list of available batteries
        """
        list = []
        for item in self.district.batteries:
            list.append([item.x_position, item.y_position])
        return list


    def get_available_batteries(self, house):
        """ returns gridpoints batteries and cables that are available """
        list_grids = []
        list_batteries = []
        for battery in self.district.batteries:
            if self.battery_capacity[battery] > house.maxoutput:
                list_batteries.append(battery)
                for item in self.battery_positions[battery]:
                    list_grids.append(item)
        return list_grids, list_batteries


    def add_cable(self, x_position, y_position):
        """
        add postition of cable to the object House
        """
        self.cables.append([x_position,y_position])



    def connect_battery_to_cable(self, battery, list):
        """
        add connection between cable and battery
        """
        self.battery_cable[battery].append(list)



    def add_horizontal_steps(self, position, house_position, list, battery):
        """
        Adding the horizontal steps towards the battery.
        """
        if house_position[0] < position[0]:
            steps = position[0] - house_position[0]
            for i in range(steps + 1):
                self.add_cable(house_position[0]+i, house_position[1])
                list.append([house_position[0]+i, house_position[1]])
                self.battery_positions[battery].append([house_position[0]+i, house_position[1]])
        else:
            steps = house_position[0] - position[0]
            for i in range(steps + 1):
                self.add_cable(house_position[0]-i, house_position[1])
                list.append([house_position[0]-i, house_position[1]])
                self.battery_positions[battery].append([house_position[0]-i, house_position[1]])
        return list


    def add_vertical_steps(self, position, house_position, list, battery):
        """
        Adding the vertical steps towards the battery, from postition of latest cable """
        if house_position[1] < position[1]:
            steps = position[1] - house_position[1]
            for i in range(steps):
                self.add_cable(position[0], house_position[1] + i + 1)
                list.append([position[0], house_position[1] + i + 1])
                self.battery_positions[battery].append([position[0], house_position[1] + i + 1])
        else:
            steps = house_position[1] - position[1]
            for i in range(steps):
                self.add_cable(position[0], house_position[1] - i - 1)
                list.append([position[0], house_position[1] - i - 1])
                self.battery_positions[battery].append([position[0], house_position[1] - i - 1])
        return list


    def remove_duplicates(self):
        """ removes duplicates in self.battery_positions """
        for key in self.battery_positions:
            duplicates = self.battery_positions[key]
            tpls = [tuple(x) for x in duplicates]
            set1 = set(tpls)
            dup_free = [list(x) for x in set1]
            dup_free.sort()
            self.battery_positions[key] = dup_free

    def add_route_from_house_to_battery(self, battery, house_position, position):
        """ add route of cables needed to go from house to battery """
        list = []
        list = self.add_horizontal_steps(position, house_position, list, battery)
        list_with_coordinates = self.add_vertical_steps(position, house_position, list, battery)
        self.remove_duplicates()
        self.connect_battery_to_cable(battery, list_with_coordinates)

    def copy(self):
        """
        Copies a model from itself.
        """
        new_model = copy.copy(self)
        new_model.solution = copy.copy(self.solution)
        return new_model
