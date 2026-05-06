from qiskit import QuantumCircuit, transpile

# bell state complexity
qc_bell = QuantumCircuit(2)
qc_bell.h(0); qc_bell.cx(0,1)
print(f'bell: depth = {qc_bell.depth()}')

# before/ater opt. 
# (HXH = Z on q0 => HCXHXH == HCXZ)
qc_unopt = QuantumCircuit(2)
qc_unopt.h(0); qc_unopt.cx(0, 1)
qc_unopt.h(0); qc_unopt.x(0); qc_unopt.h(0)
print(f"upoptimized dapth: {qc_unopt.depth()}")

# Only {cx,h,x}: no Z/U1 in basis 
# -> BasisTranslator cannot output Z; depth often unchanged
qc_basis = transpile(qc_unopt, basis_gates=['cx', 'h', 'x'])
print(f"After transpile(basis_gates=['cx','h','x']): depth = {qc_basis.depth()}")
print(qc_basis)

# default basis includes U1/RZ etc.: 
# optimizer can fold HXH to a phase gate (here U1(-pi) ~z)
qc_default = transpile(qc_unopt, optimization_level=3)
print(f"After transpile(-03) [defalt basis]: depth = {qc_default.depth()}")
print(qc_default)