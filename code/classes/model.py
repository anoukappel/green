

class Model(object):
    def __init__(self, district):
        self.district = district
        self.solution = {house: None for house in self.district.houses}
        self.cables = []
        self.battery_cable = {}


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
        battery = house.get_closest_battery(batteries)
        # list = []
        # for item in batteries:
        #     list.append([item.x_position, item.y_position])

        # position = house.get_closest_battery_or_cable(batteries)
        """
        check if position is of battery and connect it
        """
        # if position in self.get_battery_positions():
        # for battery in self.district.batteries:
        #     if battery.x_position == position[0] and battery.y_position == position[1]:
        #         battery.reduce_capacity(house)
        #         self.add_route_from_house_to_battery(battery, house)
        #         self.solution[house] = battery
        #         # print("test")


        """ battery is None when it was not possible to connect the house to a battery """
        if battery is not None:
            battery.reduce_capacity(house)
            # house.get_closest_battery(batteries)
            self.add_route_from_house_to_battery(battery, house)
        self.solution[house] = battery


    def get_battery_positions(self):
        """
        Returns a list of available batteries
        """
        list = []
        for item in self.district.batteries:
            list.append([item.x_position, item.y_position])
        return list



    def get_total_costs(self):
        """
        Returns total costs
        """
        if self.is_solution:
            return len(self.cables) * 9 + len(self.district.batteries) * 5000

    def add_cable(self, x_position, y_position, battery):
        """ add postition of cable to the object House"""
        self.cables.append([x_position,y_position])
        self.connect_battery_to_cable(x_position, y_position, battery)


    def connect_battery_to_cable(self, x_position, y_position, battery):
        """
        add connection between cable and battery
        """
        if self.battery_cable.get(battery) is not None:
            list = self.battery_cable[battery]
            list.append([x_position, y_position])
            self.battery_cable[battery] = list
        else:
            self.battery_cable[battery] = [x_position,y_position]


    def add_horizontal_steps(self, battery, house):
        """ adding the horizontal steps towards the battery """
        list = []
        if house.x_position < battery.x_position:
            steps = battery.x_position - house.x_position
            for i in range(steps + 1):
                self.add_cable(house.x_position+i, house.y_position, battery)
                list.append([house.x_position+i, house.y_position])
        else:
            steps = house.x_position - battery.x_position
            for i in range(steps + 1):
                self.add_cable(house.x_position-i, house.y_position, battery)
                list.append([house.x_position-i, house.y_position])
        return list


    def add_vertical_steps(self, battery, house):
        """ adding the vertical steps towards the battery, from postition of latest cable """
        if house.y_position < battery.y_position:
            steps = battery.y_position - house.y_position
            for i in range(steps):
                self.add_cable(battery.x_position, house.y_position + i + 1, battery)
        else:
            steps = house.y_position - battery.y_position
            for i in range(steps):
                self.add_cable(battery.x_position, house.y_position - i - 1, battery)


    def add_route_from_house_to_battery(self, battery, house):
        """ add route of cables needed to go from house to battery """
        self.add_horizontal_steps(battery, house)
        self.add_vertical_steps(battery, house)
