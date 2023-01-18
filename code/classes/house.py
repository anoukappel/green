


class House(object):
    def __init__(self, x_position, y_position, maxoutput):
        self.x_position = x_position
        self.y_position = y_position
        self.maxoutput = maxoutput


    # def get_distance_to_battery(self, battery):cd
    #     distance = abs(self.x_position - battery.x_position) + abs(self.y_position - battery.y_position)
    #     return distance

    def get_distance_to_battery_or_cable(self, x_position, y_position):
        """
        Calculates manhatten distance between house position and given x and y.
        Returns this distance.
        """
        distance = abs(self.x_position - x_position) + abs(self.y_position - y_position)
        return distance

    def get_closest_battery_or_cable(self, list):
        """
        Input is a list of all coordinates which are connected to batteries which have enough
        capacity to connect the house with.
        Returns de position [x, y] as a list which is closest to the house position.
        """
        standard = 10000
        position = None
        for item in list:
            if self.get_distance_to_battery_or_cable(item[0][0], item[0][1]) < standard:
                position = item
                standard = self.get_distance_to_battery_or_cable(item[0][0],item[0][1])
        return position


    # def get_closest_battery(self, batteries):
    #     """ returnes battery which is closest to the house """
    #     standard = 10000
    #     battery = None
    #     for item in batteries:
    #         if self.get_distance_to_battery(item) < standard and (item.capacity - self.maxoutput) > 0:
    #             battery = item
    #             standard = self.get_distance_to_battery(item)
    #             self.distance_to_battery = standard
    #     return battery



    def __repr__(self):
        """ Let the object be printed properly when its called for """
        return f"Postition house: ({self.x_position},{self.y_position}), maxoutput: {self.maxoutput}"
