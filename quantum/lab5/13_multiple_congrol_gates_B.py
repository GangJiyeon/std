from qiskit import QuantumCircuit
from qiskit.circuit.library import XGate, SwapGate

# initialize a circuit with 5 qubits
# q0, q1: Controls | q2: CCNOT target | q3, q4: SWAP target
qc = QuantumCircuit(5)

# --- 1. CCNOT (TOffoli) Gate Implementation ---
# Built-in method
qc.ccx(0, 1, 2)
qc.x(3)

# --- 2. C-SWAP (Fredkin) Gate Implementation ---
# Built-in method: q0 controls the swap betwenn q3 and q4
qc.cswap(0, 3, 4)
qc.barrier()

qc.x(0)
qc.x(1)

# --- 3. Implementation via .control() method ---
# Creating a CCNOT (2 controls) from an X gate
custom_toffoli = XGate().control(2)
qc.append(custom_toffoli, [0, 1, 2])

# Creating a C-SWAP (1 control) from a Swap gate
custom_fredkin = SwapGate().control(1)
qc.append(custom_fredkin, [0, 3, 4])


print("intergrated multi-control circuit:")
print(qc.draw(output='text'))
qc.measure_all()
