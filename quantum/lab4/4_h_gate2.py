from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# create superposition with H gate
qc = QuantumCircuit(1)
qc.x(0) # |1>
qc.h(0) # |1> -> |-1>
qc.measure_all()

# run sim
sim = AerSimulator()
results = sim.run(qc, shots = 1024).result()
counts = results.get_counts()
print(qc.draw())
print(counts)

