from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

import matplotlib.pyplot as plt

# Create 1-qubit quantum circuit
qc = QuantumCircuit(1)

# add gates: H -> X
qc.h(0) # H gate: |0> -> |+1>
qc.x(0) # X gate: |+> -> X|+> = |+> (unchanged)

# add measurement (auto-creates classical register)
qc.measure_all()

# VIsullize circuit(ASCII)
fig = qc.draw(output="mpl")
fig.tight_layout()
plt.show()

# run 1024 shots with Aersim
sim = AerSimulator()
job = sim.run(qc,shots = 5000)
result = job.result()
counts = result.get_counts()
print("counts:", counts)