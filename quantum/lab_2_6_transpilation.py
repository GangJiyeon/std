from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1)      # h > t gate circuit
qc.h(0)
qc.t(0)
qc.measure_all()
print('Original circuit: ')
print(qc.draw())

sim = AerSimulator()
qc_transpiled = transpile(qc, sim)
print('after tranpile: ')
print(qc_transpiled.draw())

result = sim.run(qc_transpiled, shots=1024).result()
print('result: ', result.get_counts())