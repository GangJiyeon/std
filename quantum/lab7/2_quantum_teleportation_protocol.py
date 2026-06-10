from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(3, 2)

# prepare |+> on q0
qc.h(0)

# bell pair on (q1, q2)
qc.h(1); qc.cx(1, 2)
qc.barrier()

# alice: CNOT + H, measure
qc.cx(0, 1); qc.h(0)
qc.measure([0, 1], [0, 1])
qc.barrier()

# bob: conditional corrections
with qc.if_test((qc.cregs[0][1], 1)):
    qc.x(2)
with qc.if_test((qc.cregs[0][0], 1)):
    qc.z(2)

# save statevector before measurement
qc.save_statevector()

sim = AerSimulator()
result = sim.run(qc.decompose(), shots=1).result()

# bob's statevector
sv = result.get_statevector()
print('Bob statevector:', sv)

counts = result.get_counts()
print('counts:', counts)