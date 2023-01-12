# from .district import District
# from .battery import Battery
# from math import abs

class House(object):
    def __init__(self, x_position, y_position, maxoutput):
        self.x_position = x_position
        self.y_position = y_position
        self.maxoutput = maxoutput
        # self.houses_connected = {}
        self.connected = False
        self.connected_battery = None
        self.cables = []

    def is_connected(self):
        return self.connected

    def set_connected(self, battery):
        self.connected_battery = battery
        self.connected = True

    def get_distance_to_battery(self, battery):
        distance = abs(self.x_position - battery.x_position) + abs(self.y_position - battery.y_position)
        return distance

    def get_closest_battery(self, batteries):
        """ returnes battery which is closest to the house """
        standard = 10000
        battery = 0
        for item in batteries:
            if self.get_distance_to_battery(item) < standard and (item.capacity - self.maxoutput) > 0:
                battery = item
                standard = self.get_distance_to_battery(item)
        battery.reduce_capacity(self)
        return battery

    def add_cable(self, x_position, y_position):
        """ add postition of cable to the object House"""
        # self.cables.append(f"{x_position},{y_position}")
        self.cables.append([x_position,y_position])


    def add_horizontal_steps(self, battery):
        """ adding the horizontal steps towards the battery """
        if self.x_position < battery.x_position:
            steps = battery.x_position - self.x_position
            for i in range(steps + 1):
                self.add_cable(self.x_position+i, self.y_position)
        else:
            steps = self.x_position - battery.x_position
            for i in range(steps + 1):
                self.add_cable(self.x_position-i, self.y_position)


    def add_vertical_steps(self, battery):
        """ adding the vertical steps towards the battery, from postition of latest cable """
        if self.y_position < battery.y_position:
            steps = battery.y_position - self.y_position
            for i in range(steps):
                self.add_cable(battery.x_position, self.y_position + i + 1)
        else:
            steps = self.y_position - battery.y_position
            for i in range(steps):
                self.add_cable(battery.x_position, self.y_position - i - 1)


    def add_route_from_house_to_battery(self, battery):
        """ add route of cables needed to go from house to battery """
        self.add_horizontal_steps(battery)
        self.add_vertical_steps(battery)
