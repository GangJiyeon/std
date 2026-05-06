from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

# apply CNOT to all basis states
for state in ['00', '01', '10', '11']:
    qc = QuantumCircuit(2)
    if state[0] == '1': qc.x(1)
    if state[1] == '1': qc.x(0)

    # apply CNOT
    qc.cx(0, 1)
    sv = Statevector(qc)
    print(f"|{state}> -> {sv}")