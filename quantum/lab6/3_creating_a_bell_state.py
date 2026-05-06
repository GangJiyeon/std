from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

# create a 2-qubit Quantum circuit
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0,1)

# statevector check
sv = Statevector(circuit)
print('bell state: ', sv)

# measurement check
circuit.measure_all()
sim = AerSimulator()
counts = sim.run(circuit, shot=1024)\
    .result().get_counts()

# print the measurement results
print('counts:', counts)