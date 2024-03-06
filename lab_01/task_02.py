from matplotlib import pyplot as plt
import math as m
import numpy as np
import prettytable as pt



def get_k1(x, u):
    print(x, u)
    return u ** 3 + 2 * x * u


def get_k2(x, u, alpha, h):
    return get_k1(x + h / (2 * alpha), u + h / (2 * alpha) * get_k1(x, u))


def get_graphs(f1, f2, x0, xn, h):
    xs = []
    ys1 = []
    ys2 = []
    n = (xn - x0) / h
    for i in range(int(n + 1)):
        xs.append(x0)
        ys1.append(f1(x0))
        ys2.append(f2(x0))
        x0 = x0 + h

    return xs, ys1, ys2


def pikar_solve_first(u):
    return 0.5 + u ** 4 / 4 + u ** 2 / 2


def pikar_solve_sec(u):
    return 0.5 + 2 * ((u ** 6) / (24) + (u ** 4) / 8) + (u ** 4) / 4 + u ** 2 / 2


def pikar_solve_third(u):
    return 0.5 + 2 * ((u ** 8) / (96) + (u ** 6) / (12) + (u ** 4) / 8 + (u ** 2) / 4) + (u ** 4) / 4


def default_solve(u):
    return np.exp(u ** 2) - (u ** 2) / 2 - 1 / 2


ys, xs_pik, xs_def = get_graphs(pikar_solve_first, default_solve, 0, 1, 0.01)
xs_pik_sec = [pikar_solve_sec(ys[i]) for i in range(len(ys))]
xs_pik_third = [pikar_solve_third(ys[i]) for i in range(len(ys))]
#print(f'{ys=}')
#print(f'{xs_pik=}')
#print(f'{xs_pik_sec=}')
#print(f'{xs_pik_third=}')
#print(f'{xs_def=}')
table = pt.PrettyTable()
table.add_column("y", np.round(ys, 3))
table.add_column("analytic x", np.round(xs_def, 5))
table.add_column("Pikar x 1", np.round(xs_pik, 5))
table.add_column("Pikar x 2", np.round(xs_pik_sec, 5))
table.add_column("Pikar x 3", np.round(xs_pik_third, 5))
print(table)

plt.plot(xs_def, ys, label='analytic x')
plt.plot(xs_pik, ys, label='Pikar x 1')
plt.plot(xs_pik_sec, ys, label='Pikar x 2')
plt.plot(xs_pik_third, ys, label='Pikar x 3')
plt.legend()
plt.grid()
plt.show()
