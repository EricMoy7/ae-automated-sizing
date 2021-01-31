import matplotlib.pyplot as plt
import numpy as np

ax3 = plt.axhline(y=0.37888, color='r' ,label = 'Cruise - ROC 300' )
ax2 = plt.axvline(x=67.79992662, color='b', label = 'Landing - 4000')
x = np.linspace(0, 80, 80)
# y = .01*x
TOP = 38
slope = 1/(1.7*TOP)
y = slope*x

ax1 = plt.plot( x,y,label= "Take Off - 4500")
plt.legend()
plt.xlabel(r"$(\frac{W}{S})$", fontsize=15)
plt.ylabel(r"$(\frac{T}{W})$", rotation=0, fontsize=15, labelpad=20)
plt.show()