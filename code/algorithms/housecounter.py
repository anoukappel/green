from code.classes.model import Model
from code.classes.district import District
import random

class Housecounter:
    """
    The Housecounter class counts the number of houses in each 10x10 grid block.
    It connects all the houses of a block to the closest battery.
    If a house can't connect it will go into a list. Which will be connected
    afterwards.
    The block with the most houses will be connected first and with the least
    houses last.
    """
    def __init__(self, model):
        self.model = model
        self.blocks = {}
        self.houses_left = []


    def make_blocks(self):
        """
        Makes 25 list in a dictionairy. With a number of a block as key.
        Block 0 is in the bottom left side and block 24 in the upper right side.
        """
        for i in range(25):
            self.blocks[i] = []


    def fill_blocks(self):
        """
        Fills the list in the dictionairy with houses present in that block.
        """
        self.make_blocks()
        # loop through all houses in the district
        for house in self.model.district.houses:
            for i in range(25):
                # if house is in this block, append house to this block
                if self.houses_in_block(house) == i:
                    self.blocks[i].append(house)


    def houses_in_block(self, house):
        """
        Checks in which block a house is.
        """
        counter = -1
        # looks from bottom to top if the house is in a particular row
        for i in range(10, 51, 10):
            if house.y_position <= i:
                # looks from left to right if the house is in a particular column
                for j in range(10, 51, 10):
                    counter += 1
                    if house.x_position <= j:
                        return counter
                        break
            else:
                counter += 5


    def largest_block(self):
        """
        Finds the block with the most houses in it.
        """
        large = 0
        block_with_most_houses = None
        # loops through all blocks
        for i in range(25):
            if len(self.blocks[i]) > large:
                # large will become the number of houses in block[i]
                large = len(self.blocks[i])
                block_with_most_houses = i
        return block_with_most_houses


    def connect_block_with_battery(self):
        """
        Connects all the houses in a block with the same battery/corresponding cable.
        If a house can't be connected because of the limit of the capacity
        of a battery, then this house will be added to a seperate list.
        """
        block = self.largest_block()
        for i in range(len(self.blocks[block])):
            # gets position of closest battery/cable
            position, list_batteries = self.model.get_closest_position(self.blocks[block][0])
            smallest_distance = 10000

            for house in self.blocks[block]:
                distance = self.model.get_distance(house, position)
                # determines the closest house to the battery/corresponding cable
                if smallest_distance > distance:
                    smallest_distance = distance
                    closest_house = house

            # removes closest house from the dictionairy
            list = self.blocks[block]
            list.remove(closest_house)
            self.blocks[block] = list

            # connects closest house to battery/corresponding cable
            if self.model.set_connection_block_given_battery(closest_house, position, list_batteries) == False:
                # append to list when house can't be connected
                self.houses_left.append(closest_house)
        self.blocks[block] = []


    def connect_left_over_houses(self):
        """
        Connect every house that couldn't be connect to a battery/cable before.
        """
        if self.houses_left != []:
            random.shuffle(self.houses_left)
            for house in self.houses_left:
                self.model.set_connection(house, self.houses_left)


    def run_housecounter(self):
        """
        Runs the housecounter algoritme. Returns model.
        """
        self.fill_blocks()
        for i in range(25):
            self.connect_block_with_battery()
        self.connect_left_over_houses()
        return self.model
