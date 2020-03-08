import argparse

from livesplit_id_normalizer.normalizer import normalize


def start():
    parser = argparse.ArgumentParser(description="Process livesplit splits")
    parser.add_argument("path", help="Path for splits file")
    parser.add_argument(
        "--initial-run", type=int, help="Do not parse old file for initial run"
    )
    parser.add_argument("--output-path", help="Output path for normalized splits file")
    args = parser.parse_args()
    normalize(args.path, args.output_path, args.initial_run)


if __name__ == "__main__":
    start()  # pragma: no cover
