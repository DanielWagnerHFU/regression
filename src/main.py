from data_handler import DataHandler
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

def main():
    def func(x, r, a, b, c, d, e, f):
        return (x**2 / (r * (1 + np.sqrt(1 - (x**2 / r**2)))) + a*x**4 + b*x**6 + c*x**8 + d*x**10 + e*x**12 + f*x**14)

    def optimize_params(x, y):
        popt, pcov = curve_fit(func, x, y)
        return popt

    def shift_min_to_origin(x, y):
        min_y_index = y.argmin()
        x_min = x[min_y_index]
        y_min = y[min_y_index]
        x_shifted = x - x_min
        y_shifted = y - y_min
        return x_shifted, y_shifted

    data = DataHandler.load_data_from_excel("./doc/Asphaere_Rohdaten_Only-0-Grad.xlsx")
    x = data[:, 0]
    y = data[:, 1]
    x, y = shift_min_to_origin(x, y)
    #r, a, b, c, d, e, f = optimize_params(x, y)
    #x = np.linspace(-10, 10, 1000)
    #y = func(x, r, a, b, c, d, e, f)

    plt.plot(x, y, 'o-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Data Plot')
    plt.show()

if __name__ == "__main__":
    main()