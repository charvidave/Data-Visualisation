# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 12:14:31 2021

@author: Charvi
"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making random walks as long as the program is active
while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    #ax.scatter(rw.x_values, rw.y_values, s=12)
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap=plt.cm.Blues,
               edgecolors='none',s=5)
    ax.scatter(0,0, c='green', edgecolors='none', s=1000)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c ='red', edgecolors='none',
               s=1000)
    plt.show()
    
    keep_running = input("Make another walk? (y/n)?")
    if keep_running == 'n':
        break