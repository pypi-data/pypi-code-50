import qcSim as qs
from qcSubroutines import grover
import numpy as np


def duerr_hoyer_boolean_function(n, g, threshold):
    """
    Creates a boolean function f which returns 1 if the function value of the objective function g is below a certain threshold.

    Parameters:
        n: Integer -> Number of qubits which determines the number of function values that can be stored (2**n function values can be stored).
        g: Function -> Objective function of the minimization problem.
        threshold: Integer or float (dependent on objective function) -> Random threshold which is determined during an iteration of the Dürr-Hoyer-algorithm.
    Return value: The boolean function.
    Return type: Function
    """

    answer = [0] * (2**n)
    for i, v in enumerate(answer):
        if g(i) < threshold:
            answer[i] = 1

    def f(basis_state):
        # Converts the Dirac representation of the basis state into the corresponding integer index
        index = int("".join(str(i) for i in basis_state), 2)
        return answer[index]

    return f


def dürr_hoyer(n, g):
    """
    A quantum minimization algorithm, which uses the Grover algorithm as a basis.
    Minimization problems are also search problems.
    Speedup: Quadratic speedup (based on speedup of the Grover algorithm).
    Time complexity of solving a minimization problem on a classical computer: O(2**n) = O(x)
    Time complexity of the Dürr-Hoyer-algorithm: O(sqrt(2**n)) = O(sqrt(x))
        -> Source: Kopczyk (2018) p.22+23

    Parameters:
        n: Integer -> Number of qubits which determines the number of function values that can be stored (2**n function values can be stored).
        g: Function: -> Objective function of the minimization problem.
    Return value: The measured state which encodes the index of the global minimum.
    Return type: Tuple of integer (0 or 1)
    """

    # Generating the start threshold and the corresponding state
    xi = np.random.randint(0, 2**n)
    binary_xi = tuple(map(int, bin(xi)[bin(xi).find('b') + 1:]))
    threshold = g(xi)

    # State that stores the current threshold
    yi = qs.bit_array(
        *tuple(map(int, bin(threshold)[bin(threshold).find('b') + 1:])))

    # Optimal number of iterations - see Dürr, Høyer (1996) p.1
    iterations = int(round(22.5 * np.sqrt(2**n) + 1.4 * np.log2(2**n) + 0.5))
    return_measurement = binary_xi

    for j in range(iterations):
        # Construction of the the boolean function, the corresponding quantum oracle and the Grover operator
        f = duerr_hoyer_boolean_function(n, g, threshold)
        # Initialize/update the state that the algorithm is running on
        state = qs.zeros(n) * yi
        # The Grover algorithm only operates on the first n qubits in the state |0>
        measurement = grover(n, f, random=True)
        # Converts the measured state index into a decimal number
        xi = int("".join(str(i) for i in measurement), 2)
        # If new function value is smaller than threshold, change threshold and yi (state that stores the threshold)
        if g(xi) < threshold:
            threshold = g(xi)
            yi = qs.bit_array(
                *tuple(map(int, bin(threshold)[bin(threshold).find('b') + 1:])))
            return_measurement = measurement

    return return_measurement
