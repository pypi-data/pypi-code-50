from os import getcwd
from tqdm import tqdm
from pathlib import Path
from argparse import ArgumentParser
from dvk_archive.file.dvk_handler import DvkHandler


def rename_files(directory_str: str = None):
    """
    Renames all the DVK files and associated media files in a given directory.

    Parameters:
        directory_str (str): Directory in which to rename files.
    """
    dvk_handler = DvkHandler()
    dvk_handler.load_dvks([directory_str])
    print("Renaming files:")
    size = dvk_handler.get_size()
    for i in tqdm(range(0, size)):
        dvk_handler.get_dvk_direct(i).rename_files()


def main():
    """
    Runs the rename_files function from the command line.
    """
    parser = ArgumentParser()
    parser.add_argument(
        "directory",
        help="Directory in which to preform operations.",
        nargs="?",
        type=str,
        default=str(getcwd()))
    args = parser.parse_args()
    dir = Path(args.directory)
    rename_files(str(dir.absolute()))


if __name__ == "__main__":
    main()
