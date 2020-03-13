import pandas as pd
import click
from execute import *


def get_cmd():
    cmd_dict = {'s': '将csv均分为N个csv',
                'c': '每N行切分为一个csv',
                't': '按csv中某列的值Top N行'}
    while True:
        print('Commands:')
        for i in cmd_dict.keys():
            print(i, ':', cmd_dict[i])
        cmd = input('Please input a command:')
        if cmd not in cmd_dict.keys():
            print('Wrong command!')
        else:
            return cmd


@click.command()
@click.argument('csv')
def run(csv):
    cmd = get_cmd()
    df = pd.read_csv(csv)
    print('csv shape: [%s rows x %s columns]' % df.shape)

    if cmd == 's':
        split_csv(df, csv)
    elif cmd == 'c':
        cut_csv(df, csv)
    elif cmd == 't':
        pass


if __name__ == '__main__':
    run()
