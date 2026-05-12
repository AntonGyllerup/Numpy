#neuralt nätverk, Z = WA + B 
#W indikerar weights där kolumn j har alla weights till nod j i lager 1
#A indikerar alla nodernas värden där varje rad har en nods värde (i lager 1)
#B är en konstant som adderas till varje nod
#Resultatet Z innehåller på rad k "pre-värdet" får nod k i lager 2

#Sedan har man någon form av funktion där man tar in "pre-värdet" för att få
#faktiska värdet. Ex kan man använda sigmoid funktionen och då får man
#A = \sigma(Z)
#A innehåller då slutgiltiga värdena för noderna i lager 2

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def sigma(x):
    z = 1.0/( 1 + np.exp( -x ))
    return z


image = mpimg.imread('one.png')
image_data = image.reshape(784, 1)

W1 = np.loadtxt('W1.txt')
W2 = np.array([[-0.16, -0.74, 2.48], [-0.745, 1.26, -2.314]])
B1 = np.array([[0.53], [0.62], [-0.183]])
B2 = np.array([[-1.0], [0.87]])


def predict(x):
    z1 = np.matmul(W1, x) + B1
    a1 = sigma(z1)
    z2 = np.matmul(W2, a1) + B2
    a2 = sigma(z2)
    return a2

result = predict(image_data)
print(result)

if result[0] > result[1]:
    print('En nolla!')
else:
    print('En etta!')

plt.imshow(image)
plt.show()