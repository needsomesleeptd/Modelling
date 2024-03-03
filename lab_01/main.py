import matplotlib.pyplot as plt


def simple_taylor(f, f_der, x0, x):
    return f(x0) + f_der(x0)(x - x0)


u = 1
u1 = 2

def f(x, y1):
    return -0.1 * y1 ** 2 - (1 + 0.1 * x) * y1

def u1_der1(x):
    return -0.1 * u1 ** 2 - (1 + 0.1 * x) * u

def u1_der2(x):
    return -0.2 * u1_der1(x) * u1 - (0.1 * u + (1 + 0.1 * x) * u1)

def u1_der3(x):
    return -0.2 * (u1_der1(x) ** 2 + u1 * u1_der2(x)) - (0.2 * u1 + (1 + 0.1 * x) * u1_der1(x))

def u1_der4(x):
    return  -0.2 * (3 * u1_der1(x) * u1_der2(x) + u1 * u1_der3(x)) - (0.3 * u1_der1(x) + (1 + 0.1 * x) * u1_der2(x))
def newton_method(x0, y0, xn, f_der0, h=0.2):
    xs = []
    ys = []
    y_der = []
    n = (xn - x0) / h
    y_res = y0
    xs.append(x0)
    ys.append(y0)
    for _ in range(int(n + 1)):
        y_prev = y_res
        y_res = y_res + h * f_der0
        f_der0 = f_der0 + h * (-0.1 * f_der0 ** 2 - (1 + 0.1 * x0) * y_prev)
        y_der.append(f_der0)
        x0 += h

        xs.append(x0)
        ys.append(y_res)
    y_der.append(f_der0)
    return xs, ys, y_der


# Define the function and its derivative


# Set initial guess, tolerance, and maximum iterations
h = 0.2

# Calculate function value using Newton's method
xs, ys, y_der = newton_method(0, 1, 30, 2, 0.01)

plt.plot(xs, ys)
plt.plot(xs, y_der)
plt.show()
print(xs)
print(ys)
print(y_der)
