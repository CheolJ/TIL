import numpy as np

int_py = 3
float_py = 3.14

int_np = np.array(int_py)
float_np = np.array(float_py)

print("integer case")
print(type(int_py), type(int_np))
print(int_py, int_np, sep=' - ')

print("Floating point case")
print(type(float_py), type(float_np))
print(float_py, float_np, sep=' - ')

# Making Vector ndarrays

vec_py = [1, 2, 3]
vec_np = np.array(vec_py)

print(type(vec_py), type(vec_np))
print(vec_py, vec_np, sep=' - ')

# Making Matrix ndarrays
mat_py = [[1, 2, 3],
          [4, 5, 6]]
mat_np = np.array(mat_py)

print(type(mat_py), type(mat_np))
print(mat_py, mat_np, sep='\n\n')

# Making 3rd Order Tensor ndarrays
tensor_py = [[[1, 2, 3],
              [4, 5, 6]],
             [[11, 12, 13],
              [14, 15, 16]]]

tensor_np = np.array(tensor_py)
print(type(tensor_py), type(tensor_np))
print(tensor_py, tensor_np, sep='\n\n')

# Making ndarrays with Fixed Intervals
print(list(range(10)))
print(list(range(2, 5)))
print(list(range(2, 10, 2)))

# same as list but type is ndarray
print(np.arange(10))
print(np.arange(2, 5))
print(np.arange(2, 10, 2))

# Float type is available
print(np.arange(10.5))
print(np.arange(1.5, 10.5))
print(np.arange(1.5, 10.5, 2.5))


# ndarrays with Specific Values
np.zeros(shape=(2, 3))
np.ones(shape=(2, 3))
np.full(shape=(2, 3), fill_value=3.14)

M = np.full(shape=(2, 3), fill_value=3.14)

print(M, '\n')
zeros_like = np.zeros_like(M)
ones_like = np.ones_like(M)
full_like = np.full_like(M, fill_value=100)
empty_like = np.empty_like(M)

print("zeros_like: \n", zeros_like, '\n')
print("ones_like: \n", ones_like, '\n')
print("full_like: \n", full_like, '\n')
print("empty_like: \n", empty_like, '\n')

# linear space
print(np.linspace(0, 1, 5)) # include start and end number
a = np.linspace([1, 10, 100], [2, 20, 200], 5)
print(a)

# random distribution
