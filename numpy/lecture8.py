import numpy as np

a = np.arange(5)
print("ndarray: ", a)
print("np.sum: ", np.sum(a))
print("ndarray.sum: ", a.sum())

a = np.arange(12).reshape((3, -1))
sum_ = a.sum(axis=0)

print("ndarray: {}\n{}".format(a.shape, a))
print("ndarray.sum(axis=0): {}\n{}".format(sum_.shape, sum_))

a = np.arange(12).reshape((3, -1))
sum_ = a.sum(axis=1)

print("ndarray: {}\n{}".format(a.shape, a))
print("ndarray.sum(axis=1): {}\n{}".format(sum_.shape, sum_))

sum_class = np.sum(a, axis=0)
sum_student = np.sum(a, axis=1)

# Keep dimensions

a = np.arange(12).reshape((3, -1))

sum_class = np.sum(a, axis=0, keepdims=True)
sum_student = np.sum(a, axis=1, keepdims=True)

print("scores: {}\n{}".format(a.shape, a))
print("sum_class: {}\n{}".format(sum_class.shape, sum_class))
print("sum_student: {}\n{}".format(sum_student.shape, sum_student))

n_student, n_class = 3, 4
m_score, M_score = 0, 100
scores = np.random.randint(low=m_score,
                           high=M_score,
                           size=(n_student, n_class))

mean_class = np.mean(scores, axis=0, keepdims=True)
mean_student = np.mean(scores, axis=1, keepdims=True)

print("Shapes: ")
print(scores.shape, mean_class.shape, mean_student.shape, '\n')

print("Mean substraction by classes\n", scores-mean_class)
print("Mean subtraction by students\n", scores-mean_student)

# 3rd order tensor case

a = np.arange(2*3*4).reshape((2, 3, 4))
sum_ = a.sum(axis=0, keepdims=True)

print("ndarray: {}\n{}".format(a.shape, a))
print("ndarray.sum(axis=0): {}\n{}".format(sum_.shape, sum_))

