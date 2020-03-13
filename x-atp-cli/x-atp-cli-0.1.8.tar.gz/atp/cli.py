import re
import sys
import zipfile
import argparse
from pathlib import Path
from api_server import api_server


def main():
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parser = argparse.ArgumentParser(description='X ATP CLI Client (X automated test platform command line client)')
    parser.add_argument('-v', '--version', help='Output client version information', action='store_true')
    parser.add_argument('-d', '--demo', help='Create `x_sweetest_example` project in the current directory',
                        action='store_true')
    parser.add_argument('-s', '--server', help='Start X-ATP automated test execution side service', action='store_true')
    args = parser.parse_args()
    if args.version:
        print("Current client version: v0.1.8")
    if args.demo:
        x_sweetest_dir = Path(__file__).resolve().parents[0]
        example_dir = x_sweetest_dir / 'example' / 'x_sweetest_example.zip'
        extract(str(example_dir), Path.cwd())
        print('Generated `x_sweetest_example` successfully\n' +
              'Quick experience, please enter the following command ' +
              '(go to the sample directory and start running the script):\n\n' +
              'cd x_sweetest_example\npython echo.py')
    if args.server:
        x_atp_url = input("X-ATP Server URL (E.g http://127.0.0.1):")
        if not re.match(r'(http|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?', x_atp_url,
                        re.IGNORECASE):
            print('This is not a valid URl address !')
            return
        server_type = input('X-ATP Server Type (Options are api/..):')
        if server_type == 'api':
            api_server(url=x_atp_url)
        else:
            print('This is not a valid entry !')
            return


def extract(z_file, path):
    f = zipfile.ZipFile(z_file, 'r')
    for file in f.namelist():
        f.extract(file, path)


if __name__ == '__main__':
    main()
