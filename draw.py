import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

direction = ["north", "east", "south", "west"]
dir_row = [1, 0, -1, 0]
dir_col = [0, 1, 0, -1]
interval = 0.00001

x = y = dim_x = dim_y = dir = 0
data = []


def parse_matrix(file):
    global x, y, dim_x, dim_y, dir, data
    with  open(file) as trail_file:
        x = y = dir = -1
        data = list()
        for i, line in enumerate(trail_file):
            data.append(list())
            for j, col in enumerate(line):
                if col == "#":
                    data[-1].append(15)
                elif col == ".":
                    data[-1].append(5)
                elif col == "S":
                    data[-1].append(35)
                    y = i
                    x = j
                    dir = 1
        dim_y = len(data)
        dim_x = len(data[0])


def turn_left():
    global dir
    dir = (dir - 1) % 4


def turn_right():
    global dir
    dir = (dir + 1) % 4


def move():
    global x, y
    data[x][y] = 25
    x = (x + dir_row[dir]) % dim_x
    y = (y + dir_col[dir]) % dim_y
    data[x][y] = 35


def parse_movement(file):
    with open(file) as moves:
        for single in moves:
            if single == "LEFT\n":
                turn_left()
            elif single == "RIGHT\n":
                turn_right()
            elif single == "FORWARD\n":
                move()
                plt.pause(interval)
            img.set_data(data)



parse_matrix("santa_fe.txt")

# create discrete colormap
cmap = colors.ListedColormap(['white', 'red', 'blue', 'black'])

# 5 - blank | 15 - food | 25 visited | 35 - actual
bounds = [0, 10, 20, 30, 40]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
img = ax.imshow(data, cmap=cmap, norm=norm)

# draw gridlines
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(0.5, dim_x, 1))
ax.set_yticks(np.arange(0.5, dim_y, 1))

plt.ion()
parse_movement("moves.log")
plt.show(block=True)