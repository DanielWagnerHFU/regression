import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

def func(x, r, a, b, c, d, e, f):
    return (x**2 / (r * (1 + np.sqrt(1 - (x**2 / r**2)))) + a*x**4 + b*x**6 + c*x**8 + d*x**10 + e*x**12 + f*x**14)

def optimize_params(x, y):
    popt, pcov = curve_fit(func, x, y)
    return popt

x = np.array([...])  # input x values
y = np.array([...])  # input y values
params = optimize_params(x, y)
r, a, b, c, d, e, f = params

x_fit = np.linspace(x.min(), x.max(), 1000)
y_fit = func(x_fit, r, a, b, c, d, e, f)

plt.plot(x_fit, y_fit, 'r', label='fit')
plt.scatter(x, y, label='data points')
plt.legend()
plt.show()