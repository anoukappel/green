from code.classes import battery, district, house, cable


if __name__ == "__main__":
    """ creation of district object """
    file = "data/Huizen&Batterijen/district_1"
    district = district.District(file)
    # district = district.District(f"data/Huizen&Batterijen/district_1/district-1_houses.csv", f"data/Huizen&Batterijen/district_1/district-1_batteries.csv")
    """ saving initial bateries in a list where we are able to remove it """
    # print(district.batteries)
    ### connectie batterij en huis (huis en battery als input)
    ## cable connected to huis
    test_batterij = district.batteries[0]
    test_house = district.houses[0]
    # test_house.add_cable(5, 4)
    # test_house.add_cable(5, 3)
    print("this is battery postition")
    print(test_batterij.x_position)
    print(test_batterij.y_position)
    print("this is house postition")
    print(test_house.x_position)
    print(test_house.y_position)
    # test_house.add_horizontal_steps(test_batterij)
    # test_house.add_vertical_steps(test_batterij)
    test_house.add_route_from_house_to_battery(test_batterij)
    print(test_house.cables)
    print(38-34 + 47 - 12 +2)
    print(district.district)

    for house in district.houses:
        closest_battery = house.get_closest_battery(district.batteries)
    # batteries = test.batteries
    # huis = test.houses[0]
    # dictbijzijnde = huis.get_closest_battery(batteries)
    #
    # print(dictbijzijnde.x_position)
    # print(dictbijzijnde.y_position)
