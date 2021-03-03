import numpy as np

ny = 100
dx = 

np.linspace(0,1,100)
y = np.zeros((2, ny))

# guess
y[:,0] = 0.   

def Jac(y_i):
    return np.array([
        [np.exp(-y_i[0])], 
        [-y[0] * np.exp(-y[0])]
    ])

def fun(y, i):
    return y[:,i+1] - 2*y[:,i] + y[:,i-1] + (dy ** 2) * np.exp(y[:,i])

def newton():
    for i in range(0:ny):
        y[:,i] - np.inv(Jac(y[:,i])) * fun(y, i)
