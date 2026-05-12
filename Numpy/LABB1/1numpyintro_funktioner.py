#listor
listvariable1 = [1, 2, 3]
listvariable2 = [4, 5, 6]

print(listvariable1 + listvariable2)
#ger [1,2,3,4,5,6]

#numpy
import numpy as np

#funktion i numpy
#np.sin(x)  använder radianer
#np.round(x)  avrunda tal  (2.5 avrundas till 2 och inte 3)
#np.floor(x) avrunda ner

#np.sqrt(x)
#np.exp(x)
#np.logX(y)    X-logaritmen av y   exempelvis
print(np.log2(2))
#om ingen X så är det e
print(np.log(np.e))

#imaginära tal skrivs med 1j, exempel
print((1j)**2)

#för att använda imaginära tal genom roten ur används emath (tänk imaginary math), exempelvis
print(np.emath.sqrt(-1))

#ta Re(z) och Im(z) genom
z = 1+2j
print(z.real)
print(z.imag)
#alternativt
print(np.real(z))
print(np.imag(z))

#np.abs(x) tar absolutbelopp
print(np.abs(-3))
#för imaginära tal funkar abs som vanligt
print(np.abs(1+1j))

#np.angle(z) ger vinkeln till z
print(180 /np.pi * np.angle(1+1j))


#lambda uttryck, skapar funktioner
f = lambda x: np.sqrt(1 + np.sin(x))

print(f(2))

#ta in två värden
g = lambda x, y: np.sin(x)+y**2

z = f(3) + g(5,9)

print("z =", z)


#annat sätt att definera funktioner är med def
def f2(x):
    #...
    #...
    return np.sin(x)

z2 = f2(0.5)
print("z2 =", z2)



#vi kan skcika in annat i def funktionerna, exempelvis andra funktioner
def f3(x, f):
    #...
    #...
    return np.sin(x)

z3 = f3(0.5, np.sin)
print(z3)