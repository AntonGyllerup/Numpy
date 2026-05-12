import numpy as np

#vektorer och materiser kommer här nedan
#np.array för vektorer
v = np.array([2 + 1j, 4 +2j])
print(v)

#matriser är en lista med listor
A = np.array([[1,1,-1], [2,1,1], [4,3,-1]])
print(A)
B =  np.array([[1,1], [2,1], [4,3]])
print(B)
#B är en 3x2 matris ty varje lista är en rad, det finns tre rader med två kolumner

#vi kan hämta rader av värden från matrierna, notera vi indexerar från 0 och upp
print(A[0]) #vi hämtar 1:te raden

#vi kan hämta specifika värden, först rad, sedan kolumn
print(A[1, 0])  #rad 2 kolumn 1 ger 2

#vi kan ändra värden i matriser och vektorer på följande sätt
A[1,0] = 12  #vi ändrar pos 2,1 till värde 12
print(A)
v[0] = 3  #vi ändrar pos 1 till värde 3
print(v)



#övning
B = np.array([[1,2], [3,4]])
C = np.array([[2,3], [4,5]])

A = B+C

print(A)

print(np.array([[1j,0,0,4,4],[0,1j,0,4,4],[0,0,1j,4,4]]))