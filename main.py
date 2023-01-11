from code.classes import battery, district, house, cable


if __name__ == "__main__":
    test = district.District(f"data/Huizen&Batterijen/district_1/district-1_houses.csv", f"data/Huizen&Batterijen/district_1/district-1_batteries.csv")
    print(test.houses[0])

    batteries = test.batteries
    huis = test.houses[0]
    dictbijzijnde = huis.get_closest_battery(batteries)

    print(dictbijzijnde.x_position)
    print(dictbijzijnde.y_position)
