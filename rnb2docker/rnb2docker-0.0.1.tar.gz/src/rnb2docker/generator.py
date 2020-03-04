# generator.py
# Copyright (C) 2020 Fracpete (fracpete at gmail dot com)

import argparse
import json
import logging
import os
import traceback

# logging setup
logger = logging.getLogger("rnb2docker.generator")


# the mirror template
MIRROR_TEMPLATE = """
cat(".Rprofile: Setting repository")
r = getOption("repos")
r["CRAN"] = "%s"
options(repos = r)
rm(r)
"""

def get_dependencies(cells):
    """
    Retrieves the 'install.packages(..)' commands from the cells.

    :param cells: the cells to iterate
    :type cells: list
    :return: the list of dependencies (instances of "pip install ...")
    :rtype: list
    """

    result = []

    for cell in cells:
        if ("cell_type" in cell) and (cell["cell_type"] == "code") and ("source" in cell):
            for line in cell["source"]:
                if ("install.packages(" in line):
                    result.append(line)

    return result


def to_code(cells):
    """
    Turns the cells into Python code.

    :param cells: the cells to iterate
    :type cells: list
    :return: the generated code
    :rtype: list
    """

    result = []

    for cell in cells:
        if ("cell_type" in cell):
            if (cell["cell_type"] == "code") and ("source" in cell):
                for line in cell["source"]:
                    if ("install.packages(" in line):
                        result.append("# " + line.rstrip())
                    else:
                        result.append(line.rstrip())
            elif (cell["cell_type"] == "markdown") and ("source" in cell):
                for line in cell["source"]:
                    result.append("# " + line.rstrip())
            result.append("")

    return result


def generate(input, docker_base_image, docker_instructions, output_dir, mirror):
    """

    :param input: the Jupyter notebook to convert
    :type input: str
    :param docker_base_image: the name of the Docker base image to use
    :type docker_base_image: str
    :param docker_instructions: the file with the additional docker instructions to insert
    :type docker_instructions: str
    :param output_dir: the output directory for the generated files, like Dockerfile
    :type output_dir: str
    :param mirror: the mirror to use for R packages
    :type mirror: str
    """

    logger.info("Loading notebook: %s" % input)
    with open(input, "r") as jsonfile:
        j = json.load(jsonfile)
        if "cells" not in j:
            logger.error("JSON file does not contain top-level 'cells' object!")
            return

        # determine dependencies
        deps = get_dependencies(j["cells"])
        logger.debug("Dependencies: %s" % deps)
        if len(deps) > 0:
            deps_name =  os.path.join(output_dir, "libs.r")
            with open(deps_name, "w") as debs_file:
                for line in deps:
                    debs_file.write("%s\n" % line)

        # mirror
        rprof_name = os.path.join(output_dir, ".RProfile")
        with open(rprof_name, "w") as rprof_file:
            rprof_file.write(MIRROR_TEMPLATE % mirror)

        # generate code and save it
        code = to_code(j["cells"])
        code_name = os.path.join(output_dir, "code.r")
        logger.info("Saving R code as: %s" % code_name)
        with open(code_name, "w") as code_file:
            for line in code:
                code_file.write("%s\n" % line)

        # load additional docker instructions
        additional = []
        if docker_instructions is not None:
            with open(docker_instructions, "r") as instructions_file:
                additional = instructions_file.readlines()

        # write Dockerfile
        docker_name = os.path.join(output_dir, "Dockerfile")
        with open(docker_name, "w") as docker_file:
            # base image
            docker_file.write("FROM %s\n" % docker_base_image)

            # additional instructions
            if len(additional) > 0:
                docker_file.write("\n")
                docker_file.write("# additional instructions\n")
                for i, line in enumerate(additional):
                    docker_file.write("%s\n" % line.rstrip())

            # profile
            docker_file.write("# profile\n")
            docker_file.write("COPY .RProfile /root/.RProfile\n")

            # dependencies
            if len(deps) > 0:
                docker_file.write("# dependencies\n")
                docker_file.write("COPY libs.r /rnb2docker/libs.r\n")
                docker_file.write("RUN R -f /rnb2docker/libs.r\n")

            # execute code
            docker_file.write("\n")
            docker_file.write("# copy/execute code\n")
            docker_file.write("COPY code.r /rnb2docker/code.r\n")
            docker_file.write('CMD ["R", "--slave", "-f", "/rnb2docker/code.r"]\n')


def main(args=None):
    """
    Runs the .nfo generation.
    Use -h/--help to see all options.

    :param args: the command-line arguments to use, uses sys.argv if None
    :type args: list
    """

    parser = argparse.ArgumentParser(
        description='Converts R Jupyter notebooks into Docker images.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prog="rnb2docker")
    parser.add_argument("-i", "--input", metavar="NOTEBOOK", dest="input", required=True, help="the R notebook to convert")
    parser.add_argument("-b", "--docker_base_image", metavar="IMAGE", dest="docker_base_image", required=True, help="the Docker base image to use, e.g., 'r-base:latest'")
    parser.add_argument("-I", "--docker_instructions", metavar="FILE", dest="docker_instructions", required=False, help="file with additional docker instructions to use for generating the Dockerfile.")
    parser.add_argument("-m", "--mirror", metavar="URL", dest="mirror", required=False, default="https://cran.stat.auckland.ac.nz/", help="the mirror to use for the R packages")
    parser.add_argument("-o", "--output_dir", metavar="DIR", dest="output_dir", required=True, help="the directory to place the generated files in")
    parser.add_argument("--verbose", action="store_true", dest="verbose", required=False, help="whether to output logging information")
    parser.add_argument("--debug", action="store_true", dest="debug", required=False, help="whether to output debugging information")
    parsed = parser.parse_args(args=args)
    # configure logging
    if parsed.debug:
        logging.basicConfig(level=logging.DEBUG)
    elif parsed.verbose:
        logging.basicConfig(level=logging.INFO)
    logger.debug(parsed)
    generate(input=parsed.input, docker_base_image=parsed.docker_base_image,
             docker_instructions=parsed.docker_instructions, output_dir=parsed.output_dir,
             mirror=parsed.mirror)


def sys_main():
    """
    Runs the main function using the system cli arguments, and
    returns a system error code.

    :return: 0 for success, 1 for failure.
    :rtype: int
    """

    try:
        main()
        return 0
    except Exception:
        logger.info(traceback.format_exc())
        return 1


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.error(traceback.format_exc())
