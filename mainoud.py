from code.classes import battery, district, house, model
from code.algorithms import random
# from statistics import mean
# # from visualization import scatterplot, boxplot
#
# import matplotlib.pyplot as plt
# import numpy as np

if _name_ == "_main_":
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

        model_test = model.Model(district_test)
        solution = random.random_assignment(model_test)
        while solution.is_solution() is False:
            test = district.District(file)
            model_2 = model.Model(test)
            solution = random.random_assignment(model_2)

    solution.is_solution()
        # for house in solution.houses:
        #     print(solution[house].x_position )
        # "Er voor zorgen dat model dat gebruikt wordt zelfde naam heeft"




    # print(f"Every house had a connection to a battery: {solution.is_solution()}")
    # for house in solution.houses:
    #     print()
    # "X coordinaat batterij printen waaraan huis verbonden is"
    # for house in solution.houses:
    #     print(model_new.solution[house].x_position)

    # print(solution.houses[0].cables)
        #
        # " Totale afstand kabels berekenen"
        # sum = 0
        # for house in solution.district.houses:
        #     sum += house.distance_to_battery
        # #
        # list_cable_lengths.append(sum)

        # print(f"Total number of cables needed: {sum}")

    # print(list_cable_lengths)

    # bins_list = list(range(3600, 4400, 25))
    # boxplot.creating_boxplot(list_cable_lengths, bins_list)
    # # Show plot
    # boxplot.showing_plot()
    # # plt.show()
    # # plt.clear()
    # " De plot laat zien dat de kabellengtes berekent met het random algoritme normaal verdeeld is, er zijn geen sterke uitschieters te zien"
    # "In het geval van scheve verdelingen en verdelingen met uitbijters wordt het gemiddelde makkelijk beïnvloed door extreme waarden, waardoor je geen goed beeld krijgt van de centrale tendens."
    # "https://www.scribbr.nl/statistiek/gemiddelde/"
    #
    #
    # average = mean(list_cable_lengths)
    # print(f"Average sum of cables using random algorithm is: {average}" )
    #
    # "Data from district for plotting (batteries and houses)"
    #
    # x_batteries, y_batteries = scatterplot.creating_list_for_coordinates(district_test.district.batteries)
    # x_houses, y_houses = scatterplot.creating_list_for_coordinates(district_test.district.houses)
    #
    # " Showing all the batteries in a seperate plot"
    # for battery in district_test.district.batteries:
    #
    #     scatterplot.creating_grid_district(x_batteries, y_batteries, x_houses, y_houses)
    #
    #     for house in solution.district.houses:
    #
    #         # you only want to plot those houses which are connected to the current battery
    #         # if solution.solution[house]!= battery:
    #         if solution.solution[house].x_position != battery.x_position and solution.solution[house].y_position != battery.y_position:
    #             continue
    #
    #     scatterplot.plot_cables_house(solution.cables)
    #
    #
    # " Creating a plot of all connections"
    # scatterplot.creating_grid_district(x_batteries, y_batteries, x_houses, y_houses)
    #
    # for house in solution.houses:
    #     scatterplot.plot_cables_house(solution.cables)
    #
    #
    # " Showing all the plots"
    # scatterplot.showing_plot()
