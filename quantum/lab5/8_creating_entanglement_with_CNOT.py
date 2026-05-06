from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

# bell state with H + CNOT
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# print the statevector - 측정전에 프린트한 이유는 모든 상태 다 보려고
sv = Statevector(qc)
print(f"bell state: {sv}")

# measure the qubits
qc.measure_all()

# print the counts
result = AerSimulator().run(qc, shots=1024).result()
print(f"counts: {result.get_counts()}")