from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(1) # 1-qubit circuit
qc.h(0)                 # Create |+> state
qc.measure_all()        # Measurement

sim = AerSimulator()    # Simulator 
result = sim.run(qc, shots=1024).result() # Run the circuit on the simulator with 1024 shots
counts = result.get_counts()
print('Measurement results:', counts) 