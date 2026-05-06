from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import SamplerV2 as Sampler

circuit = QuantumCircuit(2)

# apply H gate to qubit 0
circuit.h(0)
# apply X gate to qubit 1
circuit.x(1)
# measure the qubits
circuit.measure_all()

# run th circuit on the AerSimulator
backend = AerSimulator(seed_simulator=18620123)
sampler = Sampler(backend)
job = sampler.run([circuit], shots=1024)
result = job.result()[0].data.meas

# print the measurement results
print(result.get_counts())