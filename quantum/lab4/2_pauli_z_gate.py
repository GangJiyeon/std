from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# experiment 1: apply Z to |0>
qc1 = QuantumCircuit(1)
qc1.z(0)
qc1.measure_all()

# experiment 2: |+> with Z (H -> Z -> H -> measurement)
qc2 = QuantumCircuit(1)
qc2.h(0)
qc2.z(0)
qc2.h(0)
qc2.measure_all()

# experiment 3: 
qc3 = QuantumCircuit(1)
qc3.h(0)
qc3.x(0)
qc3.h(0)
qc3.measure_all()

qc4 = QuantumCircuit(1)
qc4.x(0)
qc4.measure_all()

sim = AerSimulator()
c1 = sim.run(qc1, shots = 1024).result().get_counts()
c2 = sim.run(qc2, shots = 1024).result().get_counts()
c3 = sim.run(qc3, shots = 1024).result().get_counts()
c4 = sim.run(qc4, shots = 1024).result().get_counts()

print('exp1 z|0>: ', c1)
print('exp2 HZH|0>: ', c2)
print('exp3 HXH|0>: ', c3)
print('exp4 X|0>: ', c4)

