import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polynomial


#vi läser in och behandlar data från filer
# with open("test.txt", "r") as f:
#     lines = f.readlines()
#     #gör något med lines


#med numpy kan v i anväda loadtxt
# data = np.loadtxt("filnamn.txt", delimiter = ",", dtype = int) #delimiter anger vad värdena är skiljda med och dtype anger datatypen

data = np.loadtxt("LABB2/data.txt", delimiter = ",")
print(data)
print(data[0])
print(data[1])

#skriva till fil genom savetxt
# np.savetxt("saved.txt",data) skriver ut nump/arrayen data till filen, värdena separeras med ny rad och skriver ut med grundpotensform

# with open("saved2.txt", "w") as f:
#     f.write("hello") #skriver ut strängen hello

