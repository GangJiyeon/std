from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import SamplerV2 as Sampler
import matplotlib.pyplot as plt

# create a 2-qubit Quantum Circuit
qc = QuantumCircuit(2, 1)

# applyt h gates to qubit 0 and 1
qc.h(0); qc.x(1); qc.h(1)
qc.barrier()

# oracle for f2(x) = NOT x
qc.x(0); qc.cx(0, 1); qc.x(0)
qc.barrier()

# apply H gate to qubit 0 and measure the qubits
qc.h(0)
qc.measure([0], [0])

# run the circuit on the AerSimulator
backend = AerSimulator(seed_simulator=18620123)
sampler = Sampler(backend)
job = sampler.run([qc], shots=8)
result = job.result()[0].data.c
print(result.get_counts())

# display the circuit
print(qc.draw(output='mpl'))
plt.show()
