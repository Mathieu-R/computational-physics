#get_ipython().run_line_magic("matplotlib", " widget")
import numpy as np
import matplotlib.pyplot as plt 


k = 1. # constante de rappel
m = 1. # mass 
w = np.sqrt(k/m) # pulsation

# matrix M for our EDO system: \dot{x} = Mx
M = np.array([[0, 1/m], [-k, 0]])

# initial conditions: x(0) = (q(0), p(0))
q0 = 1.
p0 = 0.

# time
t0 = 0
tf = 50
deltaT = 0.1

nt = int((tf - t0) / deltaT)

# time mesh
time_mesh = np.linspace(start=t0, stop=tf, num=nt)

# set initial conditions
# create a big matrix that will contain
# our position and speed solutions
# for each step time
x = np.zeros((2, nt))
x[:,0] = [q0, p0]

def analytical_solution(x, q0, p0, t):
    # q(t)
    x[0,:] = q0 * np.cos(w * t) + (p0 / m * w) * np.sin(w * t)
    # p(t)
    x[1,:] = - m * w * q0 * np.sin(w * t) + m * w * (p0 / m * w) * np.cos(w * t)
    return x

def forward_euler(x, nt, deltaT, M):
    for t in range(0,nt): 
        # x_{n+1} = x_n(1 + \Delta T  M)
        # x is a vector \in \R^2
        # 1 is the identity matrix
        x[:,t+1] = np.matmul(x[:,t], (np.identity(2) + deltaT * M))
        return x

def backward_euler(x, nt, deltaT, M):
    for t in range(0,nt):
        invert_matrix = np.linalg.inv(np.identity(2) - deltaT * M)

        x[:,t+1] = np.matmul(x[:,t], invert_matrix)
        return x

def centered_euler(x, nt, deltaT, M):
    for t in range(0, nt):
        normal_matrix = np.identity(2) + (deltaT/2) * M 
        invert_matrix = np.linalg.inv(np.identity(2) - (deltaT/2) * M)
        #matrix = np.matmul(normal_matrix, invert_matrix)

        x[:,t+1] = np.linalg.multi_dot([x[:,t], normal_matrix, invert_matrix])
        return x

forward_euler_sol = forward_euler(x, nt, deltaT, M)
backward_euler_sol = backward_euler(x, nt, deltaT, M)
centered_euler_sol = centered_euler(x, nt, deltaT, M)
analytical_solution = analytical_solution(x, q0, p0, time_mesh)
  
def plot(k, m):
    fig, ax = plt.subplots()
    ax.plot(analytical_solution[0,:], analytical_solution[1,:]/m, label="Théorique")
    ax.plot(forward_euler_sol[0,:], forward_euler_sol[1,:]/m, label="Euler avant")
    ax.plot(backward_euler_sol[0,:], backward_euler_sol[1,:]/m, label="Euler arrière")
    ax.plot(centered_euler_sol[0,:], centered_euler_sol[1,:], label="Euler centré")
    ax.legend(fontsize="small")
    ax.set_xlabel("$q$")
    ax.set_ylabel("$\dot{q}$")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_title(f"Harmonic Oscillator: $k={k}$, $m={m}$")
    plt.show()

plot(k, m)



