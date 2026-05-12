import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polynomial

p = [-1,0,1]
#hitta rötterna till polynom p genom
roots = polynomial.polyroots(p)
print(roots) #ger +-1 ty lösningen till -1 + x**2 = 0 är +-1

#skapa ett polynonm p från en lista med rötter - nollställen genom

p = polynomial.polyfromroots(roots)
print(p) #kommer ge [-1,0,1] ty det är vad man får med nollställen +-1

#räkna ut värdet av polynomet p för x-värdena x
x = [1,2,3]
y = polynomial.polyval(x,p)
print(y)

#anpassa ett n:te gradspolynom till punkterna (x,y)
n = 3
x = [0,1,2,3,4,5]
y = [a**2 for a in x]
line = polynomial.polyfit(x,y,n)
print(line)

#för att rita upp polynom kan vi använda polyval och plot

p = [30,-19,0,1]

x = np.linspace(-6,4, 100)
y = polynomial.polyval(x, p)

plt.plot(x,y)
plt.grid()
plt.show()


#anpassa polynom med polyfit
x = [0,1,2,3,4,5,6]
y = [6,5,4,3,2,1,0]

polyfunc = polynomial.polyfit(x,y,3)
print(polyfunc)

x = np.linspace(0,4, 100)
y = polynomial.polyval(x,polyfunc)
plt.plot(x,y)
plt.show()