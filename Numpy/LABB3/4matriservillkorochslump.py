import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polynomial
import scipy.optimize as optimize
from scipy.integrate import solve_ivp
import requests
import random

#matris - olika funktioner
#np.sum(A) summerar alla tal i A
#np.argmax(A) ger  index för det största elementet
#np.roll(v,1) roterar vektorn 1 steg bakåt
#np.reshape(...) ändrar dimensioner för matrisen
#np.where(...) filtrerar på olika villkor

#vi kan använda villkor för matriser

A = np.array([[1,1,-1],[2,1,1],[4,3,-1]])

#matriser med villkor
B = A >= 2 #B består nu av true eller false värden på varje position baserat på om värdet är större eller lika 2
print(B)
B = A[A >= 2] #vi får en vektor med alla element som är större än eller lika med 2
print(B)

print(np.where(A>2)) #ger alla index i A där värdet är större än 2

#man kan använda where ungefär som if sats genom följande
print(np.where(A>2,10,0)) #sätter alla värden större än 2 till 10 och alla andra till 0
print(np.where(A>2,0,A)) #sätter alla värden större än 2 till 0 och behåller övriga

#matriser med slumpvärden
D = np.random.rand(2,3) #skapar en 2x3 matris med slumpmässiga element mellan 0 och 1
D = np.random.randn(2,3) #skapar en 2x3 matris med slumpmässiga element mellan 0 +-1 med normalfördelning
D = np.random.randint(0,10, size = (2,3)) #skapar en 2x3 matris med slumpmässiga heltalselement mellan 0 9


v = np.linspace(0,10,11)
print(v)
print(np.roll(v,2))