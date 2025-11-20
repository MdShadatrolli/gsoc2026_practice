import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot = np.dot(a, b)
print("Dot product:", dot)


A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[1, 0],
              [0, 1],
              [1, 1]])

C = np.matmul(A, B)
print("Matrix multiplication:\n", C)


M = np.array([[2, 3],
              [1, 4]])

det = np.linalg.det(M)
print("Determinant:", det)
inv = np.linalg.inv(M)
print("Inverse:\n", inv)


rank = np.linalg.matrix_rank(A)
print("Rank of A:", rank)


e_vals, e_vecs = np.linalg.eig(M)
print("Eigenvalues:", e_vals)
print("Eigenvectors:\n", e_vecs)


A = np.array([[3, 1],
              [1, 2]])

b = np.array([9, 8])

x = np.linalg.solve(A, b)
print("Solution x:", x)
