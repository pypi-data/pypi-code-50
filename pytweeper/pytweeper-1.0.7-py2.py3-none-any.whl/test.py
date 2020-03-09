import argparse
parser = argparse.ArgumentParser(description='PyTweeper (Twitter crawler)')
parser.add_argument('command', nargs='?', help='command or mode')
parser.add_argument('-d', nargs=1, type=str, help='Upload to Google Drive')

args = vars(parser.parse_args())
drive = args['d']
command = args['command']

path = input('Google Drive Credentials.json ->')
print(path)
# print(args)
# print(command)
# print(drive)