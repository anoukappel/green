import json

# def calculate_costs_cables(houses):
#     number_of_cables = 0
#     for house in houses:
#         number_of_cables += house.distance_to_battery
#     costs = 9 * number_of_cables
#     return costs
#
# def calculate_costs_batteries(batteries):
#     return len(batteries) * 5000

def create_house_dict(solution, battery):
    houses = []
    for house in solution.solution:
        if solution.solution[house] == battery:
            for list in solution.battery_cable[battery]:
                if list[0] == [house.x_position, house.y_position]:
                    cables = []
                    for item in list:
                        cables.append(f"{item[0]}, {item[1]}")
            # cables = []
            # for item in house.cables:
            #     cables.append(f"{item[0]}, {item[1]}")
                    dict_house = {
                        "location": f"{house.x_position},{house.y_position}",
                        "output": house.maxoutput,
                        "cables": cables
                    }
                    houses.append(dict_house)
    return houses

def create_battery_dict(solution, dict):
    for battery in solution.district.batteries:
        houses = create_house_dict(solution, battery)
        dict.append({
            "location": f"{battery.x_position}, {battery.y_position}",
            "capacity": 1507.0,
            "houses": houses
        })

def save(filename, solution):
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
    jsonFile = open(f"code/experiments/{filename}.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
