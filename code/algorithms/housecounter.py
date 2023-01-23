from code.classes.model import Model
from code.classes.district import District
import random

class Housecounter:
    def __init__(self, model):
        self.model = model
        self.blocks = {}

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
            # break

    # housecount = housecounter.Housecounter(model_2)
    # housecount.fill_blocks()
    # print(housecount.blocks)


    #         self.blocks.append(self.house)
    #         print(f"Lijst: {self.blocks}")
    #
    # housecount = housecounter.Housecounter(house)
    # housecount.houses_in_block()

    # for i in model.district.house:
    #     print(f"Nieuw huis{model.district.houses[0]}")
    #     print(f"ander huis{model.district.houses[1]}")
