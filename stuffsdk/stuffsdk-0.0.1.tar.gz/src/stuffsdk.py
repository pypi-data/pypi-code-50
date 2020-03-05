import sys,os
import argparse


def main():
    parser = argparse.ArgumentParser(prog='stuff_mining',description='template factory package.')
    parser.add_argument('-w', action="store", dest="p",  default=False , help="home directory path of your project.")
    args = parser.parse_args()
    p = args.p
    print(p)


if __name__ == "__main__":
    main()