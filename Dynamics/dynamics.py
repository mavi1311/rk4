#!/usr/bin/env python

import numpy as np

operador = np.array([[0,1],[1,0]])

yinicial = np.array([[1,0],[0,0]])

def dyn_generator(oper, state):
    return (-1.0j)*(np.dot(oper,state)-np.dot(state,oper))

def rk4(func, oper, state, h):
    k_1 = h * func(oper , state)
    k_2 = h * func(oper , state + (k_1)/(2))
    k_3 = h * func(oper , state + (k_2)/(2))
    k_4 = h * func(oper , state + k_3)
    return state + 1/(6) * (k_1 + 2 * k_2 + 2* k_3 + k_4)

times = np.linspace(0.0,10.0,50)

h = times[1] - times [0]

ycopy = yinicial.copy()

stateQuant00 = np.zeros(times.size)
stateQuant11 = np.zeros(times.size)

for tt in range(times.size):
    stateQuant00[tt] = ycopy[0,0].real
    stateQuant11[tt] = ycopy[1,1].real
    yN = rk4(dyn_generator, operador, ycopy, h)

    ycopy = yN

import matplotlib.pyplot as plt

grafica = plt.plot(times,stateQuant00)

print(grafica)
