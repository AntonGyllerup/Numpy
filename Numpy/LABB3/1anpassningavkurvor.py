import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polynomial
import scipy.optimize as optimize

x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
y = [4.95, 8.95, 10.86, 11.88, 12.89, 14.65, 17.59, 21.68, 28.93]

#anpassa en kurva
n = 4
curve = polynomial.polyfit(x,y,n) #anpassar en n:te gradspolynom enligt minsta kvadratmetoden
x_2 = np.linspace(0,4,100)
yval = polynomial.polyval(x_2, curve)
plt.plot(x,y, "ro")
plt.plot(x_2, yval, "b-")


#vi kan anpassa mer avancerade kurvor - som exponentialfunktioner
log_y = np.log(y)
line = polynomial.polyfit(x, log_y, 1)
print(line)
loga, logc = line
a = np.exp(loga)
c = np.exp(logc)
f = lambda x: a * c**x
y_2 = f(x_2)
plt.plot(x_2, y_2, "red")
print(y_2)
plt.show()