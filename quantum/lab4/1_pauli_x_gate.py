from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

# create 1-qubit circuit
qc = QuantumCircuit(1)
qc.x(0) # x gate : |0> -> |1>
qc.measure_all()

# run sim
sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
counts = result.get_counts()
print(counts)   

# VIsullize circuit(ASCII)
fig = qc.draw(output="mpl")
fig.tight_layout()
plt.show()
