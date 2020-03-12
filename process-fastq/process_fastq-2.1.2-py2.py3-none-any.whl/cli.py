# -*- coding: utf-8 -*-

import os
import sys
import logging
import time
import pathlib
try:
    import click
except ImportError as e:
    print(
        "cli: click is not installed, please install click as it is one of the requirements."
    )
    exit(1)
try:
    import click_log
except ImportError as e:
    print(
        "cli: click-log is not installed, please install click_log as it is one of the requirements."
    )
    exit(1)
try:
    import process_fastq.process_fastq as pf
except ImportError as e:
    print(
        "cli: process_fastq module could not be loaded, please install package correctly to get this running."
    )
    exit(1)

"""
cli
~~~~~~~~~~~~~~~
:Description: console script for running process_fastq
"""
"""
Created on July 26, 2019
Description: console script for running process_fastq
@author: Ronak H Shah
"""

version = None
version_file = pathlib.Path(__file__).parent.absolute() / \
    '__init__.py'
with open(version_file, "r") as f:
    for line in f.readlines():
        line = line.strip()
        if line.startswith("__version__"):
            version = line.split("=")[-1].strip()
__all__ = []
__version__ = version
__date__ = "2019-07-27"
__updated__ = "2019-07-28"
# Making logging possible
logger = logging.getLogger("process_fastq")
click_log.basic_config(logger)
click_log.ColorFormatter.colors["info"] = dict(fg="green")


@click.command()
@click.option(
    "--sample-id",
    "-s",
    required=True,
    type=click.STRING,
    help="Sample id to get the fastq files can be either IGO sample id or Investigator sample id (eg: -s EDD_ret_pt049_cf02)",
)
@click.option(
    "--request-id",
    "-p",
    default=None,
    type=click.STRING,
    help="IGO request id to get the fastq files. (eg:-p Project_05500_GB or -p 05500_GB)",
)
@click.option(
    "--run-id",
    "-r",
    default=None,
    multiple=True,
    type=click.STRING,
    help="Run id to get the fastq files, can be specified multiple times (eg:-r PITT_0376 -r PITT_0378)",
)
@click.option(
    "--fastq-path",
    "-fp",
    required=True,
    type=click.Path(),
    help="Full path to fastq files",
)
@click.option(
    "--output-path",
    "-op",
    required=True,
    type=click.Path(),
    help="Full path to where we link the output files",
)
@click.option(
    "--cutadapt-path",
    "-cp",
    required=True,
    type=click.Path(exists=True),
    help="Full path to location of cutadapt executable",
)
@click.option(
    "--expected-read-length",
    "-l",
    required=False,
    default=101,
    type=click.INT,
    help="Expected read length from the fastq file",
)
@click.version_option(version=__version__, prog_name="process_fastq")
@click_log.simple_verbosity_option(logger)
def main(
    sample_id,
    fastq_path,
    expected_read_length,
    output_path,
    cutadapt_path,
    request_id=None,
    run_id=None,
):
    logger_output = os.path.join(output_path, "process_fastq.log")
    fh = logging.FileHandler(logger_output)
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info("==================================================")
    logger.info(">>> Running process_fastq for: %s <<<", sample_id)
    logger.info("==================================================")
    t1_start = time.perf_counter()
    t2_start = time.process_time()
    pf.run(
        sample_id,
        fastq_path,
        expected_read_length,
        output_path,
        cutadapt_path,
        request_id,
        run_id,
    )
    t1_stop = time.perf_counter()
    t2_stop = time.process_time()
    logger.info("--------------------------------------------------")
    logger.info("Elapsed time: %.1f [min]" % ((t1_stop - t1_start) / 60))
    logger.info("CPU process time: %.1f [min]" % ((t2_stop - t2_start) / 60))
    logger.info("--------------------------------------------------")
    return 0


if __name__ == "__main__":
    sys.exit(main())
