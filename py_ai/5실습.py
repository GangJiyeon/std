import numpy as np

# 1
ftemp = [63, 73,80, 86, 84, 78, 66, 54, 45, 63]
F = np.array(ftemp)
print(F)

# 2
arr1 = np.array([[1, 2, 3], [2, 3, 4], [9, 8,0]])
print(arr1)
print(arr1[1][2])

# 3
a = np.arange(1, 20+1, 2)
print(a)

# 4
b = np.linspace(1, 20+1, 3)
print(b)

# 5
c = np.logspace(np.log10(10), np.log10(100), 5)
print(c)
d = np.logspace(1, 2, 5)
print(d)

# 6
e = np.random.random()
e2= np.random.random((4, 4))
print(f"e= {e}")
print(e2)

# 7
f1 = np.random.randint(1, 10)
print(f"f1 = {f1}")
f2 = np.random.randint(1, 10, (2, 2))
print(f"f2 = {f2}")

# 8
rand1 = np.random.rand(3, 3)
print(f"rand = {rand1}")

# 9
randn = np.random.randn(3, 3)
print(f"randn = {randn}")

# 10
arr_ = np.arange(1, 5+1, 1)
print(arr_)
print(f"ndim = 배열차원수 {arr_.ndim}")
print(f"shape = {arr_.shape}")
print(f"size = {arr_.size}")
print(f"dtype = {arr_.dtype}")
print(f"itemsize = {arr_.itemsize}")
print(f"nbyte = {arr_.nbytes}")

# 11
axis_ = np.arange(9)
print(axis_[-1])
axis_[2] = 9
print(axis_)
print(axis_[0:3+1:2])

# 12
axis2 = np.arange(9).reshape(3, 3)
print(axis2)
print(axis2[2][1])
axis2[0][0] = 10
print(axis2)

# 13
axis3 = np.arange(1, 25).reshape((4, 6))
print(axis3[1])
print(axis3[1:3, 1:5])
print(axis3[::-1, ::-1])

# 