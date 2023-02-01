from code.classes.house import House


class Battery(object):
    def __init__(self, x_position: int, y_position: int, capacity: float) -> None:
        self.x_position = x_position
        self.y_position = y_position
        self.capacity = capacity


    def has_capacity(self) -> float:
        return self.capacity

    # def reduce_capacity(self, house: House) -> None:
    #     self.capacity = self.capacity - house.maxoutput

    def __repr__(self) -> str:
        """ Let the object be printed properly when its called for """
        return f"Position battery: ({self.x_position}, {self.y_position}), available capacity: {self.capacity}"
