import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

#uppgift 2
# print(np.pi)
# print(np.sqrt(3))
# print(np.emath.sqrt(-3))
# print(np.emath.sqrt(1j))
# print(np.exp(1j*np.pi))


#uppgift 3
# z = np.emath.sqrt(1j)
# print(np.abs(z))
# print(np.angle(z))
# z = np.emath.sqrt(-3)
# print(z.real)
# print(z.imag)


#ugift 4
# Komplexa tal
# a = 3 + 2j;
# b = 5 - 1j;
# x = a * b
# print(x)


# uppgift 5
# g = lambda x: np.exp(-0.1 * x) * np.cos(x)
# a = 2
# print(f"g({a}) är: {g(a)}")


#uppgift 6
# g = lambda x: np.exp(-0.1 * x) * np.cos(x)
# x = np.linspace(0,10,100)
# print(f"x[26] är {x[26]}")
# print(type(x))
# print(x.size)
# y = g(x)
# print(g(x[26]) == y[26])

# plt.figure(figsize = (8,6))
# plt.plot(x,g(x))
# plt.title("Uppgift 6")
# plt.show()


#upgift 7
# h = 1e-6
# def deriv(f,x):
#     return (f(x+h)-f(x)) / h

# f = lambda x: np.pow(x, 2)
# print(deriv(f, 3))


#upgift 8
# h = 1e-6
# def deriv(f,x):
#     return (f(x+h)-f(x)) / h
# x = np.linspace(0,10,100)
# g = lambda x: np.exp(-0.1 * x) * np.cos(x)
# plt.plot(x, g(x))
# plt.plot(x, deriv(g,x), color = "red")

# plt.title("Uppgift 8: Funktionen och dess derivata")
# plt.legend(["funktionen", "derivata"])
# plt.savefig("funktionsbild.png")

# plt.show()


# #upgift 9
# h = 1e-6
# def deriv(f,x):
#     return (f(x+h)-f(x)) / h

# x = np.linspace(0,10,100)

# g = lambda x: np.exp(-0.1 * x) * np.cos(x)
# h_1 = lambda x: np.exp(-0.1*x) * np.cos(x) - 0.1 *  np.exp(-0.1*x) * np.sin(x)
# h_2 = lambda x: -0.1 * np.exp(-0.1*x) * np.cos(x) -  np.exp(-0.1*x) * np.sin(x)
# h_3 = lambda x: -0.1 * np.exp(-0.1*x) * np.cos(x) -  0.1 * np.exp(-0.1*x) * np.sin(x)

# deriv_array = deriv(g, x)
# h_1_array = h_1(x)
# h_2_array = h_2(x)
# h_3_array = h_3(x)

# h_1_array_difference = h_1_array - deriv_array
# h_2_array_difference = h_2_array - deriv_array
# h_3_array_difference = h_3_array - deriv_array

# print(norm(h_1_array_difference), norm(h_2_array_difference), norm(h_3_array_difference))


#upgift 10
# H1 = np.eye(5) * 4
# H2 = np.ones((5, 3)) * 3
# M = np.hstack([H1, H2])
# print(M)


#upgift 11
# A = np.array([[12,20,24], [2,6,-4], [2,4,3]])
# b = np.array([1048,244,194])
# x = np.linalg.solve(A,b)
# print(np.matmul(A, x))
# print(b)
# print(A*x) # multiplikation sker elementivs beroende på arraysens storlek/form

#upgift 12
# A = np.array([[1,1,-1], [2,1,1], [4,3,-1]])
# print(np.linalg.det(A))
# b = np.array([2,3,4])
# print(np.linalg.solve(A, b))  #ingen lösning


#upgift 13
#med recursion funktion
# def sqrt_algo(S, k):
#     if k == 0:
#         series_dict[k] =  S / 2
#         return S / 2
#     else:
#         series_dict[k]  =  (sqrt_algo(S, k-1) + S / (sqrt_algo(S, k-1))) / 2
#         return (sqrt_algo(S, k-1) + S / (sqrt_algo(S, k-1))) / 2
    
# S = float(input("The numebr you want the square root of: "))
# k = int(input("Number of iterations you want: "))
# series_dict = {}
# sqrt_algo(S, k-1)
# print(f"The squre root of {S} is given by the series: {series_dict}")
# print(f"Actual square root of {S} is: {np.sqrt(S)}")


#med iterationer / for-loop
# S = float(input("The number you want the square root of: "))
# k = int(input("Number of iterations you want: "))
# series = []

# x = S / 2
# series.append(x)
# for i in range (0, k):
#     x = (x + S / x) / 2
#     series.append(x)

# print(f"The series given by the iteration is: {series}")


#modified iterations to calculate witin a difference
# h = 1e-6
# S = float(input("The number you want the square root of: "))

# x_first = S
# x_second = S / 2
# n = 0
# while np.abs(x_second - x_first) >= h:
#     n += 1
#     x_first = x_second
#     x_second = (x_second + S / x_second) / 2

# print(f"The series converges to: {x_second} and it took {n} iterations")