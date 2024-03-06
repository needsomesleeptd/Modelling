import numpy as np
from matplotlib import pyplot as plt
import prettytable as pt


def u_der1(x, u):
    # print(x,u,x ** 2 + u ** 2)
    return x ** 2 + u ** 2


def u_der2(x, u):
    return 2 * x + 2 * u * u_der1(x, u)


def check_eps(yn, ydivn, eps):
    print(f'check_abs={abs((yn - ydivn) / (ydivn))}')
    return abs((yn - ydivn) / (ydivn)) > eps


'''def euler_method(x0, u0, h, eps, der_max=1e2, is_dyn_scale=True):
    u = u0
    x = x0
    xs = [x0]
    ys = [u0]
    u_div = u + h / 2 * u_der1(x, u)
    u = u + h * u_der1(x, u)
    #x_div = x0
    #u_div = u0
    while abs(u - u_div) >= eps * abs(u_div):
        print(abs(u - u_div) - eps * abs(u_div))
        xs.append(x)
        ys.append(u)
        u_save = u
        u_div = u + h / 2 * u_der1(x, u)
        u = u + h * u_der1(x, u)
        x += h

        der = u_der1(x, u)

        #if is_dyn_scale and der > der_max:
        #    h /= 2
        h = h * 0.99

    return xs, ys'''



def euler(x0, u0, h, eps, der_max=1e2, is_dyn_scale=True):
    
    #y0 = 0
    x_res = [x0]
    y_res = [u0]
    
    base_h = h
    
    yn = u0
    x = x0
    yn_2 = yn + h / 2 * u_der1(x, yn) 
    yn += h * u_der1(x, yn)
    x += h
    
    i = 1
    
    # print(abs(yn - yn_2) < eps * abs(yn_2))
    
    while abs(yn - yn_2) >= eps * abs(yn_2):
        y_res.append(yn)
        x_res.append(x)
        temp = yn
        #print(u_der1(x, yn))
        yn_2 = yn + h / 2 * u_der1(x, yn)
        yn += h * u_der1(x, yn)
        x += h
        i += 1

        der = abs(yn - temp) / h
        if is_dyn_scale and der > der_max:
            h /= 2
        
        
    return (x_res, y_res)


def pikar_first_sol(x):
    return x ** 3 / 3


def pikar_sec_sol(x):
    return x ** 3 / 3 + x ** 7 / 63


def pikar_th_sol(x):
    return x ** 3 / 3 + x ** 7 / 63 + 2 * x ** 11 / 2079 + x ** 15 / ((63 ** 2) * 15)


def pikar_forth_sol(x):
    return (x ** (31)) / 109876902975 + (4 * x ** (27)) / (3341878155) + (662 * x ** (23)) / (10438212015) + (
            82 * x ** (19)) / (37328445) + (13 * x ** (15)) / (218295) + (2 * x ** (11)) / (2079) + (x ** 7) / (
        63) + (x ** 3) / 3


xs, ys = euler(x0=0, u0=0, h=1e-3, eps=1e-6,der_max=1e4,is_dyn_scale= True)

pikar_first_ys = [pikar_first_sol(x) for x in xs]
pikar_sec_ys = [pikar_sec_sol(x) for x in xs]
pikar_third_ys = [pikar_th_sol(x) for x in xs]
pikar_forth_ys = [pikar_forth_sol(x) for x in xs]

#plt.plot(xs, ys, label='euler method')
plt.plot(xs, pikar_first_ys, label='pikar first')
plt.plot(xs, pikar_sec_ys, label='pikar secound')
plt.plot(xs, pikar_third_ys, label='pikar third')
plt.plot(xs, pikar_forth_ys, label='pikar forth')
plt.legend()
plt.grid()
plt.show()

plt.plot(xs, ys, label='euler')

plt.legend()
plt.grid()
plt.show()
#n = 100

table = pt.PrettyTable()
table.add_column("x", np.round(xs, 3))
table.add_column("euler", np.round(ys, 3))
table.add_column("pikar first", np.round(pikar_first_ys, 3))
table.add_column("pikar second", np.round(pikar_sec_ys, 3))
table.add_column("pikar third", np.round(pikar_third_ys, 3))
table.add_column("pikar forth", np.round(pikar_forth_ys, 3))
print(table)
#print(f'{xs=}')
#print(ys[:n])
#print(pikar_first_ys[:n])
#print(pikar_sec_ys[:n])
#print(pikar_third_ys[:n])
#print(pikar_forth_ys[:n])
#print(len(ys))
print(xs[-1])
