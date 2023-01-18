from code.classes import battery, district, house, model
from code.algorithms import random
from code.solutions import save_solution
from code.visualisatie import histogram, scatterplot

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
    first_loop = True
    # 1000 x random laten lopen
    number_of_loops = 100
    for i in range(number_of_loops):
        # new_run = False

        model_test = model.Model(district_test)
        solution = random.random_assignment(model_test)
        # if solution.is_solution() is True:
        #     print("True")
        while solution.is_solution() is False:
            test = district.District(file)
            model_2 = model.Model(test)
            solution = random.random_assignment(model_2)

        if first_loop:
            smallest_solution = solution
    # " Totale afstand kabels berekenen"
        sum = len(solution.cables)
        list_cable_lengths.append(sum)

        if sum < len(smallest_solution.cables):
            smallest_solution = solution

        first_loop = False
    # print(list_cable_lengths)
        # print(f"Total number of cables needed: {sum}")

    # print(list_cable_lengths)
    print(len(smallest_solution.cables))

    # Plotting histogram greedy + random
    a = np.array(list_cable_lengths)
    histogram.plotting_histogram(a)

    # " De plot laat zien dat de kabellengtes berekent met het random algoritme normaal verdeeld is, er zijn geen sterke uitschieters te zien"
    # "In het geval van scheve verdelingen en verdelingen met uitbijters wordt het gemiddelde makkelijk beïnvloed door extreme waarden, waardoor je geen goed beeld krijgt van de centrale tendens."
    # "https://www.scribbr.nl/statistiek/gemiddelde/"

    average = mean(list_cable_lengths)
    # print(f"Average sum of cables using random algorithm is: {average}" )


    # " Lijsten maken om huizen en batterijen in op te slaan voor scatterplot"


    # "Data from district for plotting (batteries and houses)"

    x_batteries, y_batteries = scatterplot.creating_list_for_coordinates(district_test.batteries)
    x_houses, y_houses = scatterplot.creating_list_for_coordinates(district_test.houses)

    # " Showing all the batteries in a seperate plot"
    # for battery in district_test.batteries:
    #
    #     creating_grid_district(x_batteries, y_batteries, x_houses, y_houses)

        # for key in solution.battery_cable:
        #     for item in solution.battery_cable[key]:



        # for house in solution.district.houses:
        #
        #     # you only want to plot those houses which are connected to the current battery
        #     if solution.solution[house]!= battery:
        #     # if solution.solution[house].x_position != battery.x_position and solution.solution[house].y_position != battery.y_position:
        #         continue
        #
        #     plot_cables_house(solution.cables)


    # " Creating a plot of all connections"
    scatterplot.creating_grid_district(x_batteries, y_batteries, x_houses, y_houses)

    # for house in solution.district.houses:
    #     plot_cables_house(house.cables)
    for key in smallest_solution.battery_cable:
        # print(key)
        for item in smallest_solution.battery_cable[key]:
            # print(item)
            # x_pos = int(item[0][0])
            # y_pos = int(item[0][1])
            coordinates = item
            # print(len(coordinates))
            if len(coordinates) != 2:
                # print(coordinates)
                scatterplot.plot_cables_house(coordinates)

    scatterplot.showing_plot()
    # plot_cables_house(solution.cables)

    # " Showing all the plots"
    # plt.show()
