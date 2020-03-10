import argparse
import os
import errno
from mdtemplater.templater import md_template

def make_dirs_to(path):
    sub_path = os.path.dirname(path)
    if not os.path.exists(sub_path):
        make_dirs_to(sub_path)
    if not os.path.exists(path):
        os.mkdir(path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", metavar="", dest="directory", default=".", type=str, help="The top level location that the folder layout will be placed. Defaults to current directory.")
    parser.add_argument("-s", "--subject", metavar="", required=True, dest="subject", type=str, help="The subject name used to name the first folder.")
    parser.add_argument("-w", "--weeks", metavar="", dest="weeks", default=0, type=int, help="Optional number of weeks to produce lecture folders for.")
    parser.add_argument("-n", "--numlect", metavar="", dest="num_lectures", default=0, type=int, help="Optional value to add base templated markdown files for lectures per week.")

    args = parser.parse_args()

    base_dir = os.path.join(args.directory, args.subject)

    lectures_dir = os.path.join(base_dir, "Lectures")
    materials_dir = os.path.join(base_dir, "Materials")
    assignment_dir = os.path.join(base_dir, "Assignments")

    make_dirs_to(materials_dir)
    make_dirs_to(assignment_dir)
    # Opening empty hidden files so that git will actually pick them up
    open(materials_dir + "/.gitkeep", "a+")
    open(assignment_dir + "/.gitkeep", "a+")
    make_dirs_to(lectures_dir)

    # Add the weeks if they are provided
    for i in range(1, args.weeks+1):
        directory = os.path.join(lectures_dir, "week%d"%i)
        make_dirs_to(directory)
        for j in range(1, args.num_lectures + 1):
            lecture_num = j + ((i - 1) * args.num_lectures)
            lecture_name = "Lecture %d" % lecture_num
            file_name = "Lecture%d.md" % lecture_num
            md_template(directory + "/" + file_name, lecture_name)

if __name__ == "__main__":
    main()
