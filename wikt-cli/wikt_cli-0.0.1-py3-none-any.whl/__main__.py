from argparse import ArgumentParser
from wiktionaryparser import WiktionaryParser
from .utils import *

wikt = WiktionaryParser()


def main():
    argparser = ArgumentParser()
    argparser.add_argument('word')
    args = argparser.parse_args()

    etymologies = wikt.fetch(args.word)
    for etymology in etymologies:
        print('Etymology:')
        print(leftpad(etymology['etymology'], 4), '\n')
        print(leftpad('Definitions:', 4))
        for definition in etymology['definitions']:
            print(leftpad('({0}) {1}'.format(
                definition['partOfSpeech'],
                '\n'.join(definition['text'])), 8), '\n')


if __name__ == '__main__':
    main()
