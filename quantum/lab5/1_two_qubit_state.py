from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# create 2-qubit circuit
qc = QuantumCircuit(2)

# default state: |00>
sv_default = Statevector(qc)
print(sv_default)

# apply gates and measute states
qc_x = QuantumCircuit(2)
qc_x.x(0)   # |01> state
sv_x = Statevector(qc_x)
print(sv_x)
