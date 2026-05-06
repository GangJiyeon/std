from qiskit.quantum_info import DensityMatrix, state_fidelity
import numpy as np

# 1. define a pure bell state: (|00> + |11>) / sqrt(2)
rho_pure = DensityMatrix([
    [0.5,   0,      0,      0.5],
    [0,     0,      0,      0  ],
    [0,     0,      0,      0  ],
    [0.5,   0,      0,      0.5]
])

# 2 -> 1,4  4,1 일부러 노이즈를 주기위해 0으로 바꿈
# 2. define a mixed state: 50% |00><00| + 50% |11><11|
rho_mixed = DensityMatrix([
    [0.5,   0,      0,      0 ],
    [0,     0,      0,      0 ],
    [0,     0,      0,      0 ],
    [0,     0,      0,      0.5]
])

# calculate purity(Tr(rho^2))
purity_pure = rho_pure.purity()
purity_mixed = rho_mixed.purity()

print("---pure bell state---")
print(f"purity: {purity_pure.real}") # should be 1.0

print("\n---mixed state---")
print(f"purity: {purity_mixed.real}") # should be 0.5