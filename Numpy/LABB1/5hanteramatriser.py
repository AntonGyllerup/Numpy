import numpy as np
#matris addition
A = np.array([[1,2],[3,4]])

B = A + 1 #till varje term adderas 1

print(B)

#multiplikation med skalär multipliceras varje element med skalären

#matrismultiplikation använder np.matmul
print(np.matmul(A,B))

#multiplikationstecken * gör elementvis multiplikation som beror på dimesion av arrayerna
#[1 2] * [1 3] = [1 6]
#[1 2] * [[1 3], [2 4]] = [[1 6], [2, 8]]

C = A + B
#sätta samman matriser
#np.vstack([A,B,C]) för att stacka de vertikalt
#np.hstack([A,B,C]) för att stacka de horizontellt
print(np.hstack([A,B,C]))

#funktioner som skapar standardmatriser
# I = np.eye(5)
print(np.ones((3,2)))

#numpys vanliag standardoperationer (sin,log etc) kan hantera numpy-arrays som argument och ger då arrays tillbaka


#lösning av ekvationssytem på formen Ax=B använder vi
#np.linalg.solve(A,B)