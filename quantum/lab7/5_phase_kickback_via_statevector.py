# phase kickback과 어떤 차이가 있는지 보고서에 꼭 작성
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

# control in |+>, ancilla in |->
qc = QuantumCircuit(2)
qc.h(0)             # control: |+>
qc.x(1); qc.h(1)    # ancilla: |->

# oracle for f(x) = x (CNOT q0 -> q1)
qc.cx(0, 1)

sv = np.round(Statevector(qc).data, 3)
print('after oracle:', sv)
# minus sign migrated to control's |1> branch

# apply H on contrl to read out the phase
qc.h(0)
print('after H on contrl: ', np.round(Statevector(qc).data, 3))
# control localized in |1> -> reveals f