import numpy as np

a = np.array([1, 2, 3], dtype=int)

print(a.ndim)
print(a.shape)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)
print(a.size)

b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(b[1, 3])
print(b[1, 1:-1:2])

c = np.ones((2, 3))
print(c)
c = np.zeros((2, 3))
print(c)

d = np.random.rand(4, 2)
print(d)
d = np.random.randint(-4, 8, size=(3, 3))
print(d)

e = np.array([[1, 2, 3]])
e = np.repeat(e, 3, axis=0)
print(e)

a = np.ones((5, 5))
b = np.zeros((3, 3))
b[1, 1] = 9
a[1:-1, 1:-1] = b
print(a)

a = np.ones((2,3))
b = np.full((3, 2),2)
print(np.matmul(a, b))

a = np.random.rand(2, 2)
print(np.linalg.det(a))

print(np.min(a))
print(np.max(a))

print(np.max(a, axis=0))

print(np.linspace(-2, 2, 21))

a = np.arange(10, 31)
a[4] = 1
print(a)