n=8
M = 5 * np.eye(n) + 2 * np.eye(n, k=1) + 2 * np.eye(n, k=-1)
print(M)

print(np.linalg.det(M))