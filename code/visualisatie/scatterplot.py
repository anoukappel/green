
import matplotlib.pyplot as plt
import numpy as np
from typing import Any, Tuple, Optional
from code.classes.model import Model


def creating_grid_district() -> None:
    """
    Function that creates a 50 x 50 grid.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1)

    # Major ticks every 10, minor ticks every 1
    major_ticks = np.arange(0, 51, 10)
    minor_ticks = np.arange(0, 51, 1)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)


def plot_one_battery(x_battery: int, y_battery: int, color: Any) -> None:
    """
    Function that plots one of the batteries on the grid with chosen color.
    """
    plt.plot(x_battery, y_battery, color = color, marker = 's', markersize = 8)


def plot_element(coordinates_list: list[int], color: Any, marker = "", linestyle = "")   -> None:
    """
    Function that plots a coordinate on the grid.
    """
    cb_x = []
    cb_y = []

    for coordinate in coordinates_list:
        cb_x.append(coordinate[0])
        cb_y.append(coordinate[1])

    plt.plot(cb_x, cb_y, color = color, marker = marker, linestyle = linestyle)


def show_scatterplot(smallest_solution: Model, multiple_plots = True) -> None:
    """
    Function that plots all the houses, batteries and all the cables.
    """

    colors = ['b', 'peru', 'g', 'r', 'k', 'm']

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
            plot_element(coordinates_cables, color = colors[i], linestyle = '-')

        # plotting the houses in color
        plot_element(houses_certain_battery, colors[i], marker = 'o')
        i = i + 1
        # creating seperate plots for each battery if condition is true
        if multiple_plots and i < 5:
            creating_grid_district()
