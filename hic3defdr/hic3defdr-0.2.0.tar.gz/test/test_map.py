from hic3defdr.parallelization import parallel_map


def f(v):
    print('hi')
    return v


def main():
    res = parallel_map(f, [{'v': 0}, {'v': 1}], n_threads=2)
    print res


if __name__ == '__main__':
    main()
