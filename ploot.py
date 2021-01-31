from numpy import ma
import numpy as np

import csv

import sys
import os 

from matplotlib import ticker, cm
import matplotlib.pyplot as plt

def multiple_array(list1, list2):
    return to_array(list1), to_array(list2)

def to_array(List):
    b = [float(x) for x in List]
    b.sort()
    b = list(set(x))
    b = np.array(b)
    return b

for filename in os.listdir(r'C:\Users\ericm\Documents\Repos\SizingChart\DATTTTT'):
    x,y,z = ([],[],[])
    with open('DATTTTT/' + filename) as dataFile:
        data = csv.reader(dataFile, delimiter = ',')
        for row in data:
            x.append(row[0])
            y.append(row[1])
            z.append(row[2])

    x,y = multiple_array(x,y)

    fig, ax = plt.subplots()
    z = [float(x) for x in z]
    cs = ax.contourf(x, y, np.array(z).reshape(len(x), len(y)).transpose(), 25, cmap = cm.plasma)

    ax.set_xlabel('AR')
    ax.set_ylabel('Wing Area')
    
    cbar = fig.colorbar(cs)

    plt.savefig(f'Figures/{filename}')
