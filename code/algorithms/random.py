from code.classes.model import Model
from code.classes.district import District
import random

def random_assignment(model):
    """
    Assign (randomly) every house to a battery which is closest and available.
    """
    random.shuffle(model.houses)

    for house in model.houses:
        model.set_connection(house, model.get_batteries())
    return model
