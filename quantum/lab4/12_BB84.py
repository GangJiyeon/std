import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

'''
# BB84: Alice sends bits in random bases, 
  Bob measure in random bases
'''
n = 100
sim = AerSimulator()
alice_bits = np.random.randint(0, 2, n)
alice_bases = np.random.randint(0, 2, n)
bob_bases = np.random.randint(0, 2, n)
bob_results = []

# Encode, measure, record
for i in range(n):
    qc = QuantumCircuit(1, 1)
    if alice_bits[i] == 1: qc.x(0)
    if alice_bases[i] == 1: qc.h(0) # alice: Z or X basis
    if bob_bases[i] == 1: qc.h(0)   # bob: measure in Z or X
    qc.measure(0, 0)
    r = sim.run(qc, shots=1).result()
    bob_results.append(int(list(r.get_counts().keys())[0]))

match = alice_bases == bob_bases # same basis -> correct bit
key_a = alice_bits[match]
key_b = np.array(bob_results)[match]
print(f"key lenght: {sum(match)}")