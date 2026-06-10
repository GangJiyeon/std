import numpy as np
import matplotlib.pyplot as plt

N, a, m = 15, 2, 3
M = 2 ** m
# build |j>|a^j mod N> superposition
state = np.zeros((M, N), dtype=complex)
for j in range(M):
    state[j, pow(a, j, N)] = 1 / np.sqrt(M)

# Marginal probability of 2nd register
prob = (np.abs(state) ** 2).sum(axis=0)
plt.bar(range(N), prob)
plt.title(f"N={N}, a={a}, m={m}")
plt.xlabel("|a^j mod N>")
plt.ylabel("probability")
plt.show()