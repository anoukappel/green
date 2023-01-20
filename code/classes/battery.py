


class Battery(object):
    def __init__(self, x_position, y_position, capacity):
        self.x_position = x_position
        self.y_position = y_position
        self.capacity = capacity

    def has_capacity(self):
        return self.capacity

    def __repr__(self):
        """ Let the object be printed properly when its called for """
        return f"Position battery: ({self.x_position}, {self.y_position}), available capacity: {self.capacity}"
