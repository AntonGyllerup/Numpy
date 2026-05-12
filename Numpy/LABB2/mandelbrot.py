import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polynomial
import scipy.optimize as optimize

def complexmat(N, z0, z1):
    # skapar en N x N-matris med komplexa tal a + bi
    # där re(z0) <= a <= re(z1) och im(z1) <= b <= im(z0)
    # (jämnt fördelade i matrisen)
 
    xs = np.linspace(z0.real, z1.real, num = N)  # realdelar
    ys = np.linspace(z0.imag, z1.imag, num = N)  # imaginärdelar
 
    # skapa två matriser med real- respektive imaginärdelar
    [X, Y] = np.meshgrid(xs, ys)
 
    # matrisen X innehåller resultatets realdelar
    # matrisen Y innehåller resultatets imaginärdelar
 
    return X + 1j * Y    # <<< denna rad behöver utökas


def converge(c):
    k = 0
    z_k = c

    while np.abs(z_k) <= 2 and k < 100: 
        z_k = z_k**2 + c
        k +=1
    
    return k


        

        


        


N = 1000
z0 = -2+1j
z1 = 1-1j

m = complexmat(N, z0, z1)
v = np.zeros((N,N))
# for i in range(N):
#     for k in range(N):
#         c = m[i,k]
#         v[i,k] = converge(c)
vfunc = np.vectorize(converge)
v = vfunc(m)

plt.imshow(v, aspect=2/3)#cmap = plt.get_cmap("ocean")
plt.show()