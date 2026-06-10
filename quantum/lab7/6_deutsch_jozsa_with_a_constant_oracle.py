from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

n = 3
qc = QuantumCircuit(n + 1, n)
qc.x(n)
qc.h(range(n+1))
qc.barrier()

# constant-0 oracle: do nothing
qc.id(n)
qc.barrier()

qc.h(range(n))
qc.measure(range(n), range(n))
result = AerSimulator().run(qc, shots=1024).result()
print(result.get_counts())