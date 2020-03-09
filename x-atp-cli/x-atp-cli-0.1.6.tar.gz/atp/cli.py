import sys
import zipfile
import argparse
from pathlib import Path


def main():
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parser = argparse.ArgumentParser(description='X ATP CLI Client (X automated test platform command line client)')
    parser.add_argument('-v', '--version', help='Output client version information', action='store_true')
    parser.add_argument('-d', '--demo', help='Create `x_sweetest_example` project in the current directory',
                        action='store_true')
    args = parser.parse_args()
    if args.version:
        print("Current client version: v0.1.6")
    if args.demo:
        x_sweetest_dir = Path(__file__).resolve().parents[0]
        example_dir = x_sweetest_dir / 'example' / 'x_sweetest_example.zip'
        extract(str(example_dir), Path.cwd())
        print('Generated `x_sweetest_example` successfully\n' +
              'Quick experience, please enter the following command ' +
              '(go to the sample directory and start running the script):\n\n' +
              'cd x_sweetest_example\npython start.py')


def extract(z_file, path):
    f = zipfile.ZipFile(z_file, 'r')
    for file in f.namelist():
        f.extract(file, path)


if __name__ == '__main__':
    main()
