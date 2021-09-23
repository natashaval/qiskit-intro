import numpy as np
from qiskit import QuantumCircuit
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram

circuit = QuantumCircuit(2,2) # 2 qubits and 2 classical bits
circuit.h(0)
circuit.cx(0,1)
circuit.draw()