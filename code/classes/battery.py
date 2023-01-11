


class Battery(object):
    def __init__(self, x_position, y_position, capacity):
        self.x_position = x_position
        self.y_position = y_position
        self.capacity = capacity
        self.houses_connected = {}

    def has_capacity(self):
        return self.capacity
