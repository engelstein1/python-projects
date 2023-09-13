import random

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('TkAgg')
matplotlib.use('Agg')

#
steps = int(input("please enter an amount of steps: "))
dims = int(input("please enter a amount of dimension: "))
coordinate_system = [[0 for i in range(steps)] for j in range(dims)]


#
# def random_dimension(dims):
#     dims_lst = [*range(1, dims + 1)]
#     dimension = random.choice(dims_lst)
#     return dimension
# main

def main(dims, steps):
    for step in range(steps):
        move(step, random_dimension(dims))
        stay(coordinate_system, step)
    print(coordinate_system)
    show(coordinate_system)

def random_dimension(dims):
    lst = []
    for i in range(dims):
        lst.extend([i])
    random_dim = random.choice(lst)
    return random_dim


def move(step, random_dim):
    direction = [1, -1]

    random_direction = random.choice(direction)
    coordinate_system[random_dim][step] += random_direction


def stay(coordinate_sys, step):
    for i in range(dims):
        coordinate_system[i][step] += coordinate_system[i][step - 1]


def show(coordinate_system):
    if len(coordinate_system) < 4:
        ax = plt.figure().add_subplot(projection='3d')
        cs = coordinate_system
        # Prepare arrays x, y, z
        theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
        z = np.linspace(-2, 2, 100)
        r = z ** 2 + 1
        x = r * np.sin(theta)
        y = r * np.cos(theta)

        ax.plot(np.array(cs[0]), np.array(cs[1]), np.array(cs[2]), label='parametric curve')
        ax.legend()

        plt.show()
    else:
        for dim in coordinate_system:
            print(dim)


#     return show()
main(dims, steps)

# move(5,2,4)


# plt.figure(figsize=(10, 6))
# plt.plot(coordinate_system)
#
# plt.show()
