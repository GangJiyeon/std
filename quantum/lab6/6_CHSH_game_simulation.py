from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def chsh_quantum(x, y, shots=10000):
    qc = QuantumCircuit(2)

    # shared bell state
    qc.h(0); qc.cx(0, 1)


    # alice: roate based on x
    if x == 1: qc.ry(np.pi/2, 0)

    # bob: roate based on y
    if y == 0: qc.ry(np.pi/4, 1)
    else:       qc.ry(-np.pi/4, 1)
    qc.measure_all()

    # simulatre the circuit
    sim = AerSimulator()
    res = sim.run(qc, shots=shots).result()
    counts = res.get_counts()

    # calcultate the win rate
    if x == 1 and y == 1:
        wins = counts.get('01', 0)+counts.get('10', 0)
    else:
        wins = counts.get('00', 0)+counts.get('11', 0)
    return wins/shots

# calculate the total win rate
total = sum(chsh_quantum(x, y)
            for x in [0,1] for y in [0, 1])/4
print(f"win rate: {total:.3f}")