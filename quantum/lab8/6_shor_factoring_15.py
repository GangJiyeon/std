import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# inverse quantum fourier transform (IQFT)
def iqft(n):
    qc = QuantumCircuit(n, name="IQFT")

    # phase extraction
    for j in range(n - 1, -1, -1):
        for m in range(n - 1, j, -1):
            qc.cp(-np.pi / (2**(m - j)), m, j)
        qc.h(j)

    # swap to align with qiskit-s measurement order
    for i in range(n // 2):
        qc.swap(i, n - 1 - 1)
    return qc

# hardcoded 7 mod 15 operator
def c_7mod15(power):
    '''circuit specifically tailored to perform only 7^power mod 15'''
    U = QuantumCircuit(4)
    for _ in range(power):
        # gate combination that produces the effect of multiplying by 7
        U.swap(0, 1)
        U.swap(1, 2)
        U.swap(2, 3)
        U.x(range(4))
    return U.to_gate(label=f"7^{power} mod 15").control()

# total 8 qubits (4 counting + 4 target), 4 classical bits
qc = QuantumCircuit(8, 4)

# h gates on counting qubits (0-3), x gate on target qubit(4)
qc.h(range(4))
qc.x(4)
# Append 7^(2^q) mod 15 gate to each counting qubit
for q in range(4):
    qc.append(c_7mod15(2**q), [q, 4, 5, 6, 7])

# Apply IQFT to counting qubits
qc.append(iqft(4), range(4))
# Measure the 4 counting qubits and store in classical bits
qc.measure(range(4), range(4))
# Simulation Execution & Output
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)

print("Measurement Results (Counts):")
print(job.result().get_counts())