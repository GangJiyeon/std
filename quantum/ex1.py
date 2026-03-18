from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2)
qc.h(0)         # 중첩게이트
qc.cx(0, 1)     # 얽힘게이트
qc.measure_all()

sampler = StatevectorSampler()
result = sampler.run([qc], shots=1024).result() # shots=1024로 측정 횟수 설정
print(result[0].data.meas.get_counts())