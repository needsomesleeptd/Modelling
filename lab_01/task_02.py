from matplotlib import pyplot as plt
import math as m

INF = 1e8


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
    return 0.5 + (u ** 4 / 4 + u ** 2 / 2 - (1 / 2) ** 6 - (1 / 2) ** 3)


def pikar_solve_sec(u):
    return 0.5 + 2 * (u ** 6 / 24 + u ** 4 / 8 - 9 * u ** 2 / 128) + u ** 4 / 4 - int_pik_sec(0.5)


def pikar_solve_third(u):
    return 0.5 + int_pik_third(u) - int_pik_third(0.5)


def int_pik_third(u):
    return 2 * (u ** 8 / 96 + u ** 6 / 12 - 9 * u ** 4 / 256) + u ** 4 / 4


def int_pik_sec(x):
    return 2 * (x ** 6 / 24 + x ** 4 / 8 - 9 * x ** 2 / 128) + x ** 4 / 4


def default_solve(u):
    return m.exp(u ** 2) - (u ** 2) / 2 - 1 / 2


print(int_pik_sec(0.5))
ys, xs_pik, xs_def = get_graphs(pikar_solve_first, default_solve, 0, 1, 0.02)
xs_pik_sec = [pikar_solve_sec(ys[i]) for i in range(len(ys))]
xs_pik_third = [pikar_solve_third(ys[i]) for i in range(len(ys))]
print(f'{ys=}')
print(f'{xs_pik=}')
print(f'{xs_pik_sec=}')
print(f'{xs_pik_third=}')
print(f'{xs_def=}')

# plt.yscale('log')
plt.plot(ys, xs_def, label='true')
plt.plot(ys, xs_pik, label='pik ans')
plt.plot(ys, xs_pik_sec, label='pik ans sec')
plt.plot(ys, xs_pik_third, label='pik ans third')
plt.legend()
plt.show()
