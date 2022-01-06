import numpy as np

a = np.arange(6)
b = np.reshape(a, (2,3))

print("original ndarray: \n", a)
print("reshaped ndarray: \n", b, '\n')

a = np.arange(24)
b = np.reshape(a, (2, 3, 4))

print("original ndarray: \n", a)
print("reshaped ndarray: \n", b, '\n')

a = np.arange(6)
b = a.reshape((2,3)) # target array를 알고 있으면 바로 reshape 가능

a = np.random.randint(0, 100, (100,))
print(a.reshape((20, 5)).mean(axis=0).max())

# -1 in np.reshape
a = np.arange(12)
b = a.reshape((2, -1))
c = a.reshape((3, -1))
d = a.reshape((4, -1))
e = a.reshape((6, -1))

print(b.shape, c.shape, d.shape, e.shape)

a = np.arange(24)
b = a.reshape((2, 3, -1)) # -1 = 4

a = np.random.randint(0, 10, size=(2,2))

print(a)

row_vector = a.reshape(1, -1)
col_vector = a.reshape(-1, 1)

print(row_vector.shape, col_vector.shape)

# REsize 원소의 갯수를 바꿔주기 위한 API
a = np.arange(6)
b = np.resize(a, (9, ))

print("original ndarray: \n", a)
print("reshaped ndarray: \n", b, '\n')

# Flatten : tensor to vector
M = np.arange(9)
N = M.reshape((3, 3))
O = N.flatten()

print(M, '\n')
print(N, '\n')
print(O, '\n')

# copy and view
a = np.arange(5)
b = a.view()
print("Before revision: ", a)
b[0] = 100
print("After revision: ", a, '\n')

a = np.arange(5)
b = a[0:3] # In numpy, slicing means view!
print("Before revision: ", a)
b[...] = 10
print("After revision: ", a, '\n')

a = np.arange(5)
b = a.copy()
print("Before revision: ", a)
b[0] = 100
print("After revision: ", a, '\n')

# Base check!
a = np.arange(5)
b = c.copy()
c = a.view()
d = a[0:3]

print(b.base is a)
print(c.base is a)
print(d.base is a)

# Reshape : view, Resize : copy

# Astype
M = np.array([1, 2, 3], np.int8)
print(M.dtype)

N = M.astype(np.uint32)
O = M.astype(np.float32)
print(N.dtype)
print(O.dtype)

# bool dtype ndarrays
bools = np.array([True, False])
print(f"bool: \n{bools}")

bools2ints = bools.astype(np.int8)
print(f"int: \n{bools2ints}")

ints = np.array([-2, -1, 0, 1, 2])
floats = np.array([-2.5, -1.5, 0., 1.5, 2.5])

print(f"ints: \n{ints}")
print(f"floats: \n{floats}\n")

ints2bools = ints.astype(np.bool8)
print(f"ints -> bools: \n{ints2bools}")

floats2bools = floats.astype(np.float32)
print(f"floats -> bools: \n{floats2bools}\n")
