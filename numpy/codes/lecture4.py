import numpy as np

scalar_np = np.array(3.14)
vector_np = np.array([1, 2, 3])
matrix_np = np.array([[1, 2], [3, 4]])
tensor_np = np.array([[[1, 2, 3],
                       [4, 5, 6]],

                      [[11, 12, 13, ],
                       [14, 15, 16]]])

"""
# About size of ndarray
ndarray.ndim
ndarray.shape
ndarray.size

# About the type and size of ndarray
ndarray.dtype
ndarray.itemsize
ndarray.nbytes
"""

# ndim : number of dimension
print(scalar_np.ndim)
print(vector_np.ndim)
print(matrix_np.ndim)
print(tensor_np.ndim)

print("shape / dimension")
print("{} / {}".format(scalar_np.shape, len(scalar_np.shape)))
print("{} / {}".format(vector_np.shape, len(vector_np.shape)))
print("{} / {}".format(matrix_np.shape, len(matrix_np.shape)))
print("{} / {}".format(tensor_np.shape, len(tensor_np.shape)))

# shape
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3]])
c = np.array([[1], [2], [3]])

print(f"a: {a.shape}\n{a}\n")
print(f"b: {b.shape}\n{b}\n")
print(f"c: {c.shape}\n{c}\n")


# size
M = np.ones(shape=(10, ))
N = np.ones(shape=(3, 4))
O = np.ones(shape=(3, 4, 5))
P = np.ones(shape=(2, 3,  4, 5, 6))

print("Size of M:", M.size)
print("Size of N:", N.size)
print("Size of O:", O.size)
print("Size of P:", P.size)

import numpy as np

M = np.arange(100)
N = np.full(fill_value=3.14, shape=(2, 3))

print(M.dtype)
print(N.dtype)
print(M)

int_np = np.array([1, 2, 3])
float_np = np.array([1., 2., 3.])

int8_np = np.array([1, 2, 3], dtype=np.int8)
int16_np = np.array([1, 2, 3], dtype=np.int16)
int32_np = np.array([1, 2, 3], dtype=np.int32)
int64_np = np.array([1, 2, 3], dtype=np.int64)

uint8_np = np.array([1, 2, 3], dtype=np.uint8)
uint16_np = np.array([1, 2, 3], dtype=np.uint16)
uint32_np = np.array([1, 2, 3], dtype=np.uint32)
uint64_np = np.array([1, 2, 3], dtype=np.uint64)

float32_np = np.array([1, 2, 3], dtype=np.float32)
float64_np = np.array([1, 2, 3], dtype=np.float64)

print("Integer: {}/{}/{}/{}".format(int8_np.dtype, int16_np.dtype, int32_np.dtype, int64_np.dtype))
print("Unsigned Integer: {}/{}/{}/{}".format(uint8_np.dtype, uint16_np.dtype, uint32_np.dtype, uint64_np.dtype))
print("Floating Point: {}/{}".format(float32_np.dtype, float64_np.dtype))
