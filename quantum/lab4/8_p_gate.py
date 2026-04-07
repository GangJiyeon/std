from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

sim = AerSimulator()

# phase interference: H -> P(theta) -> H -> measure
def run_phase_exp(theta, label):
    qc = QuantumCircuit(1)
    qc.h(0)             # |0> -> |+>
    qc.p(theta, 0)      # add phase e^(i*theta to |1>)
    qc.h(0)             # convert phase to amplitude (interference)
    qc.measure_all()

    counts = sim.run(qc, shots=1024).result().get_counts()
    print(f"{label}: {counts}")

# compare four angles
'''
theta = 0은 왜 이런 결과가 나올까
H 적용하면 |+> ->  -> 다시: 100프로가 나오는것
'''
run_phase_exp(0,            "theta=0    (I)")
run_phase_exp(np.pi/2,      "theta=pi/2 (S)")
run_phase_exp(np.pi,        "theta=pi   (Z)")
run_phase_exp(3*np.pi/2,    "theta=3pi/2  ")

