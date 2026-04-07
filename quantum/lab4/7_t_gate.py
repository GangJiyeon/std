from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# compate T, T^2, T^4 application
for n_t, label in [(1, "T"), (2, "T^2=S"), (4, "T^4=Z")]:
    qc = QuantumCircuit(1)
    qc.h(0)

    for _ in range(n_t):
        qc.t(0)
    
    sv = Statevector(qc)
    print(f"{label}|+> = {sv}")