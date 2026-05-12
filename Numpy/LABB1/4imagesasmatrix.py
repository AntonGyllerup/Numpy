import numpy as np
import matplotlib.image as npimg
import matplotlib.pyplot as plt

img = npimg.imread("strawberry.jpg")
print(img.shape)
print(img[400,600])

copy = np.copy(img)
for row in range(0,800):
    copy[row,600] = np.array([0,0,0])

plt.imshow(copy)


plt.show()