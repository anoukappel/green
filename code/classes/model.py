import copy

class Model(object):
    def __init__(self, district):
        self.district = district
        self.solution = {house: None for house in self.district.houses}
        self.cables = []
        """
        key is battery and value is a list of lists for every cable route.
        startpoint of list in list is position of house
        """
        self.battery_cable = self.fill_battery_cable()
        self.battery_positions = self.fill_battery_positions()
        self.battery_capacity = self.fill_battery_capacity()
        self.positive_capacities = True

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
        self.battery_capacity[battery] = self.battery_capacity[battery] - house.maxoutput
        if self.battery_capacity[battery] < 0:
            # print("a battery is negative")
            self.positive_capacities = False

    def increase_capacity(self, battery, house):
        self.battery_capacity[battery] = self.battery_capacity[battery] + house.maxoutput

    def return_a_house_given_a_position(self, position):
        for house in self.district.houses:
            if position[0] == house.x_position and position[1] == house.y_position:
                return house
        return False

    def delete_a_route_from_house(self, index, battery, route):
        ### verwijder posities uit set_with_positions
        for item in route:
            self.battery_positions[battery].remove(item)
        ### verwijder route uit battery_cable
        self.battery_cable[battery].pop(index)


    def is_solution(self):
        """
        Returns True if every house is connected to a battery.
        """
        for house in self.district.houses:
            if not self.has_connection(house):
                return False
        # print(self.positive_capacities)
        # return self.positive_capacities
        return self.positive_capacities


    def get_houses(self):
        """
        Return the list of houses available in the model.
        """
        return list(self.solutions.keys())


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

            """ battery is None when it was not possible to connect the house to a battery """
            if battery is not None:
                self.reduce_capacity(battery, house)
                self.add_route_from_house_to_battery(battery, house, position)
            self.solution[house] = battery


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
            # print(battery.capacity)
            # if battery.capacity > house.maxoutput:
            if self.battery_capacity[battery] > house.maxoutput:
                list_batteries.append(battery)
                for item in self.battery_positions[battery]:
                    list_grids.append(item)
        return list_grids, list_batteries


    def get_total_costs(self):
        """
        Returns total costs
        """
        if self.is_solution:
            return len(self.cables) * 9 + len(self.district.batteries) * 5000

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



    def add_horizontal_steps(self, position, house, battery):
        """ adding the horizontal steps towards the battery """
        list = []
        if house.x_position < position[0]:
            steps = position[0] - house.x_position
            for i in range(steps + 1):
                self.add_cable(house.x_position+i, house.y_position)
                list.append([house.x_position+i, house.y_position])
                self.battery_positions[battery].append([house.x_position+i, house.y_position])
        else:
            steps = house.x_position - position[0]
            for i in range(steps + 1):
                self.add_cable(house.x_position-i, house.y_position)
                list.append([house.x_position-i, house.y_position])
                self.battery_positions[battery].append([house.x_position-i, house.y_position])
        return list


    def add_vertical_steps(self, position, house, list, battery):
        """ adding the vertical steps towards the battery, from postition of latest cable """
        if house.y_position < position[1]:
            steps = position[1] - house.y_position
            for i in range(steps):
                self.add_cable(position[0], house.y_position + i + 1)
                list.append([position[0], house.y_position + i + 1])
                self.battery_positions[battery].append([position[0], house.y_position + i + 1])
        else:
            steps = house.y_position - position[1]
            for i in range(steps):
                self.add_cable(position[0], house.y_position - i - 1)
                list.append([position[0], house.y_position - i - 1])
                self.battery_positions[battery].append([position[0], house.y_position - i - 1])
        return list


    def remove_duplicates(self):
        for key in self.battery_positions:
            duplicates = self.battery_positions[key]
            tpls = [tuple(x) for x in duplicates]
            set1 = set(tpls)
            # dct = list(dict.fromkeys(tpls))
            dup_free = [list(x) for x in set1]
            dup_free.sort()
            self.battery_positions[key] = dup_free
            # print(dup_free)

    def add_route_from_house_to_battery(self, battery, house, position):
        """ add route of cables needed to go from house to battery """
        list = self.add_horizontal_steps(position, house, battery)
        list_with_coordinates = self.add_vertical_steps(position, house, list, battery)
        self.remove_duplicates()
        self.connect_battery_to_cable(battery, list_with_coordinates)

    def copy(self):
        """
        Copies a model from itself.
        """
        new_model = copy.copy(self)
        new_model.solution = copy.copy(self.solution)
        return new_model
