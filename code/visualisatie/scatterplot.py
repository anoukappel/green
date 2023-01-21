import matplotlib.pyplot as plt
import numpy as np

def creating_grid_district():
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

def plot_one_battery(x_battery, y_battery, color):
    plt.plot(x_battery, y_battery, color = color, marker = 's', markersize = 8)

def plot_element(cables_coordinates, color, marker = "", linestyle = ""):
    cb_x = []
    cb_y = []

    for cable_point in cables_coordinates:
        cb_x.append(cable_point[0])
        cb_y.append(cable_point[1])

    plt.plot(cb_x, cb_y, color = color, marker = marker, linestyle = linestyle)


def show_scatterplot(smallest_solution, multiple_plots = True):
    colors = ['b', 'c', 'g', 'r', 'k', 'm']

    creating_grid_district()

    i = 0
    # looping through each battery
    for key in smallest_solution.battery_cable:
        houses_certain_battery = []
        plot_one_battery(key.x_position, key.y_position, colors[i])
        # looping trough al cable coordinates connected to battery
        for item in smallest_solution.battery_cable[key]:
            houses_certain_battery.append(item[0])
            coordinates_cables= item
            # plotting the cables
            plot_element(coordinates_cables, color = 'b', linestyle = '-')

        # plotting the houses in color
        plot_element(houses_certain_battery, colors[i], marker = 'o')
        i = i + 1
        # creating seperate plots for each battery if condition is true
        if multiple_plots and i < 5:
            creating_grid_district()

    plt.show()
    plt.close()
