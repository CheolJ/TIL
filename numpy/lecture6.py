import numpy as np

a = np.random.randint(1, 5, (5, ))
b = np.random.randint(1, 5, (5, ))

print("a: ", a)
print("b: ", b)

print("a + b: ", a + b)
print("a - b: ", a - b)
print("a * b: ", a * b)
print("a / b: ", a / b)
print("a // b: ", a // b)
print("a % b: ", a % b)
print("a ** b: ", a ** b)

print("a > b: ", a > b)
print("a >= b: ", a >= b)
print("a < b: ", a < b)
print("a <= b: ", a <= b)
print("a == b: ", a == b)
print("a != b: ", a != b)

# Remember!
# the shape of array should be same!


# Broadcasting
a = np.array([[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]])

b = np.array([0, 10, 20])
c = np.array([[0], [1], [2]])

A = np.arange(9).reshape(3, 3)
B = 10 * np.arange(3).reshape((-1,3))
C = A + B

# ndim : number of dimension
print("A: {}/{}\n{}".format(A.ndim, A.shape, A))
print("B: {}/{}\n{}\n".format(B.ndim, B.shape, B))
# calculation with broadcasting
print("A + B: {}/{}\n{}".format(A.ndim, C.shape, C))

A = np.arange(9).reshape(3, 3)
B = 10 * np.arange(3).reshape((3, -1))
C = A + B

# ndim : number of dimension
print("A: {}/{}\n{}".format(A.ndim, A.shape, A))
print("B: {}/{}\n{}\n".format(B.ndim, B.shape, B))
# calculation with broadcasting
print("A + B: {}/{}\n{}".format(A.ndim, C.shape, C))

A = np.arange(3).reshape((3, -1))
B = np.arange(3).rehsape((-1, 3))
C = A + B

print("A: {}/{}\n{}".format(A.ndim, A.shape, A))
print("B: {}/{}\n{}".format(B.ndim, B.shape, B))

print("A + B: {}/{}\n{}".format(A.ndim, C.shape, C))


# Broadcasting : Second Dimension ndarray
A = np.arange(18).reshape((2, 3, 3))
B = 10 * np.arange(9).reshape((1, 3, 3))

print("A: {}/{}\n{}".format(A.ndim, A.shape, A))
print("B: {}/{}\n{}".format(B.ndim, B.shape, B))

print("A + B: {}/{}\n{}".format(A.ndim, C.shape, C))

a = np.array(3)
u = np.arange(5)
print("shapes: {}/{}".format(a.shape, u.shape))
print("a: ", a)
print("u: ", u, '\n')

print("a*u: ", a*u)
