import matplotlib.pyplot as plt
import prettytable as pt
import numpy as np

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


def pikar_method_1(x):
    return 1 + 2 * x - 0.7 * x ** 2 - x ** 3 / 60


def taylor(x):
    return 1 + 2 * x - 0.7 * x ** 2 - 1.54 / 6 * x ** 3 + 1.224 / 24 * x ** 4



def pikar_method_2(x):
    return 1 + (x ** 6) / (18000) - (
                (x ** 6) / (12000) + (7 * x ** 5) / (1000) + (11 * x ** 4) / (75) - (14 * x ** 3) / (
            15) + 2 * x ** 2) / (10) + (13 * x ** 5) / (3000) + (x ** 4) / (24) - (7 * x ** 3) / (20) - (
                x ** 2) / 2 + 2 * x


xs, ys = euler_method(0, 1, 2, 5, 0.01)
ys_pikar_2 = [pikar_method_2(x) for x in xs]
ys_pikar_1 = [pikar_method_1(x) for x in xs]
ys_taylor = [taylor(x) for x in xs]
plt.plot(xs, ys[0], label='u0 euler')
plt.plot(xs, ys_pikar_2, label='u0 pikar_2')
plt.plot(xs, ys_pikar_1, label='u0 pikar_1')
plt.plot(xs, ys_taylor, label='u0 taylor')
#print(f'{xs=}')
#print(f'{ys_taylor=}')
#for i in range(5):
    # plt.plot(xs,ys[i],label = f'u_der{i}')
    #print(ys[i])
#rint(f'{ys_pikar_2=}')
plt.grid()
plt.legend()
plt.show()

table = pt.PrettyTable()
table.add_column("x", np.round(xs, 3))
table.add_column("Teylor", np.round(ys_taylor, 5))
table.add_column("u Euler", np.round(ys[0], 5))
table.add_column("u Pikar 1", np.round(ys_pikar_1, 5))
table.add_column("u Pikar 2", np.round(ys_pikar_2, 5))
table.add_column("u' Euler", np.round(ys[1], 5))
table.add_column("u'' Euler", np.round(ys[2], 5))
table.add_column("u''' Euler", np.round(ys[3], 5))
table.add_column("u'''' Euler", np.round(ys[4], 5))

print(table)
