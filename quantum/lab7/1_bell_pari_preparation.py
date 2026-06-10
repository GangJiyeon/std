from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Construct the Bell state
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Verify the state vector
sv = Statevector(qc)
print('bell stateL: ', sv)

# Confirm entaglement: ad = bc != 0
a, b, c, d = sv.data
print('ad - bc = ', a*d - b*c)

