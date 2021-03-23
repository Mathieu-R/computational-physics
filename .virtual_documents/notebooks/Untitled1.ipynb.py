import numpy as np
import matplotlib.pyplot as plt

radius = np.arange(0.6, 1.7, 0.1)

hartreefock = [-99.745, -99.93, -100.002, -100.019, -100.009, -99.98, -99.95, -99.93, -99.90, -99.872, -99.846]
mp2 = [-99.93, -100.12, -100.19, -100.22, -100.215, -100.196, -100.17, -100.14, -100.124, -100.098, -100.077]

plt.plot(radius, hartreefock, color="red", label="Hartree Fock")
plt.plot(radius, mp2, color="green", label="MP2")
plt.legend()
plt.xlabel("Radius [A]")
plt.ylabel("Energy [Hartree]")
plt.savefig("Energy_HF.png")



