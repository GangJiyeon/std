from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

# create a 2-qubit Quantum Circuit
qc = QuantumCircuit(2, 1)
qc.h(0)
qc.x(1); qc.h(1)

# barriers for the oracle
qc.barrier()
# >>> oracle goes here <<<
qc.barrier()

# apply h gate to qubit 0 and measure the qubits
qc.h(0)
qc.measure([0], [0])

# display the circuit
print(qc.draw(output='mpl'))
plt.show()