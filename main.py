from code.classes import battery, district, house, model
from code.algorithms import random
from statistics import mean

import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    """ creation of district object """
    file = "data/Huizen&Batterijen/district_1"
    # object district aanmaken bestaande uit batteries en huizen data
    district_test = district.District(file)

    """ Random assignment of house to battery, when solution invalid run again. """
    # model object aanmaken, district object meegeven

    #list maken van alle sums
    list_cable_lengths = []

    # 1000 x random laten lopen
    for i in range(1):
        # new_run = False

        model_test = model.Model(district_test)
        solution = random.random_assignment(model_test)
        while solution.is_solution() is False:
            test = district.District(file)
            model_2 = model.Model(test)
            solution = random.random_assignment(model_2)
            # new_run = True

        # for house in solution.houses:
        #     print(solution[house].x_position )
        "Er voor zorgen dat model dat gebruikt wordt zelfde naam heeft"
        # if new_run is True:
        #     model_new = model_2
        # else:
        #     model_new = model_test

    # print(f"Every house had a connection to a battery: {solution.is_solution()}")
    # for house in solution.houses:
    #     print()
    # "X coordinaat batterij printen waaraan huis verbonden is"
    # for house in solution.houses:
    #     print(model_new.solution[house].x_position)

    # print(solution.houses[0].cables)

        " Totale afstand kabels berekenen"
        sum = 0
        for house in solution.houses:
            sum += house.distance_to_battery
        #
        list_cable_lengths.append(sum)

        # print(f"Total number of cables needed: {sum}")

    # print(list_cable_lengths)

    # Creating dataset
    a = np.array(list_cable_lengths)

    # Creating histogram
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(a, bins = [3600, 3625, 3650, 3675, 3700, 3725, 3750, 3775, 3800, 3825, 3850, 3875, 3900, 3925, 3950, 3975, 4000, 4025, 4050, 4075, 4100, 4125, 4150, 4175, 4200, 4225, 4250, 4275, 4300, 4325, 4350, 4375, 4400])

    # Show plot
    # plt.show()
    " De plot laat zien dat de kabellengtes berekent met het random algoritme normaal verdeeld is, er zijn geen sterke uitschieters te zien"
    "In het geval van scheve verdelingen en verdelingen met uitbijters wordt het gemiddelde makkelijk beïnvloed door extreme waarden, waardoor je geen goed beeld krijgt van de centrale tendens."
    "https://www.scribbr.nl/statistiek/gemiddelde/"

    average = mean(list_cable_lengths)
    print(f"Average sum of cables using random algorithm is: {average}" )


    " Lijsten maken om huizen en batterijen in op te slaan voor scatterplot"

    def creating_list_for_coordinates(district):
        x = []
        y = []

        for item in district:
            x.append(item.x_position)
            y.append(item.y_position)

        return x, y


    " Basis plaatje met alle huizen en batterijen erop afgebeeld van bepaalde wijk"
    def creating_grid_district(x_batteries, y_batteries, x_houses, y_houses):
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(1, 1, 1)

            # Major ticks every 10, minor ticks every 1
            major_ticks = np.arange(0, 51, 10)
            minor_ticks = np.arange(0, 51, 1)

            ax.set_xticks(major_ticks)
            ax.set_xticks(minor_ticks, minor=True)
            ax.set_yticks(major_ticks)
            ax.set_yticks(minor_ticks, minor=True)

            # And a corresponding grid
            ax.grid(which='both')

            # Or if you want different settings for the grids:
            ax.grid(which='minor', alpha=0.2)
            ax.grid(which='major', alpha=0.5)

            plt.scatter(x_batteries, y_batteries, c ="red",
                        linewidths = 2,
                        marker ="s",
                        s = 80)

            plt.scatter(x_houses, y_houses, c ="black",
                        linewidths = 2,
                        marker ="o",
                        edgecolor ="black",
                        s = 60)

    def plot_cables_house(cables_coordinates):
        cb_x = []
        cb_y = []

        for cable_point in cables_coordinates:
            cb_x.append(cable_point[0])
            cb_y.append(cable_point[1])

        plt.plot(cb_x, cb_y, 'b-')

    "Data from district for plotting (batteries and houses)"

    x_batteries, y_batteries = creating_list_for_coordinates(district_test.batteries)
    x_houses, y_houses = creating_list_for_coordinates(district_test.houses)

    " Showing all the batteries in a seperate plot"
    for battery in district_test.batteries:

        creating_grid_district(x_batteries, y_batteries, x_houses, y_houses)

        for house in solution.houses:

            # you only want to plot those houses which are connected to the current battery
            if solution.solution[house]!= battery:
            # if solution.solution[house].x_position != battery.x_position and solution.solution[house].y_position != battery.y_position:
                continue

            plot_cables_house(house.cables)


    " Creating a plot of all connections"
    creating_grid_district(x_batteries, y_batteries, x_houses, y_houses)

    for house in solution.houses:
        plot_cables_house(house.cables)

    " Showing all the plots"
    plt.show()
