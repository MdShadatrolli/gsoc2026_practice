import numpy as np

# ==== RESHAPE ====
a = np.array([1, 2, 3, 4, 5, 6])
print("Original:", a)

# reshape to 2 rows & 3 columns
r1 = a.reshape(2, 3)
print("Reshaped (2x3):\n", r1)

# reshape to 3 rows & 2 columns
r2 = a.reshape(3, 2)
print("Reshaped (3x2):\n", r2)

# reshape using -1 (auto calculate)
r3 = a.reshape(-1, 3)
print("Reshape with -1:\n", r3)

# ==== TRANSPOSE ====
m = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Original matrix:\n", m)
print("Shape:", m.shape)

t = m.T
print("Transposed matrix:\n", t)
print("Shape:", t.shape)

# Transpose of a column vector
col = np.array([[1], [2], [3]])
print("Column vector:\n", col)
print("Transposed column (row vector):\n", col.T)


m = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Matrix:\n", m)

# Sum along columns (axis = 0)
print("Sum axis=0 (column-wise):", np.sum(m, axis=0))

# Sum along rows (axis = 1)
print("Sum axis=1 (row-wise):", np.sum(m, axis=1))

# Mean along columns
print("Mean axis=0:", np.mean(m, axis=0))

# Mean along rows
print("Mean axis=1:", np.mean(m, axis=1))


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a:", a)
print("b:", b)

# Vertical stacking
v = np.vstack((a, b))
print("\nVertical stack:\n", v)

# Horizontal stacking
h = np.hstack((a, b))
print("\nHorizontal stack:\n", h)

# Column stack (makes each vector a column)
c = np.column_stack((a, b))
print("\nColumn stack:\n", c)

# Row stack (same as vstack)
r = np.row_stack((a, b))
print("\nRow stack:\n", r)

# Concatenate
concat = np.concatenate((a, b))
print("\nConcatenate:\n", concat)
