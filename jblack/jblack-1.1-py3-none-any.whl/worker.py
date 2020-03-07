from useful import get_json, write_json
import subprocess
import os


base_name = "_jblack_tmp"


def formatter(filename: str, tmpfile_name: str, args: list = None):
    """

    :param filename: name of the file to reformat
    :param tmpfile_name: name of the temp file
    :param args: arguments send to black
    :return: True if no errors else raise the error
    """
    if args is None or args == ['']:
        args = []
    json = get_json(filename)
    for i, cell in enumerate(json["cells"]):
        if cell["cell_type"] == "code":
            tmpfile_content = "".join(cell["source"])
            with open(tmpfile_name, "w") as f:
                f.write(tmpfile_content)

            # Black file tmpfile_name
            subprocess.call(["black", tmpfile_name, *args])

            # get content
            with open(tmpfile_name, "r") as f:
                tmpfile_content = f.read()

            # rewrite
            json["cells"][i]["source"] = [e + "\n" for e in tmpfile_content.split("\n")]
            json["cells"][i]["source"] = json["cells"][i]["source"][:-1]
            if len(json["cells"][i]["source"]) != 0:
                json["cells"][i]["source"][-1] = json["cells"][i]["source"][-1][:-1] 

    write_json(filename, json)
    subprocess.call(["rm", tmpfile_name])
    return True


def get_tmpfile_name() -> str:
    """
    search an unused file name
    :return: free file name
    """
    global base_name
    number = 0
    while base_name + str(number) in os.listdir("./"):
        number += 1
    return base_name + str(number)


def main(filename: str, args: list = None):
    if args is None:
        args = []
    formatter(filename, get_tmpfile_name(), args)


if __name__ == '__main__':
    fn = input("File name :")
    a = input("args :").split(" ")
    main(fn, a)
