import argparse
from useful import get_json
from worker import main as work
import os


class Args:
    def __init__(self):
        parser = argparse.ArgumentParser()

        parser.add_argument("paths", help="The path(s) of the file(s).", nargs="+")

        self.black_args: list = []
        self.black_args_b: list = []
        for arg in get_json(
            __file__[: -len(os.path.basename(__file__))] + "arguments.json"
        ):
            if "type" in arg.keys():
                if arg["type"] == "bool":
                    self.black_args_b.append(arg["long"].replace("-", "_"))
                    if "short" in arg.keys():
                        parser.add_argument(
                            "-" + arg["short"],
                            "--" + arg["long"],
                            help=arg["help"],
                            default=None,
                            type=bool,
                            nargs="?",
                            const=True,
                        )
                    else:
                        parser.add_argument(
                            "--" + arg["long"],
                            help=arg["help"],
                            default=None,
                            type=bool,
                            nargs="?",
                            const=True,
                        )
                    continue
            self.black_args.append(arg["long"].replace("-", "_"))
            if "short" in arg.keys():
                parser.add_argument(
                    "-" + arg["short"],
                    "--" + arg["long"],
                    help=arg["help"],
                    default=None,
                )
            else:
                parser.add_argument("--" + arg["long"], help=arg["help"], default=None)
        self.args = parser.parse_args()

    @property
    def files(self):
        return self.args.paths

    @property
    def for_black(self):
        return " ".join(
            [
                f"--{name.replace('_', '-')} {vars(self.args)[name]}"
                for name in self.black_args
                if vars(self.args)[name] is not None
            ]
            + [
                "--" + name.replace("_", "-")
                for name in self.black_args_b
                if vars(self.args)[name] is True
            ]
        )

    def run(self):
        for file in self.files:
            work(file, self.for_black.split(" "))


def main():
    args = Args()
    args.run()


if __name__ == "__main__":
    pass
