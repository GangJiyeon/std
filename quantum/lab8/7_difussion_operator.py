from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate
import matplotlib.pyplot as plt

# 3 qubit grover diffuser circuit using an explicit CCZ gate
qc = QuantumCircuit(3)

# apply H to all qubit
qc.h([0, 1, 2])
# X > all
qc.x([0, 1, 2])
# CCZ > all
qc.ccz(0, 1, 2)
# X > all
qc.x([0, 1, 2])
# apply H to all qubit
qc.h([0, 1, 2])

# draw the circuit
print(qc.draw(output='mpl'))
plt.show()