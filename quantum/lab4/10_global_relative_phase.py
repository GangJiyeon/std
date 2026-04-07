from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

sim = AerSimulator()

# exp 1: relative phase comparision (Z-basis)
for label, use_z in [("global(|+>)", False), ("relative(|->)", True)]:
    qc = QuantumCircuit(1)
    qc.h(0)
    if use_z: qc.z(0)
    qc.measure_all()
    c = sim.run(qc, shots=1024).result().get_counts()
    print(f"Z-basis {label}:{c}")

# exp 2: X-basis (H then measure)
for label, use_z in [("H|+>", False), ("H|->", True)]:
    qc = QuantumCircuit(1)
    qc.h(0)
    if use_z: qc.z(0)
    qc.h(0)
    qc.measure_all()
    qc.h(0)
    c = sim.run(qc, shots=1024).result().get_counts()
    print(f"X-basis {label}: {c}")