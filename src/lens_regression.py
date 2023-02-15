from math import sqrt
import numpy as np
from data_handler import DataHandler
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from math_utility import MathUtility

class LensRegression:
    def __init__(self, data_path):
        self.points = DataHandler.load_data_from_excel(data_path)
        assert (len(self.points.shape) == 2 and self.points.shape[1] == 2)
        self.r = 1.0
        self.a4 = 1.0
        self.a6 = 1.0
        self.a8 = 1.0
        self.a10 = 1.0
        self.a12 = 1.0
        self.a14 = 1.0
        self.r_squared = None
        self.predicted_y = None

    def model_function(self, x, r, a4, a6, a8, a10, a12, a14):
        return (x**2 / (r * (1 + np.sqrt(1 - (x**2 / r**2))))) + a4*x**4 + a6*x**6 + a8*x**8 + a10*x**10 + a12*x**12 + a14*x**14

    def do_iterative_regression(self, set_r = True):
        if (set_r):
            self.r = max([abs(np.min(self.points[:, 0])), abs(np.max(self.points[:, 0]))]) + 100
        x = self.points[:, 0]
        y = self.points[:, 1]
        parameters = [self.r, self.a4, self.a6, self.a8, self.a10, self.a12, self.a14]
        popt, pcov = curve_fit(self.model_function,x,y,p0 = parameters)
        self.predicted_y = self.model_function(x, *popt)
        self.r, self.a4, self.a6, self.a8, self.a10, self.a12, self.a14 = popt
        self.calculate_r_squared()

    def do_analytical_regression(self, set_r = True):
        def create_design_matrix(points, degrees):
            m = len(points)
            n = len(degrees)
            X = np.zeros((m, n))
            for i, point in enumerate(points):
                x, y = point
                for j, degree in enumerate(degrees):
                    X[i, j] = x**degree
            return X

        def nonlinearPart(x_i):
            return (x_i**2 / (self.r * (1 + sqrt(1 - (x_i**2 / self.r**2)))))

        if (set_r):
            self.r = 9693416815.0
        x = self.points[:, 0]
        y = self.points[:, 1]
        points = [(x, y) for x, y in zip(x, y)]
        degrees = [4, 6, 8, 10, 12, 14]
        X = create_design_matrix(points, degrees)
        Y = np.array([(y - nonlinearPart(x)) for x, y in points])
        a = np.linalg.inv(X.T @ X) @ X.T @ Y
        self.r, self.a4, self.a6, self.a8, self.a10, self.a12, self.a14 = self.r, a[0], a[1], a[2], a[3], a[4], a[5]
        self.predicted_y = self.model_function(x, self.r, self.a4, self.a6, self.a8, self.a10, self.a12, self.a14)
        self.calculate_r_squared()


    def calculate_r_squared(self):
        x = self.points[:, 0]
        y = self.points[:, 1]
        parameters = [self.r, self.a4, self.a6, self.a8, self.a10, self.a12, self.a14]
        self.predicted_y = self.model_function(x, *parameters)
        residuals = y - self.predicted_y
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((y-np.mean(y))**2)
        self.r_squared = ss_res / ss_tot

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
        ax.scatter(self.points[:, 0], self.points[:, 1], color='red', s=1)
        ax.scatter(self.points[:, 0], self.predicted_y, color='blue', s=1)
        y_difference = abs(self.points[:, 1] - self.predicted_y)
        max_y = max([np.max(self.predicted_y), np.max(self.points[:, 1])])
        max_y_dif = np.max(y_difference)
        factor = max_y / max_y_dif
        y_difference = y_difference * (factor / 1.5)
        ax.scatter(self.points[:, 0], y_difference, color='green', s=1)
        plt.show()

