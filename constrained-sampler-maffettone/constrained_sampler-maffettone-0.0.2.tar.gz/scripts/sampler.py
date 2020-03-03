"""
Python script to to efficiently sample high dimensional spaces with complex, non-linear constraints.

The script that can be run as python sampler.py <input_file> <output_file> <n_results>.

The input file starts with a single line header that gives the dimensionality of the problem,
which is defined on the unit hypercube.
The next line is a single example feasible point.
The remaining lines are a list of constraints as python expressions containing + , - , * , / , and ** operators.
They have been transformed such that they all take the form g(x) >= 0.0 .
@author: maffettone
"""
import sys
import argparse

sys.path.append('../')
from constrained_sampler.sample_space import SampledSpace


def main(namespace):
    space = SampledSpace(namespace.input_file, random_state=namespace.seed)
    space.adaptive_displacement(target_rate=namespace.acceptance_rate,
                                total_steps=namespace.max_steps,
                                timeout=namespace.timeout)

    arr = space.sample_space(namespace.n_results)
    with namespace.output_file as f:
        for i in range(arr.shape[0]):
            f.write(" ".join(map(str, arr[i, :])) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('input_file', type=str,
                        help='Path to input file. Required. ')
    parser.add_argument('output_file', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                        help='Path to output file. Defaults to STDOUT.')
    parser.add_argument('n_results', nargs='?', type=int, default=1000,
                        help='Number of samples to be output. Defaults to 1000.')
    parser.add_argument('-s ', '--seed', type=int,
                        help='Optional seed for pseudo random number generator.')
    parser.add_argument('-m ', '--max_steps', type=int, default=10 ** 7,
                        help='Maximum number of steps for internal Markov chain. Defaults to 1e7.')
    parser.add_argument('-t ', '--timeout', type=float, default=4.5,
                        help='Timeout for sampler in minutes. Sampler will exit if exploration of max_steps is '
                             'incomplete in timeout minutes. Defaults to 4.5 minutes.')
    parser.add_argument('-a', '--acceptance_rate', type=float, default=0.01,
                        help='Desired acceptance rate for internal Markov chain. Defaults to 0.01.')

    args = parser.parse_args()
    main(args)
