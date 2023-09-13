# with doc
import random
import matplotlib.pyplot as plt


steps = int(input("please choose an amount of steps: "))
dims = int(input("please choose a number of possible dimensions: "))
coordinate_system = [[0 for step in range(steps)] for dim in range(dims)]

def walk():
    pass
    # calls move and stay_put

def move(dims, steps):
    direction = 1
    chdim = random.randint(0, dims)
    coin_flip = random.random()
    if coin_flip < 0.5:
        direction = -1
        coordinate_system[chdim][steps +1drunken _




def stay_put(dims, steps):
    pass

def diplay():
    pass

walk()
diplay()
