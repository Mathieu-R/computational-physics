import numpy as np
import matplotlib.pyplot as plt

import matplotlib
colors = matplotlib.cm.jet

# plate size: \Gamma: [-1,1] x [-1,1]
width = height = 2.
# space intervals
dx = dy = 0.1
# thermal diffusivity parameter
alpha = 4

# beta parameter
beta = 0.25

# initial temperature
t0 = 1

# number of steps
nx = int(width/dx)
ny = int(height/dy)
nt = 10

# mesh points in space
x_mesh = np.linspace(start=-1, stop=1, num=nx+1)
y_mesh = np.linspace(start=-1, stop=1, num=ny+1)

# mesh points in time
# numpy doc advice to use linspace 
# instead of arange for decimal time steps.
time_mesh = np.linspace(start=0, stop=1, num=nt+1)

# set initial conditions (t=0)
u0 = t0 * np.ones((nx+1, ny+1))

# numerical solution for each step time
u = u0.copy()

"""
apply finite difference equation, leverage numpy vectors (way faster) instead of python loop
@u: current u solution
@u0: prev u solution (was first initial conditions)
http://hplgit.github.io/fdm-book/doc/pub/diffu/html/._diffu-solarized001.html
https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/
"""
def finite_difference(u, u0, beta):
    # at each time step, compute mesh solution
    for t in range(0,nt):
        u[1:nx, 1:ny] = u0[1:nx, 1:ny] + beta * (u0[2:nx+1, 1:ny] + u0[0:nx-1, 1:ny] + u0[1:nx, 2:ny+1] + u0[1:nx, 0:ny-1] - 4*u0[1:nx, 1:ny])

        # set boundary conditions
        u[0, 1:ny] = 0
        u[nx, 1:ny] = 0
        u[1:nx, 0] = 1
        u[1:ny, ny] = 0

        u0 = u

    return u

def plot_mesh(u):
    plt.contourf(x_mesh, y_mesh, u, time_mesh, cmap=colors)
    plt.contour(x_mesh, y_mesh, u, time_mesh, colors="k", linewidths=1)
    plt.axis("off")
    plt.title("Equation de la chaleur")
    plt.show

result = finite_difference(u, u0, beta)
plot_mesh(result)



