import matplotlib.pyplot as plt
import numpy as np
import math as m

# 1
vector = np.array(np.linspace(0, 20, 21))
for i in range(9, 16):
    vector[i] = - vector[i]
print(vector)

# 2
vector = np.array(np.linspace(15, 55, 41))
print("[ ", end="")
for i in range(1, vector.shape[0] - 1):
    print("{}".format(vector[i]), end=" ")
print(" ]", end="")

# 3 
matrix = np.random.random((3, 4))
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        print(matrix[i, j], end=" ")
        
# 4
matrix = np.random.randint(5, 50, (3, 4))
print(matrix)

# 5
vector = 10 * np.random.random(5)
print(vector)

# 6
def multiply_vector(u, v):
    if u.shape[0] != v.shape[0]: pass
    r = 0
    for i in range(u.shape[0]):
        r += u[i] * v[i]
    return r
print(multiply_vector(np.random.random(5), np.random.random(5)))

# 7
matrix = np.random.randint(10, 21, (3, 4))
print(matrix)

# 8
def column_and_row(x):
    return np.array([x.shape[0],x.shape[1]])
print(column_and_row(np.random.randint(5, 50, (3, 4))))

# 9
matrix = np.zeros((4, 4))
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if (i + j)%2 == 0:
            matrix[i, j] = 0
        else:
            matrix[i, j] = 1
print(matrix)

# 10
matrix1 = np.array([0, 10, 20, 40, 60])
matrix2 = np.array([10, 30, 40])
same = []
for i in range(matrix1.shape[0]):
    for j in range(matrix2.shape[0]):
        if matrix1[i] == matrix2[j]:
            same.append(matrix1[i])
print(np.array(same))

# 11
matrix = np.array([[1, 1],[2, 3]])
unique = []
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i, j] not in unique:
            unique.append(matrix[i, j])
print(unique)

matrix = np.array([10, 10, 20, 20, 30, 30])
unique = []
for i in range(matrix.shape[0]):
    if matrix[i] not in unique:
        unique.append(matrix[i])
print(unique)

# 12
vector1 = np.array([10, 30, 40])
vector2 = np.array([15, 35, 45])
print(np.array([vector1[1] * vector2[2] - vector1[2] * vector2[1],
                vector2[0] * vector1[2] - vector2[2] * vector1[0],
                vector1[0] * vector2[1] - vector1[1] * vector2[0]]))

# 13
matrix_cart = np.random.random((10, 2))
matrix_pol = np.zeros((10, 2))
for i in range(matrix_cart.shape[0]):
    matrix_pol[i, 0] = m.sqrt(matrix_cart[i, 0] ** 2 + matrix_cart[i, 1] ** 2)
    matrix_pol[i, 1] = m.atan(matrix_cart[i, 1] / matrix_cart[i, 0])
print(matrix_pol)

# 14
vector = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
val = 34.99062268928913
closest = 0
diff = 1000
for i in range(vector.shape[0]):
    if diff >  abs(vector[i] - val):
        diff = abs(vector[i] - val)
        closest = vector[i]
print(closest)
        