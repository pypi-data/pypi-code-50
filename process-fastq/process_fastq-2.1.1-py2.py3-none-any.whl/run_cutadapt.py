# -*- coding: utf-8 -*-

"""
run_cutadapt
~~~~~~~~~~~~~~~
:Description: this function helps to run cutadapt to trim reads larger then expected read length
"""
"""
Created on July 26, 2019
Description: this function helps to run cutadapt to trim reads larger then expected read length
@author: Ronak H Shah
"""

import os
import logging
import subprocess
import pathlib
import tempfile

# Making logging possible
logger = logging.getLogger("process_fastq")


def run(cutadapt_path, output_path, fastq_list, trim_length):
    p_path_1 = pathlib.Path(fastq_list[0])
    sample_id_1 = p_path_1.name
    p_path_2 = pathlib.Path(fastq_list[1])
    sample_id_2 = p_path_2.name
    tmp_fo = tempfile.mkdtemp(dir=output_path, prefix="cutadapt_")
    out_file_path_1 = os.path.join(tmp_fo, sample_id_1)
    out_file_path_2 = os.path.join(tmp_fo, sample_id_2)
    cmd = (
        cutadapt_path
        + " --action none -l "
        + str(trim_length)
        + " -o "
        + out_file_path_1
        + " -p "
        + out_file_path_2
        + " "
        + fastq_list[0]
        + " "
        + fastq_list[1]
    )
    logger.debug(
        "run_cutadapt: run: the commandline is %s",
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
        logger.debug("run_cutadapt: run: Read: %s", stdout.decode("utf-8"))
    else:
        logger.error(
            "run_cutadapt: run: could not run cutadapt for: %s and %s",
            sample_id_1,
            sample_id_2,
        )
        exit(1)
    return [out_file_path_1, out_file_path_2]
