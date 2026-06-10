from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

secret = '1011'     # the hidden bit-string b
n = len(secret)
qc = QuantumCircuit(n+1, n)
qc.x(n); qc.h(range(n+1))
qc.barrier()

# oracle for f(x) = x . b
for i, bit in enumerate(reversed(secret)):
    if bit == '1':
        qc.cx(i, n)
qc.barrier()

qc.h(range(n))
qc.measure(range(n), range(n))

counts = AerSimulator().run(qc, shots=1).result().get_counts()
print('Measured:', counts)