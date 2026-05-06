from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Operator
from qiskit_aer import AerSimulator

controls = QuantumRegister(3, 'c')
ancilla = QuantumRegister(1, 'a')
target = QuantumRegister(1, 't')
qc = QuantumCircuit(controls, ancilla, target)

# apply x gates to the control qubits
for i in range(3):
    qc.x(controls[i])

# conpute the Toffoli gate
qc.ccx(controls[0], controls[1], ancilla[0])
qc.ccx(controls[2], controls[0], target[0])

# uncompute the Toffoli age
qc.ccx(controls[0], controls[1], ancilla[0])

# measure the qubits
qc.measure_all()

# simulate the circuit
simlator = AerSimulator()
job = simlator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()
print(counts)
