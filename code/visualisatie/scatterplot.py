" Lijsten maken om huizen en batterijen in op te slaan voor scatterplot"
import matplotlib.pyplot as plt
import numpy as np

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

def showing_plot():
    plt.show()
    # plt.clear()
