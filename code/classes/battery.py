

class Battery(object):
    def __init__(self, x_position: int, y_position: int, capacity: float) -> None:
        self.x_position = x_position
        self.y_position = y_position
        self.capacity = capacity


    def has_capacity(self) -> float:
        """
        Returns the capacity of a battery.
        """
        return self.capacity


    def __repr__(self) -> str:
        """
        Let the object be printed properly when its called for
        """
        return f"Position battery: ({self.x_position}, {self.y_position}), available capacity: {self.capacity}"
