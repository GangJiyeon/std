from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(1)      # 1-qubit circuit
qc.h(0)                     # 1+> state
qc.measure_all()

sampler = StatevectorSampler()
pub = (qc,)
job = sampler.run([pub], shots=1024)
result = job.result()

data = result[0].data
counts = data.meas.get_counts()
print('measurement results:', counts)

total = sum(counts.values())
for k, v in sorted(counts.items()):
    print(f'P({k}) = {v/total:.3f}')