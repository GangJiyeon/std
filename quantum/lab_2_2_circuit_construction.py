from qiskit import QuantumCircuit    
import matplotlib.pyplot as plt # Importing the pyplot module from the matplotlib library for plotting

qc = QuantumCircuit(1)  # Creating a quantum circuit with 1 qubit
qc.h(0) # Applying the Hadamard gate to the first qubit (index 0)
qc.t(0) # Applying the T gate to the first qubit (index 0)
qc.s(0) # Applying the S gate to the first qubit (index 0)
qc.z(0) # Applying the Z gate to the first qubit (index 0)
qc.measure_all()   # Adding measurement operations to all qubits in the circuit

fig = qc.draw(output="mpl") # Drawing the quantum circuit using the matplotlib output format and storing the figure in the variable 'fig'
fig.tight_layout()          # Adjusting the layout of the figure to make it more compact and visually appealing
print(f'Gate count: {qc.size()}') # Printing the total number of gates in the quantum circuit using the size() method
print(f'Depth: {qc.depth()}')   # Printing the depth of the quantum circuit using the depth() method, which indicates the longest path from input to output in terms of gate layers

plt.show()                  # Displaying the figure containing the drawn quantum circuit