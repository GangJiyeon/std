from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime.fake_provider import FakeProviderForBackendV2

# Fake Backend Service
FakeProvideService = FakeProviderForBackendV2

qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()

# [1] Ideal simulator (no noise)
sim_ideal = AerSimulator()
counts_ideal = sim_ideal.run(qc, shots=1024).result().get_counts()
print('ideal simulator:', counts_ideal)

# [2] Fake Backend (simulate real hw noise)
fake_backend = FakeProvideService().backend('fake_manila')
sim_noisy = AerSimulator.from_backend(fake_backend)
qc_t = transpile(qc, sim_noisy)
counts_noisy = sim_noisy.run(qc_t, shots = 1024).result().get_counts()
print('fake backend (noisy): ', counts_noisy)