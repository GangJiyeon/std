import matplotlib as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# 1. initialize n qubits to represnt 2^n state
n_qubits = 3
qc = QuantumCircuit(n_qubits)

# 2. create equal superposition (parallelism) via H-gates
qc.h(range(n_qubits))
qc.barrier()

# 3. measure to observe wavefuntion collapse
qc.measure_all()

# 4. excute simulation with 1024 shots
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

# 5. visualizatino
print("Measurement Counts:", counts)
print(qc.draw(output='text'))
plot_histogram(counts)
plt.show()