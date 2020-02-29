import qcSim as qs
from qcSubroutines import swap_test
import numpy as np


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

    # Initalization of the quantum states in two ways to avoid underestimation of the distance in direction of the x-asis
    bloch_sphere = []
    bloch_sphere_exchanged = []
    for i in range(len(values)):
        state = qs.bit_array(0)
        theta = values[i][1] * np.pi
        # Φ can range from 0 to π -> Only if this is the case the phase difference between qubits is proportional to the actual Euclidean distance between the two data points
        phi = values[i][0] * np.pi
        n_state = qs.two_pulse(theta, phi)(state)
        e_state = qs.two_pulse(phi, theta)(state)
        bloch_sphere.append(n_state)
        bloch_sphere_exchanged.append(e_state)

    distances = []
    for i in range(1, len(values)):
        results_n = [0] * r
        results_e = [0] * r
        # r repetitions of the SWAP-Test
        for j in range(r):
            results_n[j] = swap_test(bloch_sphere[0], bloch_sphere[i])
            results_e[j] = swap_test(
                bloch_sphere_exchanged[0], bloch_sphere_exchanged[i])
        # Estimtation of the probability for measuring the ancillary qubit in state |1>
        distance_n = sum(results_n) / r
        distance_e = sum(results_e) / r
        if abs((distance_n - distance_e)) > (1 / 4):
            distances.append(max(distance_n, distance_e))
        else:
            distances.append(distance_n)

    return distances
