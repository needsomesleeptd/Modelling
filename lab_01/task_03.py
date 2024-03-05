from matplotlib import pyplot as plt
import math as m
def u_der1(x, u):
    print(x,u,x ** 2 + u ** 2)
    return x ** 2 + u ** 2


def u_der2(x, u):
    return 2 * x + 2 * u * u_der1(x, u)


def check_eps(yn, ydivn, eps):
    print(f'check_abs={abs((yn - ydivn) / (ydivn))}')
    return abs((yn - ydivn) / (ydivn)) > eps


def euler_method(x0, u0, h, eps):
    u = u0
    x = x0
    x_div = x0
    u_div = u0
    xs = []
    ys = []
    while u == u0 or check_eps(u, u_div, eps):
        xs.append(x)
        ys.append(u)
        u = u + h * u_der1(x, u)
        u_div = u_div + h / 2 * u_der1(x_div, u_div)
        x += h
        x_div += h / 2
    return xs, ys

def pikar_first_sol(x):
    return x**3/3
def pikar_sec_sol(x):
    return x**3/3+x**7/63
def pikar_th_sol(x):
    return x**3/3+x**7/63+2*x**11/2079+x**15/((63**2) *15)

xs,ys = euler_method(0,0,1e-8,7.1)
pikar_first_ys = [pikar_first_sol(x) for x in xs]
pikar_sec_ys = [pikar_sec_sol(x) for x in xs]
pikar_third_ys = [pikar_th_sol(x) for x in xs]

plt.plot(xs,ys,label='euler method')
plt.plot(xs,pikar_first_ys,label='pikar first')
plt.plot(xs,pikar_sec_ys,label='pikar secound')
plt.plot(xs,pikar_third_ys,label='pikar third')


plt.legend()
plt.show()
print(xs,ys)




