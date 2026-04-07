import numpy as np

# define gate matrics
X = np.array([[0, 1], [1, 0]])
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]])
H = (1/np.sqrt(2)) * np.array([[1,1], [1, -1]])

# verify Y^2 = I
print("Y^2 = \n", np.round(Y @ Y, 4))

# verify Y = iXZ
print("iXZ = \n", np.round(1j * X @ X, 4))

