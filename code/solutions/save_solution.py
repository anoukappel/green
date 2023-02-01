import json
from code.classes.model import Model
from code.classes.battery import Battery


def create_house_dict(solution: Model, battery: Battery) -> list:
    """
    Returns a list of houses connect to a particular battery.
    """
    houses: list = []
    for house in solution.solution:
        if solution.solution[house] == battery:
            for list in solution.battery_cable[battery]:
                if list[0] == [house.x_position, house.y_position]:
                    cables = []
                    for item in list:
                        cables.append(f"{item[0]}, {item[1]}")
                    dict_house = {
                        "location": f"{house.x_position},{house.y_position}",
                        "output": house.maxoutput,
                        "cables": cables
                    }
                    houses.append(dict_house)
    return houses


def create_battery_dict(solution: Model, dict) -> None:
    """
    Makes a battery dict which will be filled with the houses.
    """
    for battery in solution.district.batteries:
        houses = create_house_dict(solution, battery)
        dict.append({
            "location": f"{battery.x_position}, {battery.y_position}",
            "capacity": 1507.0,
            "houses": houses
        })

def save(filename, solution: Model) -> None:
    """
    Creates a json file.
    """
    district = solution.district.district
    # own_costs = calculate_costs_cables(solution.district.houses) + calculate_costs_batteries(solution.district.batteries)
    output = [
                {
                    "district": district,
                    "costs-shared": solution.return_total_costs()
                },
    ]
    create_battery_dict(solution, output)
    jsonString = json.dumps(output, indent=4)
    jsonFile = open(f"code/experiments/{filename}", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
