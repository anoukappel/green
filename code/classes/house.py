from typing import Tuple, Optional

class House(object):
    def __init__(self, x_position: int, y_position: int, maxoutput: float) -> None:
        """
        Initializes a House object with a x and y coordinate (position on the grid).
        It also initializes the maximal output of a house.
        """
        self.x_position = x_position
        self.y_position = y_position
        self.maxoutput = maxoutput


    def get_distance_to_battery_or_cable(self, x_position: int, y_position: int) -> int:
        """
        Calculates manhatten distance between house position and given x and y.
        Returns this distance.
        """
        distance = abs(self.x_position - x_position) + abs(self.y_position - y_position)
        return distance


    def get_closest_battery_or_cable(self, list: list[Tuple[int, int]]) -> Optional[Tuple[int, int]]:
        """
        Input is a list of all coordinates which are connected to batteries which have enough
        capacity to connect the house with.
        Returns de position [x, y] as a list which is closest to the house position.
        """
        standard = 10000
        position = None
        for item in list:
            if self.get_distance_to_battery_or_cable(item[0], item[1]) < standard:
                position = item
                standard = self.get_distance_to_battery_or_cable(item[0],item[1])
        return position


    def __repr__(self) -> str:
        """
        Let the object be printed properly when its called for.
        """
        return f"Postition house: ({self.x_position},{self.y_position}), maxoutput: {self.maxoutput}"
