import numpy as np   #import numpy
import matplotlib.pyplot as plt # import matplo library for plotting

x = np.linspace(0, 2 * np.pi, 100) #generate 100 numbers evenly spaced between 0 to 2 pie

y1 = np.sin(x) #functions for sin and cos
y2 = np.cos(x)

plt.plot(x, y1, label='Sine')
plt.plot(x, y2, label='Cosine')
plt.title("Sine and Cosine Waves")
plt.xlabel("x (radians)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.savefig("sine_cosine_plot.png")
plt.show()


