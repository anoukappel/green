# from .district import District
# from .battery import Battery
# from math import abs

class House(object):
    def __init__(self, x_position, y_position, maxoutput):
        self.x_position = x_position
        self.y_position = y_position
        self.maxoutput = maxoutput
        self.houses_connected = {}
        self.connected = False
        self.connected_battery = None
        self.cables = []

    def is_connected(self):
        return self.connected

    def set_connected(self, battery):
        self.connected_battery = battery
        self.connected = True

    def add_cable(self, x_position, y_position):
        self.cable.append([x_position, y_position])

    def get_distance_to_battery(self, battery):
        distance = abs(self.x_position - battery.x_position) + abs(self.y_position - battery.y_position)
        return distance

    def get_closest_battery(self, batteries):
        standard = 10000
        battery = 0
        for item in batteries:
            if self.get_distance_to_battery(item) < standard:
                battery = item
        return battery
