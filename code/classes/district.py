from .battery import Battery
from .house import House
import csv

class District(object):
    def __init__(self, source_file: str, district: str, geo_json = None) -> None:
        self.houses = self.load_houses(f"{source_file}/district-{district}_houses.csv")
        self.batteries = self.load_batteries(f"{source_file}/district-{district}_batteries.csv")
        self.district = int(source_file[-1])


    def load_houses(self, houses_file: str) -> list[House]:
        """
        Load all the houses in District.
        """
        houses = []

        with open(houses_file, 'r') as file:
            header = file.readline()
            houses = []
            for line in file:
                splits = line.split(',')
                houses.append(House(int(splits[0]), int(splits[1]), float(splits[2])))
        return houses


    def load_batteries(self, battery_file:str) -> list[Battery]:
        """
        Load all the batteries in District.
        """
        batteries = []
        with open(battery_file, 'r') as file:
            header = file.readline()
            houses = []
            for line in file:
                line = line.replace('"', '')
                splits = line.split(',')
                batteries.append(Battery(int(splits[0]), int(splits[1]), float(splits[2])))
        return batteries
