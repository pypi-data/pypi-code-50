import qcSim as qs
import numpy as np


def grover(n, f, k=1, random=False):
    """
    Quantum algorithm that searches through a specific number of boolean function inputs to check whether the function returns true for that input.
    It is very efficient in case the function is unknown or extremely complex and we want to know for which input the function returns true or for which input the equation is solved.
    Speedup: Quadratic speedup.
    Time complexity of search algorithm on a classical computer: O(2**n) = O(x)
    Time complexity of the Grover algorithm: O(sqrt(2**n)) = O(sqrt(x))
        -> Source: Kopczyk (2018) p.19

    Parameters:
        n: Integer -> Number of qubits which determines the number of function values that can be stored (2**n function values can be stored).
        f: Function -> The boolean function that returns 1 for the searched function values resp. their indices.
        k: Integer -> Number of function values (entries) for that the boolean function returns true.
        random: Boolean -> True if the number of Grover iterations should be a random number (necessary for Dürr-Hoyer-algorithm).
    Return value: The measured state which encodes the searched entry.
    Return type: Tuple of integer (0 or 1)
    """

    # Construction of operator r_n (Homeister S. 144)
    m = np.eye(2**n)
    m[0][0] = -1
    r_n = qs.Operator(m)

    # Other operators that are needed
    oracle = qs.u_f(n, f)
    h_n = qs.hadamard(n)
    d_n = -h_n(r_n)(h_n)
    grover = d_n(oracle)

    # Initial State
    state = qs.zeros(n)
    state = h_n(state)

    # Number of Grover iterations
    if random:
        iterations = np.random.randint(1, 2 ** n)
    else:
        iterations = int(
            round((np.pi / (4 * np.arcsin(np.sqrt(k / 2**n)))) - 0.5))

    # Actual Grover iterations and subsequent measurement
    for i in range(iterations):
        state = grover(state)
    measurement = state.measure()

    return measurement
