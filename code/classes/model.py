

class Model(object):
    def __init__(self, district):
        self.houses = district.houses
        self.batteries = district.batteries
        self.solution = {house: None for house in self.houses}
        self.district = district


    def is_solution(self):
        """
        Returns True if every house is connected to a battery.
        """
        for house in self.houses:
            if not self.has_connection(house):
                return False
        return True


    def get_houses(self):
        """
        Return the list of houses available in the model.
        """
        return list(self.solutions.keys())


    def has_connection(self, house):
        """
        Returns whether the house has an assigned battery.
        """
        return self.solution[house] is not None


    def set_connection(self, house, batteries):
        """
        Set the connection between house and battery.
        """
        battery = house.get_closest_battery(batteries)
        """ battery is None when it was not possible to connect the house to a battery """
        if battery is not None:
            battery.reduce_capacity(house)
            # house.get_closest_battery(batteries)
            house.add_route_from_house_to_battery(battery)
        self.solution[house] = battery


    def get_batteries(self):
        """
        Returns a list of available batteries
        """
        return self.batteries
