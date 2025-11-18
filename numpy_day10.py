import numpy as np

# Random integer 0–9
print("randint:", np.random.randint(0, 10))

# Random float between 0 and 1
print("rand:", np.random.rand())

# Random 1D array
print("rand array:", np.random.rand(5))

# Random matrix
print("rand matrix:\n", np.random.rand(2, 3))
np.random.seed(42)
print(np.random.rand(3))


# Normal Distribution (mean=0, std=1)
print("normal:", np.random.randn(5))

# Uniform Distribution (0 to 1)
print("uniform:", np.random.uniform(0, 1, 5))


arr = np.array([1, 2, 3, 4, 5])

np.random.shuffle(arr)
print("Shuffled:", arr)

print("Permutation:", np.random.permutation(arr))


x = np.array([10, 20, 30, 40, 50])
print("min:", x.min())
print("max:", x.max())
print("mean:", x.mean())
print("std:", x.std())
print("var:", x.var())
print("median:", np.median(x))
