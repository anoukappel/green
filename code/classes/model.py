import itertools

class Model(object):
    def __init__(self, district):
        self.district = district
        self.solution = {house: None for house in self.district.houses}
        self.cables = []
        """
        key is battery and value is a list of lists for every cable route.
        startpoint of list in list is position of house
        """
        self.battery_cable = {}
        self.set_with_positions = {}

    def fill_battery_cable(self):
        for battery in self.district.batteries:
            self.battery_cable[battery] = [[[battery.x_position, battery.y_position]]]

    def fill_set_with_positions(self):
        for battery in self.district.batteries:
            list = []
            list.append([battery.x_position, battery.y_position])
            self.set_with_positions[battery] = list


    def is_solution(self):
        """
        Returns True if every house is connected to a battery.
        """
        for house in self.district.houses:
            if not self.has_connection(house):
                return False
        return True


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

            position = house.get_closest_battery_or_cable(self.get_available_batteries(house))

            battery = None
            for key in self.battery_cable:
                for list in self.battery_cable[key]:
                    for item in list:
                        if item == position:
                            battery = key
                            break

            """ battery is None when it was not possible to connect the house to a battery """
            if battery is not None:
                battery.reduce_capacity(house)
                self.add_route_from_house_to_battery(battery, house, position)
            self.solution[house] = battery
            # print(self.set_with_positions)


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
        list = []
        for battery in self.district.batteries:
            if battery.capacity > house.maxoutput:
                for item in self.set_with_positions[battery]:
                    list.append(item)
        return list


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
                self.set_with_positions[battery].append([house.x_position+i, house.y_position])
        else:
            steps = house.x_position - position[0]
            for i in range(steps + 1):
                self.add_cable(house.x_position-i, house.y_position)
                list.append([house.x_position-i, house.y_position])
                self.set_with_positions[battery].append([house.x_position-i, house.y_position])
        return list


    def add_vertical_steps(self, position, house, list, battery):
        """ adding the vertical steps towards the battery, from postition of latest cable """
        if house.y_position < position[1]:
            steps = position[1] - house.y_position
            for i in range(steps):
                self.add_cable(position[0], house.y_position + i + 1)
                list.append([position[0], house.y_position + i + 1])
                self.set_with_positions[battery].append([position[0], house.y_position + i + 1])
        else:
            steps = house.y_position - position[1]
            for i in range(steps):
                self.add_cable(position[0], house.y_position - i - 1)
                list.append([position[0], house.y_position - i - 1])
                self.set_with_positions[battery].append([position[0], house.y_position - i - 1])
        return list


    def remove_duplicates(self):
        for key in self.set_with_positions:
            duplicates = self.set_with_positions[key]
            tpls = [tuple(x) for x in duplicates]
            set1 = set(tpls)
            # dct = list(dict.fromkeys(tpls))
            dup_free = [list(x) for x in set1]
            dup_free.sort()
            self.set_with_positions[key] = dup_free
            print(dup_free)

    def add_route_from_house_to_battery(self, battery, house, position):
        """ add route of cables needed to go from house to battery """
        list = self.add_horizontal_steps(position, house, battery)
        list_with_coordinates = self.add_vertical_steps(position, house, list, battery)
        self.remove_duplicates()
        self.connect_battery_to_cable(battery, list_with_coordinates)
