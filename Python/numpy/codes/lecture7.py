import numpy as np

a = np.arange(10)
print(f"ndarray: \n{a}\n")
print("a[0:3] : , ", a[0:3])
print("a[3:7] :, ", a[3:7])
print("a[5:-1]", a[5:-1])

# Indexing & Slicing
a = np.arnage(10)
print(f"ndarray: \n{a}\n")

print("a[7:2:-1] : ", a[7:2:-1])

print("a[::-1] : ", a[::-1])

print("a[8:3:-2] : ", a[8:3:-2])

a = np.arange(12).reshape((4, 3))
print(f"ndarray: \n{a}\n")

print("a[1: 0] : ", a[1:, 0])

a = np.arange(16).reshape(4, 4)
print(f"ndarray: \n{a}\n")
print("a[1:3, 1:3] : \n", a[1:3, 1:3])

image = np.arnage(9).reshape((3, 3))
print(f"ndarray: \n{image}\n")

horizontal_flip = image[:, ::-1]
print(f"horizontal_flip : \n{horizontal_flip}\n", horizontal_flip)

a = np.arange(16).reshape((4, 4))
print(f"ndarray: \n{a}\n")

print("a[0, :] : \n", a[0, :])
print("a[0, ...] : \n", a[0, ...])

# 3rd order tensor ndarrays
a = np.arange(27).reshape((3, 3, 3))

np.random.normal(size=(32, 100, 100))
print("image set: ", image.shape)

a = np.arange(10)
print(f"ndarray: \n{a}\n")

indices = np.array([0, 3, 4])
print(a[indices])

# indices in ndarray
# 각 원소의 "위치"에 해당하는 원소를 가지고 온다
a = np.random.randint(0, 20, (10, ))
print(f"ndarray: \n{a}\n")

indices = np.random.randint(0, 10, size=(2, 3, 4))
print(f"indices: \n{indices}")
print(f"a[indices]: \n{a[indices]}")

# 각 위치에 해당하는 원소를 가져오다보니 a[0], a[2]에 해당하는 값을 가져오게 된다.
a = np.arange(12).reshape((3, 4))
print(f"ndarray: \n{a}\n")

indices = np.array([0, 2])
print(f"indices: \n{indices}")
print(f"a[indices]: \n{a[indices]}")

a = np.arange(12).reshape((3, 4))

indices0, indices1 = np.array([0]), np.array([1])
print(a[indices0, indices1])

indices0, indices1 = np.array([1]), np.array([2])
print(a[indices0, indices1])

indices0, indices1 = np.array([-1]), np.array([2])
print(a[indices0, indices1])

indices0 = np.array([[0, 1, 2], [0, 1, 2]])
indices1 = np.array([[0, 1, 2], [1, 2, 3]])

print("Paired indices")
for row_indices0, row_indices1 in zip(indices0, indices1):
    for idx0, idx1 in zip(row_indices0, row_indices1):
        print(f"({idx0}, {idx1})", end=' ')
    print()

print(f"a[indices0, indices1]: \n{a[indices0, indices1]}")

# Boolean_indexing
a = np.arange(5)
print(f"ndarray: \n{a}\n")

b_indices = np.array([True, False, True, False, True])
print(a[b_indices])

