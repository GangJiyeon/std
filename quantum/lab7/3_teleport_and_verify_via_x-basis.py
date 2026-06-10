from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Prepare |+> on q0, then teleport
qc = QuantumCircuit(3, 1)
qc.h(0)     # |psi> = |+>
qc.h(1); qc.cx(1, 2)    # bell pair (q1, q2)
qc.cx(0, 1); qc.h(0)    # alice: CNOT + H

# Bob's correcions (deferred measurement)
qc.cx(1, 2); qc.cz(0, 2)

# X-basis measurement on Bob
qc.h(2)
qc.measure(2, 0)

counts = AerSimulator().run(qc, shots=1024).result().get_counts()
print('X-basis on Bob: ', counts)