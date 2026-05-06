from qiskit import QuantumCircuit
from qiskit.circuit.library import XGate

# basic conrolled gates
qc_cx = QuantumCircuit(2)
qc_cx.cs(0, 1)

print(f"1) C-X gate: ")
print(qc_cx)

# C-X gate using control() method
x_gate = XGate()
c_x = x_gate.control(1)
qc_x = QuantumCircuit(2)
qc_x.append(c_x, [0, 1])

print(f"2) C-X Gate:")
print(qc_x)