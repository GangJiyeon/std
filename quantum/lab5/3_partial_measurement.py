from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# bell state (entangled)
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)

# simulate and count results
sim = AerSimulator()

# measure only qubit 0
qc.measure(0, 0)
resuult = sim.run(qc, shots=1024).result()
print(resuult.get_counts())

# measure only qubit 1
qc.measure(1, 1)
resuult = sim.run(qc, shots=1024).result()
print(resuult.get_counts())
