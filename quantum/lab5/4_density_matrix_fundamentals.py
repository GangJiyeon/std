from qiskit import QuantumCircuit
from qiskit.quantum_info import DensityMatrix

# pure state: |0> -> H
qc_pure = QuantumCircuit(1)
qc_pure.h(0)
dm_pure = DensityMatrix(qc_pure)

# print the density matrix
print("pure state density matrix! ")
print(dm_pure)