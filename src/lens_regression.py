import numpy as np
from data_handler import DataHandler
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from math_utility import MathUtility

class LensRegression:
    def __init__(self, data_path):
        self.points = DataHandler.load_data_from_excel(data_path)
        assert (len(self.points.shape) == 2 and self.points.shape[1] == 2)
        self.r = 2.0
        self.a4 = 2.0
        self.a6 = 2.0
        self.a8 = 2.0
        self.a10 = 2.0
        self.a12 = 2.0
        self.a14 = 2.0
        self.r_squared = None
        self.predicted_y = None

    def model_function(self, x, r, a4, a6, a8, a10, a12, a14):
        return r + a4*x**4 + a6*x**6 + a8*x**8 + a10*x**10 + a12*x**12 + a14*x**14

    def set_final(self):
        def fun(x, r, a4, a6, a8, a10, a12, a14):
            return (x**2 / (r * (1 + np.sqrt(1 - (x**2 / r**2))))) + a4*x**4 + a6*x**6 + a8*x**8 + a10*x**10 + a12*x**12 + a14*x**14
        parameters = [200000000, self.a4, self.a6, self.a8, self.a10, self.a12, self.a14]
        x = self.points[:, 0]
        print(x.min())
        print(x.max())
        self.predicted_y = fun(x, *parameters)


    def do_regression(self):
        x = self.points[:, 0]
        y = self.points[:, 1]
        parameters = [self.r, self.a4, self.a6, self.a8, self.a10, self.a12, self.a14]
        popt, pcov = curve_fit(self.model_function,x,y,p0 = parameters)
        self.predicted_y = self.model_function(x, *popt)
        self.r, self.a4, self.a6, self.a8, self.a10, self.a12, self.a14 = popt
        self.calculate_r_squared()

    def calculate_r_squared(self):
        x = self.points[:, 0]
        y = self.points[:, 1]
        parameters = [self.r, self.a4, self.a6, self.a8, self.a10, self.a12, self.a14]
        self.predicted_y = self.model_function(x, *parameters)
        residuals = y - self.predicted_y
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((y-np.mean(y))**2)
        self.r_squared = 1 - (ss_res / ss_tot) #Unbestimmtheitsmaß

    def shift_min_to_origin(self):
        x = self.points[:, 0]
        y = self.points[:, 1]
        min_y_index = y.argmin()
        x_min = x[min_y_index]
        y_min = y[min_y_index]
        x_shifted = x - x_min
        y_shifted = y - y_min
        self.points = np.column_stack((x_shifted, y_shifted))

    def rotate_points(self, angle):
        self.points = MathUtility.rotate_points_origin(self.points, angle)

    def render(self):
        print(self.r_squared)
        fig, ax = plt.subplots()
        ax.scatter(self.points[:, 0], self.points[:, 1], color='red')
        ax.scatter(self.points[:, 0], self.predicted_y, color='blue')
        plt.show()

