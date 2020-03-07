import argparse
import inspect
import logging
import os
import sys

from py_pal.tracer import Tracer

from py_pal.complexity import Complexity
from py_pal.estimator import Columns, AllArgumentEstimator, SeparateArgumentEstimator
from py_pal.util import plot_data_points, save_statistics


def main():
    assert sys.version_info >= (3, 7)
    # TODO: change "-v" flag to output version information
    parser = argparse.ArgumentParser(description='Profile')
    parser.add_argument('-f', '--function', type=str, help='specify a function')
    parser.add_argument('-l', '--line', help='Calculate complexity for each line', action='store_true')
    parser.add_argument('-v', '--visualize', help='Plot runtime graphs', action='store_true')
    parser.add_argument('-s', '--separate', help='Estimate function complexity for each argument', action='store_true')
    parser.add_argument('-o', '--out', type=str, help='Output directory', default='stats')
    parser.add_argument('--save', help='Save statistics', action='store_true')
    parser.add_argument('--debug', help='Log debug output', action='store_true')
    parser.add_argument('--format', type=str, help='Output format, possible types are: csv, html, excel, json',
                        default='csv')
    parser.add_argument('target', type=str, help='a Python file or import path')

    args, unknown = parser.parse_known_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format='[%(levelname)s, %(module)s, %(funcName)s]: %(message)s'
    )
    logger = logging.getLogger(__name__)

    sys.path.insert(0, '.')

    function = None
    if args.function:
        function = getattr(__import__(args.target, fromlist=[args.function]), args.function)
        sys.argv = [inspect.getfile(function), *unknown]

    file = None
    try:
        file = open(args.target).read()
    except FileNotFoundError:
        pass

    if not function and file is None:
        raise ValueError("File or function could not be loaded")

    # TODO: Test cases: simple examples, sorting algorithms, games(pygame, term2048, mario, ...)
    # TODO: Output: function, parameter_name+nummer, complexity, line, module(filename), amount_data_points

    tracer = Tracer()

    if file:
        code = compile(file, filename=args.target, mode='exec')
        _globals = globals()

        # Execute as direct call e.g. 'python example.py'
        _globals['__name__'] = '__main__'

        # Append path to enable module import resolution in client code
        sys.path.append(os.path.dirname(args.target))

        # Pass arguments
        sys.argv = [args.target, *unknown]

        tracer.trace()
        exec(code, _globals, _globals)
        tracer.stop()

    if function:
        tracer.trace()
        function()
        tracer.stop()

    if args.separate:
        res = SeparateArgumentEstimator(tracer, args.line).export()
    else:
        res = AllArgumentEstimator(tracer, args.line).export()

    logger.info(res[[
        Columns.FUNCTION_NAME, Columns.ARG_DEP, Columns.COMPLEXITY, Columns.FUNCTION_LINE, Columns.FILE,
        Columns.DATA_POINTS
    ]].to_string())

    # pd.options.display.max_colwidth = 100

    # TODO: additionally allow plot on single axis and let user select which functions to plot (using querying language)

    if not args.save and args.visualize:
        res = res[[isinstance(x, Complexity) for x in res[Columns.COMPLEXITY]]]

        for index, data_frame in res.iterrows():
            plot = plot_data_points(data_frame)
            plot.show()

    if args.save:
        save_statistics(res, args.out, args.target, args.format, args.visualize)


if __name__ == "__main__":
    main()
