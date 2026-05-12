import numpy as np
import matplotlib.pyplot as plt
#np.linspace ger ett antal jämnt fördelade värden i ett intervall, exempel
print(np.linspace(0,10, 5))   #ger 5 värden mellan 0 och 10
print(np.linspace(0,10, num = 5))
#det vi får är en numpy array
#om man inte anger att num är något tal får vi 50 värden, exempel
x = np.linspace(0,10)  
print(x.size)    #size ger hur många som ingår i arrayen

def sigma(x):
    return 1/(1+np.exp(-x))

x = np.linspace(-6,6) 
y = sigma(x) #här blir y en array då inputen x är en array, se nästa print
print(y.size) #ger 50

plt.plot(x,y)
plt.plot(3, sigma(3), "r+")
plt.grid()
plt.show()

#programmet väntar efter plt.show() tills man stänger plotten

print("hej")


x = np.linspace(0,10)
y = x**2
g = x**3

plt.plot(x,y, marker = "o", color = "red", linestyle = "none")
plt.plot(x, g, "bx")  #alternativt att man skriver x för marker och color blue
plt.show()




#övning
#polotta funktionen e^(-x/4)*sin(2\pi x) i intervallet 0 till 10
x = np.linspace(0,10, 1000)

def f(x):
    return np.exp(-x/4)*np.sin(2*np.pi*x)

y = f(x)

plt.plot(x, y)
plt.show()