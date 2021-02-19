import numpy as np
import matplotlib.pyplot as plt 


k = 1 # constante de rappel
m = 1 # mass 
w = k/m # pulsation

# matrix M for our EDO system: \dot{x} = Mx
M = np.array([0, 1], [-w^2, 0])

# initial conditions
x0 = 1
v0 = 0

# time
t0 = 0
tf = 50
step = 0.1

nt = int((tf - t0) / step)

# time mesh
time_mesh = np.linspace(start=t0, stop=tf, num=nt)

# set initial conditions
# create a big matrix that will contain
# our position and speed solutions
# for each step time
x = np.ones((nt, nt))
x[0][0] = x0
x[0][1] = v0

def forward_euler(x, n, deltaT, M):
  x[1:n] = x[0:n-1] * (1 + deltaT * M)

def backward_euler(x, n, deltaT, M):
  invert_matrix = np.linalg.inv(1 - deltaT * M)
  
  x[1:n] = x[0:n-1] * invert_matrix
  
def centered_euler(x, n, deltaT, M):
  normal_matrix = 1 + (deltaT/2) * M 
  invert_matrix = np.linalg.inv(1 - (deltaT/2) * M)
  
  x[1:n] = x[0:n-1] * normal_matrix * invert_matrix
  
def plot(x, t):
  plt.plot(x, time_mesh)