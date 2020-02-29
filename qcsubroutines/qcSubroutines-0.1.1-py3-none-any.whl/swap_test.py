import qcSim as qs


def swap_test(state1, state2):
    """
    Calculates  the overlap or fidelity |⟨a| b⟩| of two quantum states |a⟩ and |b⟩. The fidelity is a 'measurement of the similarity' of these two quantum states.
    If measuring the first qubit results in the state |0⟩ with a probability of 1, then states |a⟩ and |b⟩ are identical.
    If both states do not overlap at all (in other words, they are orthogonal), the measurement of the first qubit will show the result of 0 with a probability of 1/2.
    The swap test is an important calculation step in the bist_calc subroutine.
    Source: Aïmeur, Brassard, Gambs - Machine learning in a quantum world (2006)
    Speedup: No speedup.

    Parameters:
        state1: State -> State 1 for which the fidelity should be calculated.
        state2: State -> State 2 for which the fidelity should be calculated.
    Return value: The value of the of the control qubit after measurement.
    Return type: Integer (0 or 1)
    """

    # Required operators + states
    h_1 = qs.hadamard()
    swap = qs.swap()
    c_swap = qs.controlled_operator(swap)
    control_qubit = qs.zeros(1)

    # State preparation
    x = control_qubit * state1 * state2

    # Controlled swap as fidelity estimator
    x = h_1(x, qubit_ind=[0])
    x = c_swap(x)
    x = h_1(x, qubit_ind=[0])

    return x.measure(qubit_ind=0)
