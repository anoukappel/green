

class House(object):
    def __init__(self, x_position, y_position, maxoutput):
        self.x_position = x_position
        self.y_position = y_position
        self.maxoutput = capacity
        self.houses_connected = {}
        self.connected = False
        self.connected_battery = None

    def is_connected(self):
        return self.connected

    def set_connected(self, battery):
        self.connected_battery = battery
