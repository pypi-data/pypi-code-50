from argparse import (
    ArgumentParser,
    ArgumentDefaultsHelpFormatter,
)


def surfcut_parser():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        dest="image_path",
        type=str,
        nargs=1,
        help="Path to the image to be analysed",
    )
    parser.add_argument(
        "-g",
        "--gauss_sigma",
        dest="gauss_sigma",
        type=int,
        default=3,
        help="Gaussian smoothing sigma width",
    )
    parser.add_argument(
        "-t",
        "--threshold",
        dest="threshold",
        type=int,
        default=20,
        help="Threshold for binarising the image",
    )

    parser.add_argument(
        "-s",
        "--shift",
        dest="shift",
        type=int,
        default=14,
        help="Where relative to the surface of the sample should the "
        "cut be made",
    )

    parser.add_argument(
        "-d",
        "--depth",
        dest="depth",
        type=int,
        default=4,
        help="Thickness of the projection",
    )

    parser.add_argument(
        "-m",
        "--morphology",
        dest="morphology",
        action="store_true",
        help="Use morphological operations for highly curved objects (takes longer)",
    )

    parser.add_argument(
        "-n",
        "--no-viewer",
        dest="no_viewer",
        action="store_true",
        help="Don't launch the viewer",
    )

    return parser
