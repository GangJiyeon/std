import random
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def bv_circuit(secret):
    n = len(secret)
    qc = QuantumCircuit(n+1, n)
    qc.x(n); qc.h(range(n+1))
    for i, b in enumerate(reversed(secret)):
        if b == '1':
            qc.cx(i, n)
    qc.h(range(n))
    qc.measure(range(n), range(n))
    return qc

random.seed(7)
sim = AerSimulator()

for _ in range(5):
    n = random.randint(4, 7)
    secret = ''.join(random.choice('01') for _ in range(n))
    counts = sim.run(bv_circuit(secret), shots=1).result().get_counts()
    found = list(counts.keys())[0]
    ok = '✓' if found == secret else 'x'
    print(f'{ok} secret={secret}, found={found}')