from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
import matplotlib.pyplot as plt
import numpy as np

# QFT function
def qft(m):
    qc = QuantumCircuit(m)
    for i in range(m):
        qc.h(i)
        for j in range(i + 1, m):
            qc.cp(np.pi / 2 ** (j - i), j, i)
        qc.barrier()

    for i in range(m//2):
        qc.swap(i, m - i - 1)
    return qc

# IQFT function
def iqft(m):
    qc = QuantumCircuit(m)
    # swap qubits to get the correct order
    for i in range(m // 2):
        qc.swap(i, m - i - 1)

    # apply controlled pahse gate
    for i in range(m - 1, -1, -1):
        for j in range(m - 1, i, -1):
            qc.cp(-np.pi / 2 **  (j - i), j, i)
        qc.h(i)
    return qc

# verify QFT · IQFT = I (should be identity)
m = 3; M = Operator(qft(m).compose(iqft(m))).data

# display the reuslt
plt.imshow(np.abs(M), vmin=0, vmax=1, cmap='Blues')
plt.title("QFT · IQFT (should be identity)")
plt.show()