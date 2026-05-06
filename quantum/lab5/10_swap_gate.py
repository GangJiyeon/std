from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector

# swap decomposition equivalence
qc_native = QuantumCircuit(2)
qc_native.swap(0, 1)

# print the SWAP gate
print(f"1) Swap gate: ")
print(qc_native)

# decompose the SWAP gate into 3-CNOT
qc_decomp = QuantumCircuit(2)
qc_decomp.cx(0, 1); qc_decomp.cx(1,0)
qc_decomp.cx(0, 1)

# print the 3-CNOT gate
print(f"2) 3-CNOT gate: ")
print(qc_decomp)

# print the equivalence
print(f"3) SWAP == 3-CNOT? {Operator(qc_native)==Operator(qc_decomp)}")