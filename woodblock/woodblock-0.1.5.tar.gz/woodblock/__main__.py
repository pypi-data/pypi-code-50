import pathlib
import sys

import click

import woodblock

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass


@main.command(name='generate')
@click.argument('config', type=click.Path(exists=True))
@click.argument('image', type=click.Path())
def generate_image(config, image):
    """Generate an image based on the given configuration file.

    \b
    CONFIG is the path to the configuration file to use.
    IMAGE  is the output path of the generated image."""
    img = woodblock.image.Image.from_config(pathlib.Path(config))
    img.write(pathlib.Path(image))

import string
@main.command(name='parse')
@click.argument('logfile', type=click.Path(exists=True))
def parse_image_log(logfile):
    """Generate an image based on the given configuration file.

    \b
    CONFIG is the path to the configuration file to use.
    IMAGE  is the output path of the generated image."""
    with open(logfile, 'rb') as fp:
        parser = woodblock.image.ImageLogParser(fp)
        frag_order = parser.get_fragment_order()
        files = {x[1] for x in frag_order}
        for k in files:
            print(k)
        for k,v in enumerate(frag_order):
            print(k,v)
        #files = tuple(x[2] for x in frag_order)

        for frag in frag_order:
            print(frag)
    

if __name__ == '__main__':
    sys.exit(main())
