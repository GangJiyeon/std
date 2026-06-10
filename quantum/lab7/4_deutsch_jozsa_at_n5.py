from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def dj_circuit(oracle, n = 5):
    qc = QuantumCircuit(n + 1, n)
    qc.x(n); qc.h(range(n + 1))
    oracle(qc, n)
    qc.h(range(n))
    qc.measure(range(n), range(n))
    return qc

# constant-1 oracle
const = lambda qc, n: qc.x(n)

# balanced oracle f(x) = x2
bal = lambda qc, n: qc.cx(2, n)

sim = AerSimulator()
for name, ora in [('constant', const), ('balanced', bal)]:
    out = sim.run(dj_circuit(ora), shots=1).result().get_counts()
    print(f'{name:9s}: {out}')