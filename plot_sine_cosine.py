import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
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
