from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

n = 3
qc = QuantumCircuit(n+1, n)
qc.x(n)
qc.h(range(n+1))
qc.barrier()

# balanced oracle: f(x) = x0 XOR x1 XOR x2
for i in range(n):
    qc.cx(i, n)
qc.barrier()

qc.h(range(n))
qc.measure(range(n), range(n))

result = AerSimulator().run(qc, shots=1024).result()
print(result.get_counts())