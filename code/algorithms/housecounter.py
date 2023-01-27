from code.classes.model import Model
from code.classes.district import District
import random

class Housecounter:
    def __init__(self, model):
        self.model = model
        self.blocks = {}
        self.houses_left = []

    def fill_blocks(self):
        for i in range(25):
            self.blocks[i] = []
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
        position, list_batteries = self.model.get_closest_position(self.blocks[block][0])
        # random.shuffle(self.blocks[block])
        for house in self.blocks[block]:
            if self.model.set_connection_block_given_battery(house, position, list_batteries) == False:
                self.houses_left.append(house)
        self.blocks[block] = []


    def connect_left_over_houses(self):
        if self.houses_left != []:
            random.shuffle(self.houses_left)
            for house in self.houses_left:
                self.model.set_connection(house, self.houses_left)


    def connect_all_blocks(self):
        for i in range(25):
            self.connect_block_with_battery()
        self.connect_left_over_houses()
        return self.model

    # def run(self):
    #     list_cable_lengths = []
    #     solution = self.connect_all_blocks()
    #     sum = len(self.model.cables)
    #     list_cable_lengths.append(sum)
    #     return solution, list_cable_lengths

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
