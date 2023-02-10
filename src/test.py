import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x)
def f(x, a0, a1, a2, a3):
    return a0 + a1 * x + a2 * x**2 + a3 * x**3

# Define the points
x = np.array([0.5, -0.5, 0, -1])
y = np.array([1, 0, 0, 1])

# Perform the regression
A = np.array([[1, x[0], x[0]**2, x[0]**3],
              [1, x[1], x[1]**2, x[1]**3],
              [1, x[2], x[2]**2, x[2]**3],
              [1, x[3], x[3]**2, x[3]**3]])
b = y
a, _, _, _ = np.linalg.lstsq(A, b, rcond=None)

# Plot the points and the fitted function
xx = np.linspace(-1.5, 0.5, 100)
yy = f(xx, a[0], a[1], a[2], a[3])
print(a[0], a[1], a[2], a[3])
plt.plot(xx, yy, label="Fitted function")
plt.scatter(x, y, label="Original points")
plt.legend()
plt.show()


