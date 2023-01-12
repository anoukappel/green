

class Model(object):
    def __init__(self, district):
        self.houses = district.houses
        self.batteries = district.batteries
        self.connections = {}
        # self.house = house

    def save_connections(self):
        houses = []

        for house in self.houses:

        self.connected[battery] = house
