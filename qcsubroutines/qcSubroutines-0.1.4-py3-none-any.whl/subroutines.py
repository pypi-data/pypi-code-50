import qcSim as qs
import numpy as np

"""
A collection of functions that are used in quantum optimization or quantum machine learning algorithms.

Explanation for time complexity consideration:
    Number of qubits: n
    Number of elements: x = 2**n
"""


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
    controll_qubit = qs.zeros(1)

    # State preparation
    x = controll_qubit * state1 * state2

    # Controlled swap as fidelity estimator
    x = h_1(x, qubit_ind=[0])
    x = c_swap(x)
    x = h_1(x, qubit_ind=[0])

    return x.measure(qubit_ind=0)


# Auxiliary function which is necessary for the dist_calc-algorithm.
def transform(centroid, points):
    """
    Transforms the data points into a value range from 0 to 1. Necessary to map them in the Bloch sphere.

    Parameters:
        centroid: List -> Coordinates of the centroid.
        points: List -> Nested list that contains the coordinates of all data points.
    Return values and return types:
        reduced_centroid: List -> Coordinates of the centroid transformed into a value range from 0 to 1.
        reduced_vectors: List -> Nested list that contains the coordinates of the data points transformed into a value range from 0 to 1.
    """

    maximum = np.amax(np.append(points, centroid))
    minimum = np.amin(np.append(points, centroid))

    reduced_centroid = [(centroid[0] - minimum) / (maximum - minimum),
                        (centroid[1] - minimum) / (maximum - minimum)]

    reduced_vectors = []
    for i in range(len(points)):
        x = (points[i][0] - minimum) / (maximum - minimum)
        y = (points[i][1] - minimum) / (maximum - minimum)
        cord = [x, y]
        reduced_vectors.append(cord)

    return reduced_centroid, reduced_vectors


def dist_calc(centroid, points, r=1000):
    """
    Used in quantum algorithms like quantum k-means to find the closest centroid -> Calculates the "distance" of a point A to a set of other points.
    By applying different unitary operators to a quantum state that stores the informations about the vectors we want to calculate the distance between,
    we obtain a relationship between the probability of measuring the ancillary qubit in the state |1> and the fidelity (inner product) of the two states.
    The equation for the probability of measuring the ancillary qubit in state |1> is positively correlated with the equation for the euclidean distance.
    Therefore we can measure the "distance" between two vectors on a quantum computer by estimating the probability of measuring the ancillary qubit in state |1>.
    Note: The "distance" determined by the dist_calc function is not proportional to the euclidean distance, only positively correlated.
          But the subroutine is still useful for algorithms that need to find the closest centroid (or neighbor) for a point A and  not the exact distances between these points.
    Source: https://towardsdatascience.com/quantum-machine-learning-distance-estimation-for-k-means-clustering-26bccfbfcc76
    Speedup: Exponential speedup.
    Time complexity of calculating the euclidean distance between two x-dimensional vectors on a classical computer: O(x) = O(2**n)
    Time complexity of the dist_calc subroutine on a quantum computer: O(log(x)) = O(n)
        -> The x-dimensional basis vector is encoded in n qubits -> To estimated the distance between this vectors n swap tests (smallest step) are necessary.
        -> Source: Kopczyk (2018) p.34

    Parameters:
        centroid: List -> X and Y coordinates of the centroid formated as a list.
        points: List ->  Coordinates of the other points of the data set formated as a nested list.
        r: Integer -> Number of repetitions of the swap test (more repetitions will provide a better estimation).
    Return value: "Distances" between point A (the centroid) and the other points.
    Return type: List
    """

    # First step of scaling the points into a co-domain of 0 to 1 can be done on a normal computer.
    reduced_centroid, reduced_points = transform(centroid, points)

    # For the following calculations a quantum computer is needed.
    # Initialization of quantum states -> Map data points in the Bloch sphere
    values = np.append(reduced_centroid, reduced_points).reshape(
        (len(points) + 1), 2)

    bloch_sphere = []
    bloch_sphere_exchanged = []
    for i in range(len(values)):
        state = qs.bit_array(0)
        theta = values[i][1] * np.pi
        phi = values[i][0] * np.pi
        n_state = qs.two_pulse(theta, phi)(state)
        e_state = qs.two_pulse(phi, theta)(state)
        bloch_sphere.append(n_state)
        bloch_sphere_exchanged.append(e_state)

    distances = []
    for i in range(1, len(values)):
        results_n = [0] * r
        results_e = [0] * r
        for j in range(r):
            results_n[j] = swap_test(bloch_sphere[0], bloch_sphere[i])
            results_e[j] = swap_test(
                bloch_sphere_exchanged[0], bloch_sphere_exchanged[i])
        distance_n = sum(results_n)
        distance_e = sum(results_e)
        if abs((distance_n - distance_e)) > (r / 4):
            distances.append(max(distance_n, distance_e))
        else:
            distances.append(distance_n)

    return distances


def quantum_phase_estimation(m, e_vec, c=5):
    """
    Algorithm to estimate the phase (or eigenvalue) of an eigenvector of a unitary operator.
    This function is used in quantum Principal Components Analysis algorithm.
    Speedup: Exponential speedup (based on speedup of quantum Fourier transformation).
    Time complexity of the fast Fourier transformation on a classical computer: O(n * (2**n)) = O(log(x) * x)
    Time complexity of the quantum Fourier transformation: O(log(n) * n) = O(log(log(x)) * log(x))
        -> Source: Kopczyk (2018) p.27

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

    # Generates the operator for matrix
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


# Auxiliary function which is necessary for the Dürr-Hoyer-algorithm.
def create_boolean_function(n, g, threshold):
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


def duerr_hoyer(n, g):
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
    threshold = g(xi)

    # State that stores the current threshold
    yi = qs.bit_array(
        *tuple(map(int, bin(threshold)[bin(threshold).find('b') + 1:])))

    # Optimal number of iterations - see Dürr, Hoyer (1996) p.1
    iterations = int(round(22.5 * np.sqrt(2**n) + 1.4 * np.log2(2**n) + 0.5))
    return_measurement = 0

    for j in range(iterations):
        # Construction of the the boolean function, the corresponding quantum oracle and the Grover operator
        f = create_boolean_function(n, g, threshold)
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

    # Necessary so that the measurement with the lowest function value is returned and not the last measurement
    if return_measurement == 0:
        return measurement
    else:
        return return_measurement
