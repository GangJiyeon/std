from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

gates = {
    'X|0⟩': lambda qc: qc.x(0),
    'H|0⟩': lambda qc: qc.h(0),
    'SH:0⟩': lambda qc: (qc.h(0), qc.s(0)),
    'TH:0⟩': lambda qc: (qc.h(0), qc.t(0)),
}

for name, apply_gate in gates.items():
    qc = QuantumCircuit(1)
    apply_gate(qc)
    sv = Statevector(qc)
    print(f'{name} = {sv}')