from code.classes.model import Model
from code.classes.district import District
import random

def random_assignment(model):
    """
    Assign (randomly) every house to a battery which is closest and available.
    """
    random.shuffle(model.district.houses)

    model.fill_battery_cable()
    
    for house in model.district.houses:
        ## sets connection between house and closest battery with available capacity
        model.set_connection(house, model.district.batteries)


    return model
