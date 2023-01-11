from .battery import Battery
from .cable import Cable
from .house import House


class District(object):
    # def __init__(self, source_file, battery_file, houses_file):
    def __init__(self, houses_file):
        self.houses = self.load_houses(houses_file)
        # self.batteries = self.load_batteries(battery_file)
        # save the district number
        # self.district = int(source_file[-1])


    def load_houses(self, houses_file):
        """ load all the houses in District """
        houses = []
        #
        # with open(houses_file, 'r') as file:
        #     reader = csv.DictReader(file)

        with open(houses_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            for row in reader:
                houses.append(House(row['x'], row['y'], row['maxoutput']))

                return houses
