import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polynomial
import scipy.optimize as optimize


#uppgift 1
# p = [1512, -498, -263, 33, 15, 1]

# roots = polynomial.polyroots(p)
# print(roots)

# def poly(x):
#     return p[0] + p[1] * x + p[2] * x**2 + p[3] * x**3 + p[4] * x**4 + p[5] * x**5
# print(poly(roots))
# print(poly(np.array([9,4])))


#uppgift 2
# roots = np.array([-7, -5, -3, 2, 6])

# p = polynomial.polyfromroots(roots)
# print(p)
# def poly(x):
#     return p[0] + p[1] * x + p[2] * x**2 + p[3] * x**3 + p[4] * x**4 + p[5] * x**5
# x = np.linspace(-7.5,7, 1000) #att plotta från -50 till 50 är wild
# y = poly(x)

# plt.plot(x,y)
# plt.show()


#uppgift 3
# f = lambda t: 5 * np.exp(-0.5*t) + 2 * t**3

# x = np.linspace(1.5, 2.6, 100)
# y = f(x)

# area = np.trapezoid(y,x)
# print(area)

# plt.fill_between(x,y, alpha = 0.5)
# plt.show()


#uppgift 4
# g = lambda x: np.cos(np.exp(x)) / (1-x)


# x = np.linspace(2, 3, 100)
# y = g(x)
# plt.plot(x,y)
# plt.grid()

# x_0_värden = [2.5, 2.9]
# for values in x_0_värden:
#     minimas = optimize.minimize(g, values)
#     print(minimas.x, minimas.fun)

# plt.show()


#uppgift 5
# h = lambda x: 8 * x**2 - x - 2 * np.exp(-x**2)

# x = np.linspace(-2, 2, 10000) # kollat och den växer mycket vid stora eller små pga exp termen
# y = h(x)
# plt.plot(x,y)
# plt.grid()

# x_0_värden = [2.5, 2.9]
# for values in x_0_värden:
#     minimas = optimize.minimize(h, values)
#     print(minimas.x, minimas.fun)

# roots = optimize.fsolve(h, [-2,2])
# print(roots)

# plt.show()


#uppgift 6
# n=8
# M = 5 * np.eye(n) + 2 * np.eye(n, k=1) + 2 * np.eye(n, k=-1)
# print(M)

# print(np.linalg.det(M))