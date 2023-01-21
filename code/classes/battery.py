


class Battery(object):
    def __init__(self, x_position, y_position, capacity):
        self.x_position = x_position
        self.y_position = y_position
        self.capacity = capacity
        # self.color = color

    def has_capacity(self):
        return self.capacity

    def reduce_capacity(self, house):
        self.capacity = self.capacity - house.maxoutput

    def __repr__(self):
        """ Let the object be printed properly when its called for """
        return f"Position battery: ({self.x_position}, {self.y_position}), available capacity: {self.capacity}"
