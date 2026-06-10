from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
import numpy as np

# QFT function
def qft(m):
    qc = QuantumCircuit(m)

    # apply Hadamard gate to exch qubit
    for i in range(m):
        qc.h(i)
        for j in range(i + 1, m):
            # apply controlled phase gate
            qc.cp(np.pi / 2 ** (j - i), j, i)
        qc.barrier()
    
    # swap qubits to get the correct order
    for i in range(m // 2):
        qc.swap(i, m - i - 1)
    return qc

# create a 3-qubit QFT circuit
qft3 = qft(3)

# display and save circuit diagram
fig = qft3.draw(output = "mpl")
fig.tight_layout()
plt.show(block=True)