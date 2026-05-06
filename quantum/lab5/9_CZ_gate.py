from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector

# CZ on all basis states
for state in ['00', '01', '10','11']:
    qc = QuantumCircuit(2)
    if state[0] == '1': qc.x(1)
    if state[1] == '1': qc.x(0)

    qc.cz(0, 1)

    # print the statevector
    sv = Statevector(qc)
    print(f"|{state}> -> {sv}")