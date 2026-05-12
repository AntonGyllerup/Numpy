#linjär algebra, många linjär algebra funktioner i np.linalg
import numpy as np
A = np.array([[1,1,-1],[2,1,1],[4,3,-1]])
print(np.linalg.det(A))

#vi kan transponera matrisen med .T enligt
print(A.T)

#invertera matriser (om det går) np.linalg.inv(A)

#lösa ekvationssystem Ax=b enligt np.linalg.solve(A,b)