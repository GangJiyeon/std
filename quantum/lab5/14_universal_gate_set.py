from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Operator

# CZ decomposition: CZ = H·CNOT·H
qc_cz = QuantumCircuit(2)
qc_cz.cz(0, 1)

qc_decomp = QuantumCircuit(2)
qc_decomp.h(1)
qc_decomp.cx(0, 1)
qc_decomp.h(1)
print(f'CZ==H·CX·H? {Operator(qc_decomp)}')


# Toffoli to basis gates via transpile
qc_toffoli = QuantumCircuit(3)
qc_toffoli.ccx(0, 1, 2)
qc_tr = transpile(qc_toffoli,basis_gates=['cx','h','t','s','tdg','sdg'])
print(f'Depth: {qc_toffoli.depth()} -> {qc_tr.depth()}')
print(f'Gates: {qc_toffoli.size()} -> {qc_tr.size()}')
print(qc_tr.draw())

# tdg, sdg => 네이티브 게이트