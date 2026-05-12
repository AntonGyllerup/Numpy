import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polynomial
from scipy.integrate import solve_ivp #ivp = initial value problem
import requests


#uppgift 1
# yprime = lambda t,y: 9 * t + 3 * t**3 - 5 * y**2
# y_start = 8
# t_start = 2
# t_end = 6
# solution = solve_ivp(yprime, [t_start, t_end], [y_start], max_step = 0.1, dense_output=True) #man kan byta max_step = 0.1 mot t_eval = np.linspace[0,4,100]
# print(solution)
# t = solution.t
# y = solution.y[0]
# plt.plot(t,y, "ro-")
# print(solution.sol(5)[0])
# plt.show()


#uppgift 2
# x = np.array([ 0.000, 1.000, 2.000, 3.000, 4.000, 5.000 ])
# y = np.array([ 3.749, 4.689, 6.273, 5.897, 6.381, 7.003 ])

# n = 5
# curve = polynomial.polyfit(x,y,n)
# print(curve)
# x_2 = np.linspace(-1,6,1000)
# y2 = polynomial.polyval(x_2, curve)
# plt.plot(x,y, "+")
# plt.plot(x_2, y2, "b-")
# plt.axis([0, 5, 3, 8])

# line = polynomial.polyfit(x,y,1)
# x3 = np.linspace(-1,6,1000)
# y3 = polynomial.polyval(x3,line)
# plt.plot(x3,y3, color = "red")

# plt.show()


#uppgift 3
# x = np.array([0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00, 1.10, 1.20, 1.30, 1.40, 1.50])
# y = np.array([1.69,2.14,1.94,2.48,3.29,2.95,3.62,3.95,6.24,6.68,6.29,8.37,9.82,8.51,12.75])

# ylog = np.log(y)

# curve = polynomial.polyfit(x,ylog,1)
# loga,logb = curve
# a = np.exp(loga)
# b = np.exp(logb)
# print(a,b)
# x_2 = np.linspace(0,2,100)

# def f(a,b,x):
#     return a * b**x

# y_2 = f(a,b,x_2)
# plt.plot(x,y, "ro")
# plt.plot(x_2, y_2, "b-")

# plt.show()

#uppgift 4
# url = 'https://fileadmin.cs.lth.se/cs/Education/EDAA85/numpy/race'
# data = requests.get(url).text
# with open('race.txt', 'w') as f: f.write(data)

# v = np.loadtxt('race.txt')
# print(v.size)
# print(v[0])
# print(v[450])

# x = np.linspace(0,40,v.size)

# plt.plot(x,v)
# plt.show()


#uppgift 5 - del 1
# v = np.loadtxt('race.txt')
# print(v.size)
# print(v[0])
# print(v[450])

# x = np.linspace(0,40,v.size)

# v[v==100] = 0


# plt.plot(x,v)

# plt.show()


#uppgift 5 - del 2
# v = np.loadtxt('race.txt')
# print(v.size)
# print(v[0])
# print(v[450])

# x = np.linspace(0,40,v.size)

# spikes = v == 100
# v[spikes] = v[np.where(spikes)[0]-1]

# plt.plot(x,v)

# maxhastighet = np.max(v)
# print(maxhastighet)

# plt.show()


#uppgift 6
# v = np.loadtxt('race.txt')

# x = np.linspace(0,40,v.size)

# spikes = v == 100
# v[spikes] = v[np.where(spikes)[0]-1]

# plt.plot(x,v)

# maxhastighet = np.max(v)
# print(maxhastighet)


# s = np.trapezoid(v,x)
# print(s)


# med_v = np.mean(v)
# print(med_v*40)


# plt.show()


#uppgift 7
# url = 'https://fileadmin.cs.lth.se/cs/Education/EDAA85/numpy/const_accel'
# data = requests.get(url).text
# with open('const_accel.txt', 'w') as f: f.write(data)


# v = np.loadtxt('const_accel.txt')

# x = np.linspace(0,5,v.size)

# plt.plot(x,v)
# plt.show()

# n=1
# curve = polynomial.polyfit(x,v,n)
# print(curve)
# print(curve[1])

# x_2 = np.linspace(0,4,100)
# yval = polynomial.polyval(x_2, curve)
# plt.plot(x_2, yval, "b-")

# plt.show()