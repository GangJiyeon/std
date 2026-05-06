from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

def superdense_enc_and_dec(msg):
    qc = QuantumCircuit(2)
    # q_0 = Alice's qubit, q_1 = Bob's qubit
    # Create Bell state
    qc.h(0)
    qc.cx(0, 1)
    
    # Alice encodes (b1, b0)
    b1, b0 = int(msg[0]), int(msg[1])
    if b0 == 1: qc.z(0) # X gate
    if b1 == 1: qc.x(0) # Z gate
    qc.barrier()

    # print statevector
    print(Statevector.from_instruction(qc))

    # Bob decodes
    qc.cx(0, 1)
    qc.h(0)
    qc.measure_all()
    return qc

sim = AerSimulator()
for msg in ['00','01','10','11']:
    qc = superdense_enc_and_dec(msg)
    r = sim.run(qc, shots=1024).result()
    print(f'{msg} -> {r.get_counts()}')