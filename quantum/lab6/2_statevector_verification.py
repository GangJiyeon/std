from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.x(1)

state = Statevector(circuit)
print(state)

# confirm bit-reversal
for i, amp in enumerate(state.data):
    if abs(amp) > 1e-9:
        print(f'index {i} = '
              f'{format(i, "02b")}: {amp:.4f}')