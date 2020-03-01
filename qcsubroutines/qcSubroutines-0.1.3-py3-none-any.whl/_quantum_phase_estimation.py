import qcSim as qs
import numpy as np


def quantum_phase_estimation(m, e_vec, c=5):
    """
    Algorithm to estimate the phase (or eigenvalue) of an eigenvector of a unitary operator.
    This function is used in quantum Principal Components Analysis algorithm.
    Speedup: - (no comparable classical algorithm)

    Parameters:
        m: Two-dimensional numpy array -> The unitary matrix for phase estimation.
        e_vec: One-dimensional numpy array ->  Eigenvector for which the phase should be estimated
        c: Integer -> Number of control qubits, that will later store the estimated phase (more control qubits will lead to a more accurate estimation).
    Return value: The calculated eigenvalue based on the measurements of the control qubits.
    Return type: float
    """

    # Checks whether the provided matrix is unitary
    if not np.allclose(m.dot(m.conj().T), np.eye(len(m))):
        raise ValueError('Provided matrix has to be unitary.')
    n = int(np.log2(len(m)))

    # Encoding the eigenvector as a quantum state
    e_vec_state = qs.State(e_vec)

    # Generates the operator for matrix m
    U = qs.Operator(m)

    # Adding the c control qubits, that will later store the estimated phase
    state = qs.zeros(c) * e_vec_state

    # Actual quantum algorithm for phase estimation
    h_c = qs.hadamard(c)
    state = h_c(state, qubit_ind=range(c))

    # Moving the phase of the eigenvector to the control qubits
    for i in range(c):
        U_2_i = U
        for j in range(i):
            U_2_i = U_2_i(U_2_i)
        C_U = qs.controlled_operator(U_2_i)
        state = C_U(state, qubit_ind=[(c - i - 1)] + list(range(c, c + n, 1)))

    # Controlled phase gates for inverse Quantum Fourier Transformation
    all_Rs_H = {}
    for i in range(2, c + 1, 1):
        Ri = qs.Operator([[1, 0], [0, np.exp((np.pi * 2j) / (2**i))]])
        all_Rs_H[i - 2] = qs.controlled_operator(Ri).con_trans()

    # Inverse Quantum Fourier transformation
    h_1_H = qs.hadamard().con_trans()

    for i in range(c):
        state = h_1_H(state, qubit_ind=[i])
        for j in range(c - 1 - i):
            state = all_Rs_H[j](state, qubit_ind=[i + j + 1, i])

    swap_H = qs.swap().con_trans()
    for i, j in zip(range(c), range(c - 1, -1, -1)):
        if i >= j:
            break
        state = swap_H(state, qubit_ind=[i, j])

    measurement = state.measure(qubit_ind=range(c))

    # Calculation of the estimated phase -> See Patil et al. p. 4
    estimated_phase = 0
    for i in range(c):
        estimated_phase += measurement[i] / 2**(i + 1)

    return estimated_phase
