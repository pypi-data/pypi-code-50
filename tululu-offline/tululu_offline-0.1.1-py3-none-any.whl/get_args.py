import argparse


def create_parser() -> argparse.ArgumentParser:
    """Gets arguments from command line."""
    parser = argparse.ArgumentParser(
        description='download books in txt format from the site tululu.org',
    )

    parser.add_argument(
        'category_url',
        type=str,
        help='enter the url of the category whose books you want to parse',
    )

    parser.add_argument(
        '--start_page',
        type=int,
        default=1,
        help='enter the page where you want to start downloading',
    )

    parser.add_argument(
        '--end_page',
        type=int,
        default=100000,  # noqa: WPS432
        help='enter the page where you want to end downloading',
    )

    parser.add_argument(
        '--dest_folder',
        type=str,
        default='result',
        help='path to directory with parsing results: pictures, books, JSON',
    )

    parser.add_argument(
        '--skip_txt',
        type=str,
        help='do not download books',
    )

    parser.add_argument(
        '--skip_imgs',
        type=str,
        help='do not download images',
    )

    parser.add_argument(
        '--json_path',
        type=str,
        help='specify your path to *.json file with results',
    )

    return parser


def get_args() -> argparse.Namespace:
    """Gets arguments from command line."""
    return create_parser().parse_args()
