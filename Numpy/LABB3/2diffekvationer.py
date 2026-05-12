import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polynomial
import scipy.optimize as optimize
from scipy.integrate import solve_ivp

yprime = lambda t, y: -np.sin(t)
y_start = 2
t_start = 0
t_end = 4
solution = solve_ivp(yprime, [t_start, t_end], [y_start], max_step = 0.1) #man kan byta max_step = 0.1 mot t_eval = np.linspace[0,4,100]
print(solution)
t = solution.t
y = solution.y[0]
plt.plot(t,y, "ro-")
plt.show()

#vid ett system av diffekvationer så blir yprime ovan en lista och [ystart] blir en lista av startvärden
#vid högre ordningens diffekvationer så kommer man göra variabelbyte där varje derivata blir en ny variabel y_1,y_2 osv
#se nedan
def yprime(t,yc):
    y1 = yc[0]
    y2 = yc[1]
    y1prime = y2
    y2prime = 3 * y1 - 7 * y2
    return [y1prime, y2prime]

solution = solve_ivp(yprime, [0,2], [0,1], max_step = 0.1)
y = solution.t
y = solution.y[0]
plt.plot(t,y, "ro-")
plt.show()