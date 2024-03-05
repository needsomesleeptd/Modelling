import matplotlib.pyplot as plt





def u1_der1(x, u, u1):
    return -0.1 * u1 ** 2 - (1 + 0.1 * x) * u


def u1_der2(x, u, u1):
    return -0.2 * u1 * u1_der1(x, u, u1) - u1 - 0.1 * u - 0.1 * u1 * x


def u1_der3(x, u, u1):
    return (-0.2 * (u1_der1(x, u, u1) ** 2) - 0.2 * u1 * u1_der2(x, u, u1)
            - u1_der1(x, u, u1) - 0.2 * u1 - 0.1 * u1_der1(x, u, u1) * x)


def u1_der4(x, u, u1):
    return (-0.4 * u1_der1(x, u, u1) * u1_der2(x, u, u1) - 0.2 * u1_der1(x, u, u1) * u1_der2(x, u, u1)
            - 0.2 * u1 * u1_der3(x, u, u1) - u1_der2(x, u, u1)
            - 0.2 * u1_der1(x, u, u1) - 0.1 * u1_der2(x, u, u1) * x
            - 0.1 * u1_der1(x, u, u1))


def euler_method(x0, u0, u10, xn, h=0.2):
    xs = []
    ys = [[], [], [], [], []]  # for y,y',..,y'''''
    n = (xn - x0) / h
    u = u0
    u1 = u10
    u2 = u1_der1(x0, u, u1)
    u3 = u1_der2(x0, u, u1)
    u4 = u1_der3(x0, u, u1)
    # u5 = u1_der4(x0, u, u1)
    x = x0
    for _ in range(int(n + 1)):
        xs.append(x0)
        ys[0].append(u)
        ys[1].append(u1)
        ys[2].append(u2)
        ys[3].append(u3)
        ys[4].append(u4)
        u_save = u + h * u1
        u1_save = u1 + h * u1_der1(x, u, u1)
        u2_save = u2 + h * u1_der2(x, u, u1)
        u3_save = u3 + h * u1_der3(x, u, u1)
        u4_save = u4 + h * u1_der4(x, u, u1)
        #  u5_save = u5 + h * u4
        x0 += h

        u = u_save
        u1 = u1_save
        u2 = u2_save
        u3 = u3_save
        u4 = u4_save
    # u5 = u5_save

    return xs, ys


# Define the function and its derivative


# Set initial guess, tolerance, and maximum iterations
h = 0.2

# Calculate function value using Newton's method
xs, ys = euler_method(0, 1, 2, 10, 0.1)

plt.plot(xs, ys[0],label = 'u0')
print(xs)
for i in range(5):
    #plt.plot(xs,ys[i],label = f'u_der{i}')
    print(ys[i])

plt.legend()
plt.show()
