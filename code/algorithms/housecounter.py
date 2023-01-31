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
        for house in self.model.district.houses:
            for i in range(25):
                if self.houses_in_block(house) == i:
                    self.blocks[i].append(house)


    def houses_in_block(self, house):
        counter = -1
        for i in range(10, 51, 10):
            # print(f"Dit is i: {i}{counter}")
            # counter += 1
            if house.y_position <= i:
                # print(f"True and {house}")
                for j in range(10, 51, 10):
                    counter += 1
                    if house.x_position <= j:
                        return counter
                        break
            else:
                counter += 5

    def largest_block(self):
        large = 0
        block_with_most_houses = None
        for i in range(25):
            if len(self.blocks[i]) > large:
                large = len(self.blocks[i])
                block_with_most_houses = i
        return block_with_most_houses


    def connect_block_with_battery(self):
        block = self.largest_block()
        for i in range(len(self.blocks[block])):
            position, list_batteries = self.model.get_closest_position(self.blocks[block][0])
            smallest_distance = 10000
            for house in self.blocks[block]:
                distance = self.model.get_distance(house, position)
                if smallest_distance > distance:
                    smallest_distance = distance
                    closest_house = house
            list = self.blocks[block]
            list.remove(closest_house)
            self.blocks[block] = list
            if self.model.set_connection_block_given_battery(closest_house, position, list_batteries) == False:
                self.houses_left.append(closest_house)
        self.blocks[block] = []


    def connect_left_over_houses(self):
        if self.houses_left != []:
            random.shuffle(self.houses_left)
            for house in self.houses_left:
                self.model.set_connection(house, self.houses_left)


    def run_housecounter(self):
        self.fill_blocks()
        for i in range(25):
            self.connect_block_with_battery()
        self.connect_left_over_houses()
        return self.model



    # def run(self, amount_valid_solutions, district_test):
    #
    #     list_cable_lengths = []
    #     first_loop = True
    #     while (len(list_cable_lengths) != amount_valid_solutions):
    #         model_test = Model(district_test)
    #         solution = self.connect_all_blocks()
    #
    #         sum = len(solution.cables)
    #
    #         if solution.is_solution() is not False:
    #             list_cable_lengths.append(sum)
    #
    #         if first_loop:
    #             smallest_solution = solution
    #
    #         if sum < len(smallest_solution.cables):
    #             smallest_solution = solution
    #
    #         first_loop = False
    #     return smallest_solution, list_cable_lengths


# model_test = model.Model(district_test)
# housecount = housecounter.Housecounter(model_test)
# housecount.fill_blocks()
# housecount.connect_all_blocks()
