from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

# Toffoli truth table for all 8 basis states
for i in range(8):
    # Get the basis state
    c0=(i>>2)&1; c1=(i>>1)&1; t=i&1
    
    # Create the QuantumCircuit
    qc = QuantumCircuit(3)
    if c0: qc.x(0)
    if c1: qc.x(1)
    if t: qc.x(2)
    qc.ccx(0, 1, 2)
    
    # Print the Statevector
    # 출력 순서가 바뀜 > 잘 나오게 고쳐서 제출하기
    sv = Statevector(qc)
    out = list(sv.probabilities_dict())[0]
    print(f'|{t}{c1}{c0}> -> |{out}>')