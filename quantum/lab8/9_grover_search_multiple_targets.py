from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2 as Sampler
import matplotlib.pyplot as plt

# 3 qubit grover diffuser circuit using an explicit CCZ gate
def get_ccz_diffuser():
    qc = QuantumCircuit(3)

    qc.h([0, 1, 2])
    qc.x([0, 1, 2])
    qc.ccz(0, 1, 2)
    qc.x([0, 1, 2])
    qc.h([0, 1, 2])

    return qc


# build the oracle circuit to mart the target strings
def build_oracle(targets):
    qc = QuantumCircuit(4)

    # apply the oracle to the target stirngs
    for target in targets:
        # qiskit uses little-endian (q2 q2 q0), so we need to reverse the string
        rev_target = target[::-1]

        # apply x and MCX to the qubits where the target stirng is '0'
        for i, bit in enumerate(rev_target):
            if bit == '0':
                qc.x(i)
        qc.mcx([0, 1, 2], 3)

        # apply x gate to the qubits where the target string was '0' to restore the state
        for i, bit in enumerate(rev_target):
            if bit == '0': qc.x(i)

    return qc

# build the grover circuit with the oracle and the diffuser
def grover_circuit(oracle, k):
    qc = QuantumCircuit(4, 3)

    qc.h([0, 1, 2])
    qc.x(3)
    qc.h(3)

    diffuser = get_ccz_diffuser()

    for _ in range(k):
        qc = qc.compose(oracle)
        qc = qc.compose(diffuser, [0, 1, 2])

    qc.measure([0, 1, 2], [0, 1, 2])

    return qc

# Build the oracle and the Grover circuit
oracle = build_oracle(["000", "011", "101"])
# Calculate the number of iterations
# k = floor((pi/4) * sqrt(N/m))
# = floor((pi/4) * sqrt(8/3)) = 1
grover = grover_circuit(oracle, k=1)


# runt the circuit and print the measurement results
sampler = Sampler(seed=1234)

job = sampler.run([grover.decompose()], shots=1000)
counts = job.result()[0].data.c.get_counts()

for i in range(8):
    state = f"{i:03b}"
    if state not in counts:
        counts[state] = 0

print("results:")
for s in sorted(counts):
    # If the state is a target string, mark it visually
    marker = "<-- Target" if s in ["000", "011", "101"] else ""
    print(f"{s}: {counts[s]:4d} {marker}")
# Draw the circuit
grover.draw(output='mpl')
plt.show()