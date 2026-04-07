from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Generate 8-bit quantum random number
qc = QuantumCircuit(8)  # 8-qubit circuit 
qc.h(range(8))  # apply H gate to all qubits
qc.measure_all()

sim = AerSimulator()
result = sim.run(qc, shots=1).result()
counts = result.get_counts()
random_bits = list(counts.keys())[0]
random_int = int(random_bits, 2)
print(f"random bit string: {random_bits}")
print(f"integer value: P{random_int}(range: 0-255)")