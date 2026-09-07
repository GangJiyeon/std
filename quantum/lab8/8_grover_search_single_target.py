from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2 as Sampler
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

def get_ccz_diffuser():
    # 3 qubit grover diffuser circuit using an explicit CCZ gate
    qc = QuantumCircuit(3)

    qc.h([0, 1, 2])
    qc.x([0, 1, 2])
    qc.ccz(0, 1, 2)
    qc.x([0, 1, 2])
    qc.h([0, 1, 2])

    return qc

# build the oracle circuit to mark the target string '111'
def build_oracle(targets):
    qc = QuantumCircuit(4)
    qc.mcx([0, 1, 2], 3)
    return qc

# build the grover circuit with the oracle and the diffuser
def grover_circuit(oracle, k):
    #create a quantum circuit with 4 qubits and 3 classical bits
    qc = QuantumCircuit(4, 3)

    # initialization
    qc.h([0, 1, 2])
    qc.x(3) 
    qc.h(3) # prepare the ancilla qubit for phase kickback

    # load the diffuser with the explicit ccz
    diffuser = get_ccz_diffuser()

    # grover iterations
    for _ in range(k):
        qc = qc.compose(oracle)

        # apply the diffuser only to the 3 data qubits (0, 1, 2)
        qc = qc.compose(diffuser, [0, 1, 2])

    # measurement
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc

# build the oracle and the grover circuit and draw the circuit
oracle = build_oracle(['111'])
grover = grover_circuit(oracle, k = 2)
grover.draw(output='mpl')
plt.show()

# run the circuit and print the measurement results
sampler  = Sampler(seed=1234)
job = sampler.run([grover.decompose()], shots=100)
print("mea. results:", job.result()[0].data.c.get_couts())
