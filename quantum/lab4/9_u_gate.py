from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
import numpy as np

sim = AerSimulator()

# reproduce H gate as U(pi/2, 0, pi)
qc_h = QuantumCircuit(1)
qc_h.u(np.pi/2, 0, np.pi, 0)
sv_h = Statevector(qc_h)
print("U(pi/2, 0, pi)|0> =  ", sv_h.data.round(3))

# reproduce X gate as U(pi, 0, pi)
qc_x = QuantumCircuit(1)
qc_x.u(np.pi, 0, np.pi, 0)
sv_x = Statevector(qc_x)
print("U(pi, 0, pi)|0> =    ", sv_x.data.round(3))

# measure to verify distributino (U=H except 50/50)
qc_h.measure_all()
counts = sim.run(qc_h, shots=1024).result().get_counts()
print("counts: ", counts)