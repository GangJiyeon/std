from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

# Initialize a 2-qubit Quantum Circuit
qc = QuantumCircuit(2)
qc.x(1)

# verify the statevector indexing
# little-endian means index i = binary value of the state
state = Statevector.from_instruction(qc)
print("\n--- statevector data ---")
print(state.data)

# In |10>, the binary value is 2
# Therefor, state.data[2] should be 1+0j
index_val = state.data[2]
print(f"value at index 2: {index_val} (matches state |10>)")

qc.measure_all()

backend = AerSimulator()
job = backend.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()

# verity measurement result string
print("\n --- measurement results (counts) ---")
print(counts)