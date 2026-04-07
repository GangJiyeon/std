from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# apply S gate and chek state
qc = QuantumCircuit(1)
qc.h(0) # crate |+>
qc.s(0) # apply S gate
sv = Statevector(qc)    # 실제로 어떤 상태인지 확인
print("S|+>: ", sv)

# verify S^2 = Z
qc2 = QuantumCircuit(1)
qc2.h(0)
qc2.s(0)
qc2.s(0)    # apply S 2 times
sv2 = Statevector(qc2)
print("S^2|+>", sv2)

qc3 = QuantumCircuit(1)
qc3.h(0)
qc3.z(0)
sv3 = Statevector(qc3)
print("Z|+>: ", sv3)

