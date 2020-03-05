import argparse
import atexit
import sys
from pathlib import Path
from tempfile import NamedTemporaryFile

import requests
from pyunpack import Archive
from tqdm import tqdm

CHUNK_SIZE = 1024


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--destination",
        default=".",
        help=(
            "Path where files will be extracted (defaults to current "
            "directory)"
        ),
    )
    parser.add_argument("url", help="URL of file to download and extract")
    return parser.parse_args()


def check_request_error(r):
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    return r


def progress(url):
    head = check_request_error(requests.head(url))
    options = dict(desc=url, initial=0, unit="B", unit_scale=True)
    file_size = int(head.headers.get("Content-Length", -1))
    if file_size > 0:
        options["total"] = file_size
    return tqdm(**options)


def download(url):
    with progress(url) as p:
        with check_request_error(requests.get(url, stream=True)) as r:
            with NamedTemporaryFile(delete=False) as f:
                # remove archive when program exits
                atexit.register(Path(f.name).unlink)
                for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                    if chunk:
                        f.write(chunk)
                        p.update(CHUNK_SIZE)

    return f.name


def extract(filename, destination, mode=0o755):
    Path(destination).mkdir(mode=mode, parents=True, exist_ok=True)
    Archive(filename).extractall(destination)


def download_and_extract(url, destination, **kwargs):
    extract(download(url), destination, **kwargs)


def main():
    args = arguments()
    download_and_extract(args.url, args.destination)


if __name__ == "__main__":
    main()
