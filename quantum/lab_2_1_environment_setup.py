import qiskit
import matplotlib.pyplot as plt
print('Qiskit version:', qiskit.__version__)

from qiskit import QuantumCircuit
qc = QuantumCircuit(1)  # 1-qubit circuit
qc.h(0)                 # apply h gate
qc.h(0)                 # measure all qubits
qc.measure_all()

qc.draw(output='mpl')
plt.show()