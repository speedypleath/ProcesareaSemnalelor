import numpy as np
import matplotlib.pyplot as plt
def sine(amplitude, frequency, phase, time):
    return amplitude * np.sin(2 * np.pi * frequency * time + phase)

amplitude = 1
frequency = 2
phase = np.pi

n_samples = 60
time_of_view = 2

atime = np.linspace(0, time_of_view, int(10e5))
time = np.linspace(0, time_of_view, int(n_samples))

asignal = sine(amplitude, frequency, phase, atime)
signal = sine(amplitude, frequency, phase, time)

plt.plot(atime, asignal)
plt.grid(True)
plt.stem(time, signal)
plt.show()