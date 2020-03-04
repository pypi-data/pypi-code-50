"""Console script for slicerfiducials."""
import argparse
import os
import sys

import SimpleITK as sitk

from slicerfiducials.slicerfiducials import SlicerFiducials

TRANSFROM_COMMAND_NAME = "transform"
DISTANCE_COMMAND_NAME = "distance"
DESCRIBE_COMMAND_NAME = "describe"


def get_transform_name(tfm):
    # HACK: replace this with a supported interface
    itk_name = str(tfm).split()[1]
    param_str = "-".join(["%.3f" % a for a in tfm.GetParameters()])
    return f"{itk_name}_params_{param_str}"


def cli_transform(args):
    transform = sitk.ReadTransform(args.transform_file)

    fiducials = SlicerFiducials(args.fcsv)

    fiducials.apply_sitk_transform(transform, inplace=True)

    output_dir = os.path.join(
        os.path.abspath(args.output_dir),
        get_transform_name(transform),
    )

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    output_filename = os.path.join(
        output_dir,
        os.path.split(args.fcsv)[-1],
    )

    fiducials.write(output_filename)


def cli_distance(args):
    print("inside distance")
    print(args)
    pass


def main():
    """Console script for slicerfiducials."""
    parser = argparse.ArgumentParser()
    parser.add_argument("fcsv", help="fcsv file")

    command_subparsers = parser.add_subparsers(dest="command", required=True)

    #  subparser for transform functionality
    parser_transform = command_subparsers.add_parser(TRANSFROM_COMMAND_NAME)
    parser_transform.add_argument("transform_file", help="tranform to apply")

    #  subparser for distance functionality
    parser_distance = command_subparsers.add_parser(DISTANCE_COMMAND_NAME)
    parser_distance.add_argument(
        "-f1", "--fiducial-one", required=True, help="first fiducial"
    )
    parser_distance.add_argument(
        "-f2", "--fiducial-two", required=True, help="second fiducial"
    )
    parser_distance.add_argument(
        "-m",
        "--metric",
        default="euclidean",
        help="distance metric to use in calculation",
    )
    # ADD NEW SUBPARSERS HERE

    # optional args
    parser.add_argument(
        "-o",
        "--output-dir",
        default="./slicerfiducials_out",
        help="output directory to write the distance/transformed fcsv to",
    )

    args = parser.parse_args()

    # validate global args
    if not os.path.isdir(args.output_dir):
        os.makedirs(args.output_dir)

    command_dict = {
        TRANSFROM_COMMAND_NAME: cli_transform,
        DISTANCE_COMMAND_NAME: cli_distance,
        # ADD NEW COMMANDS HERE
    }
    # run the command
    command_dict[args.command](args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
