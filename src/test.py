import matplotlib.pyplot as plt
import numpy as np

def plot_function(min_x, max_x, min_y, max_y, func):
    x = np.linspace(min_x, max_x, 1000)
    y = func(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Function Plot')
    ax.set_xticks(np.arange(min_x, max_x+1, 1))
    ax.set_yticks(np.arange(min_y, max_y+1, 1))
    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)
    plt.show()


def func(x, r=-2, a=1, b=1, c=1, d=1, e=1, f=1):
    return (x**2 / (r * (1 + np.sqrt(1 - (x**2 / r**2)))) + a*x**4 + b*x**6 + c*x**8 + d*x**10 + e*x**12 + f*x**14)

plot_function(-3, 3, 0, 40, func)