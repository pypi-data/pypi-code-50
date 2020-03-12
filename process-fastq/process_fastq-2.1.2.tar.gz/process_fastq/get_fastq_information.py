# -*- coding: utf-8 -*-
"""
get_fastq_information
~~~~~~~~~~~~~~~
:Description: this function helps to get_fastq_read_length and get_fastq
"""
"""
Created on July 26, 2019
Description: this function helps to get_fastq_read_length and get_fastq
@author: Ronak H Shah
"""


import os
import glob
import logging
import subprocess

# Making logging possible
logger = logging.getLogger("process_fastq")


def get_fastq(dir_path):
    logger.info("get_fastq_information: get_fastq: Globbing fastq.gz file")
    R1_pattern = "*_R1_*.gz"
    R2_pattern = "*_R2_*.gz"
    logger.debug(
        "get_fastq_information: get_fastq: Path to search for fastq: %s", dir_path
    )
    glob_path_R1 = os.path.join(dir_path, R1_pattern)
    glob_path_R2 = os.path.join(dir_path, R2_pattern)
    glob_path_R1 = glob.glob(glob_path_R1)
    glob_path_R2 = glob.glob(glob_path_R2)
    logger.info("get_fastq_information: get_fastq: Done globbing fastq.gz file")
    return ["".join(glob_path_R1), "".join(glob_path_R2)]


def get_fastq_read_length(fastq_list):
    logger.info(
        "get_fastq_information: get_fastq_read_length: getting the read length of each fastq file"
    )
    read_length_list = []
    for fastq in fastq_list:
        cmd = (
            "zcat"
            + " "
            + fastq
            + " | head -n 2 | "
            + "grep -v ^@ | "
            + "tr -d "
            + "'\n'"
        )
        logger.debug(
            "get_fastq_information: get_fastq_read_length: the commandline is %s",
            cmd.encode("unicode_escape").decode("utf-8"),
        )
        out = subprocess.Popen(
            (cmd),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
        )
        stdout, stderr = out.communicate()
        if stderr is None:
            logger.debug(
                "get_fastq_information: get_fastq_read_length: Read: %s",
                stdout.decode("utf-8"),
            )
            read_length = len(stdout)
        else:
            logger.error(
                "get_fastq_information: get_fastq_read_length: could not calcualte the read for: %s",
                fastq,
            )
            exit(1)
        read_length_list.append(read_length)
    return read_length_list
