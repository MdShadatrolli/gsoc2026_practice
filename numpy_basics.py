import numpy as np

print("=== SHAPE & RESHAPE ===")
arr = np.arange(12)
print("Original:", arr)
print("Reshaped:\n", arr.reshape(3,4))

print("\n=== INDEXING ===")
a = np.array([[10,20,30],[40,50,60],[70,80,90]])
print("Element [0,1]:", a[0,1])
print("Column 1:", a[:,1])
print("Row 1:", a[1,:])

print("\n=== VECTORIZED OPS ===")
x = np.array([1,2,3])
y = np.array([10,20,30])
print("x+y:", x+y)
print("x*y:", x*y)
print("sqrt(y):", np.sqrt(y))

print("\n=== BROADCASTING ===")
m = np.array([[1,2,3],[4,5,6]])
v = np.array([10,20,30])
print("m+v:\n", m+v)
