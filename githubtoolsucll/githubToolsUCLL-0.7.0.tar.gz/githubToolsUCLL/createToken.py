import argparse
import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+"/..")
from githubToolsUCLL import service


# de student pullt alle issues van de hoofd-repo na het clonen van de start-code
def main():
    parser = argparse.ArgumentParser(description="Script voor het creëren van een token")
    required = parser.add_argument_group("required arguments")

    required.add_argument('-T','--token', type=str, required=True, help="De gitHub token")

    args = parser.parse_args()

    service.valideerStrInputs(args)
    service.createToken(args.token)

if __name__ == '__main__':
    main()
