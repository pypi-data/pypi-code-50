import argparse
import os
import errno


def make_dirs_to(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def _write_header(file, size, header):
    for _ in range(size):
        file.write("#")
    file.write(" " + header)
    file.write("\n")


def write_link(file, link, link_text):
    file.write("[" + link_text + "]")
    file.write("(" + link + ")")
    file.write("\n")


def write_title(file, title):
    _write_header(file, 1, title)


def write_table_of_contents(file):
    file.write("[TOC]\n")


def write_terms_header(file):
    _write_header(file, 2, "Terms")


def md_template(filename, title, link=None):
    with open(filename, "a+") as f:
        if os.stat(filename).st_size != 0:
            print(filename + " is not empty. Skipping")
            return
        write_title(f, title)
        write_table_of_contents(f)
        if link:
            write_link(f, link, "Corresponding material")

        f.write("\n\n\n\n")
        write_terms_header(f)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--filename",
        metavar="",
        dest="filename",
        required=True,
        type=str,
        help="Name and path of the file. Generally add the .md suffix. Required",
    )
    parser.add_argument(
        "-t",
        "--title",
        metavar="",
        dest="title",
        required=True,
        type=str,
        help="Title used for the file. Required",
    )
    parser.add_argument(
        "-l",
        "--link",
        metavar="",
        dest="link",
        type=str,
        help="The link to the corresponding material",
    )

    args = parser.parse_args()

    md_template(args.filename, args.title, args.link)


if __name__ == "__main__":
    main()
