import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polynomial

#vi beräknar integralen med trapetsmetoden

x = np.linspace(0,4, 100)
y = [a**2 for a in x]

area = np.trapezoid(y,x) #beräknar integralen med trapetsmetoden
print(area)

# plt.fill_between(x,y, color = "g", alpha = 0.5)
# plt.show()


#biblioteket scipy kan integrera

import scipy.integrate as integrate
start = 0
finish = 4

def f(x):
    p = [5, 9, -4, 1]
    return p[0] + p[1] * x + p[2] * x**2 + p[3] * x**3

area,error = integrate.quad(f, start, finish)
print(area, error)


#scipy optimize för att ex hitta nollställen till funktioner

import scipy.optimize as optimize

f = lambda x: np.exp(-x) * np.sin(x) * np.cos(x)
x = np.linspace(0,6, 100)
y = f(x)
plt.plot(x,y)
plt.grid()

x_0 = 1

zeroes = optimize.fsolve(f,x_0) #hittar nollställen till funktionen nära x_0
minval = optimize.minimize(f,x_0) #hittar minimivärdet nära x_0
minival = optimize.fminbound(f, start, finish) #hittar minimivärdet i intervallet start-finish, ger x-värdet

zeroes = optimize.fsolve(f, [0, 1.4, 2.9, 4.3])
print(zeroes)
plt.scatter(zeroes, [0,0,0,0], color = "r")

print(minval)
plt.show()