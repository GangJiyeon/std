from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def deutsch(oracle_type):
    qc = QuantumCircuit(2, 1)
    qc.x(1)         # prepare |1> on qubit 1
    qc.h([0, 1])    # hadamard both

    # oracle
    if oracle_type == 'f0': # constant 0
        pass
    elif oracle_type == 'f1': # identity
        qc.cx(0, 1)
    elif oracle_type == 'f2': # NOT
        qc.x(0); qc.cx(0, 1); qc.x(0)
    elif oracle_type == 'f3': # constant 1
        qc.x(1)
    
    # final H + measure
    qc.h(0)
    qc.measure(0, 0)
    sim = AerSimulator()
    res = sim.run(qc, shots=1).result()
    bit = list(res.get_counts().keys())[0]
    return 'constant' if bit == '0' else 'balanced'

for f in ['f0','f1','f2','f3']:
    print(f'{f}: {deutsch(f)}')