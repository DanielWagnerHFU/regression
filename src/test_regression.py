from math import sqrt
import numpy as np

def f(x, a0, a1):
    T1 = 1-sqrt(1-x**2)
    T2 = a0*x**2 + a1*x**4
    return T1 + T2

def create_design_matrix(points, degrees):
    m = len(points)
    n = len(degrees)
    
    X = np.zeros((m, n))
    for i, point in enumerate(points):
        x, y = point
        for j, degree in enumerate(degrees):
            X[i, j] = x**degree
    
    return X

#2-sqrt(2-x**2)
m = 10
x_values = np.random.uniform(-1, 1, m)
y_values = (2-np.sqrt(2-x_values**2)) + 2 * x_values**2 + 4 * x_values**4 + np.random.normal(0, 0.01, m)

points = [(x, y) for x, y in zip(x_values, y_values)]
degrees = [2, 4]

# Create the design matrix
X = create_design_matrix(points, degrees)
Y = np.array([(y - (2-sqrt(2-x**2))) for x, y in points])
a = np.linalg.inv(X.T @ X) @ X.T @ Y
print(X)
print("------------------------")
print(a)