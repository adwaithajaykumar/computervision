import numpy as np   #import numpy
import matplotlib.pyplot as plt # import matplo library for plotting

x = np.linspace(1,10,5) #generate 100 numbers evenly spaced between 0 to 2 pie

y1 = x*x #functions for sin and cos


plt.plot(x, y1, label='square')

plt.title("square wave")
plt.xlabel("x vlues")
plt.ylabel("y values")
plt.legend() # appears to help identify which colour is which graphs if on using multiple functions on single graph

plt.grid(True) # to see grids

plt.savefig("basicmatplot.png") #saves
plt.show() #shows

    
