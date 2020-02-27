import argparse

import kgd.validators as validators


def parse_args():
    """ Parse CLI arguments and return validated values """
    parser = argparse.ArgumentParser(
        description="Tool for retrieving information on tax payments by Kazakhstan companies",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("token", type=str,
                        help="KGD API secret token")

    parser.add_argument("fpath", type=validators.check_fpath,
                        help="input file with BINs")

    parser.add_argument("date_range", type=validators.check_date_range,
                        help="date range for which we retrieve data")

    parser.add_argument("-t", "--timeout", default=3.0,
                        type=validators.check_positive_float,
                        help="server connect timeout")

    parser.add_argument("-f", "--fsize",
                        default=50000000, type=validators.check_positive_int,
                        help="size limit for output file")

    return parser.parse_args()
