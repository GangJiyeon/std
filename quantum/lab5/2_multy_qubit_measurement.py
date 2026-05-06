from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# bell state 1번재랑 3번째 출력하기 - 숙제! (x게이트 등등 써서 코드로)
# bell state(entangled) / # bell state 1번
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# bell state 3번
qc1 = QuantumCircuit(2)
qc1.h(0)
qc1.cx(0, 1)
qc1.x(1)

# measure all qubits
qc.measure_all()
qc1.measure_all()

# simulate and count results
sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
result1 = sim.run(qc1, shots=1024).result()

# print the results
print(f"1번 bell state: {result.get_counts()}")
print(f"3번 bell state: {result1.get_counts()}")
