# from genome import Genome
# from genome import skew
from genome import *

def main():
    clumps = clump_finder("""ACGTACGT""",1,5,2)
    print("clumps: {}".format(clumps))

# def main():
#     gen = open('dataset_7_6.txt', 'r').read()
#     genome = Genome(gen,'The genome of E.Coli','dataset_7_6.txt')
#     min_skew = genome.minimum_skew()
#     _skew = skew(gen,5)
#     print("minimum skew: \n\n{}\n".format(min_skew))
#     print(genome)
#     print("\nskew: {}\n".format(_skew))


if __name__ == '__main__':
    main()
