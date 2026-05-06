from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

circuit = QuantumCircuit(2)

# step 1: bell pair
circuit.h(0); circuit.cx(0, 1)
circuit.barrier()

# step 2: alice encodes b1 = 1, b2 = 0
b1, b2 = 1, 0
if b1: circuit.x(0)
if b2: circuit.z(0)
circuit.barrier()

# step 3: bob decodes
circuit.cx(0, 1); circuit.h(0)
circuit.measure_all()

# run the circuit on the AerSimulator
sim = AerSimulator()

# print the measurement results
print(sim.run(circuit, shots=1024).result().get_counts())

# display the circuit
print(circuit.draw(output='mpl'))
plt.show()