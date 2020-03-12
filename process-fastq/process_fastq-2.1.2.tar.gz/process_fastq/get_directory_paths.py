# -*- coding: utf-8 -*-

"""
get_directory_paths
~~~~~~~~~~~~~~~
:Description: this function helps to create and provide directories
"""
"""
Created on July 26, 2019
Description: this function helps to create and provide directories
@author: Ronak H Shah
"""
import os
import logging
import glob
import subprocess
import re
import pathlib
from collections import defaultdict

# Making logging possible
logger = logging.getLogger("process_fastq")


def make_path(dir_path, sample_id, run_id, request_id):
    logger.info(
        "get_directory_paths: make_pathMaking file path to search for files")
    if run_id:
        glob_run_id = "*" + run_id + "*"
    else:
        glob_run_id = "*"
    logger.debug(
        "get_directory_paths: make_path: glob_run_id: %s", glob_run_id)
    if request_id:
        glob_request_id = "*" + request_id + "*"
    else:
        glob_request_id = "*Proj*"
    logger.debug(
        "get_directory_paths: make_path: glob_request_id: %s", glob_request_id)
    glob_sample_id = "*_" + sample_id + "$"
    logger.debug(
        "get_directory_paths: make_path: glob_sample_id: %s", glob_sample_id)
    glob_path = os.path.join(dir_path, glob_run_id,
                             glob_request_id)
    logger.debug("get_directory_paths: make_path: glob_path: %s", glob_path)

    """
    find /ifs/archive/GCL/hiseq/FASTQ/ -maxdepth 3 -type d -name "*MSK-ML-0055-03-5001542C*" 2>&1 | grep -v "Permission denied"
    """
    if run_id is None or request_id is None:
        logger.warning(
            "get_directory_paths: make_path: As run id and request id are not provided we will use find to get fastq directories."
        )
        logger.warning(
            "get_directory_paths: make_path: Please be aware that this will take significantly longer to run."
        )
        cmd = (
            "find "
            + glob_path
            + " -maxdepth 1 -type d -regex "
            + '"'
            + glob_sample_id
            + '"'
            + " 2>&1 | grep -v "
            + '"Permission denied"'
        )
        logger.debug(
            "get_directory_paths: make_path: the commandline is %s",
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
                "get_directory_paths: make_path: Read: %s", stdout.decode(
                    "utf-8")
            )
            glob_path = stdout.decode("utf-8").split("\n")[:-1]
        else:
            logger.error(
                "get_directory_paths: make_path: could not find the fastq files for: %s",
                sample_id,
            )
            exit(1)
        ext_project_id = []
        ext_run_dict = defaultdict(list)
        for m_path in glob_path:
            p_path = pathlib.Path(m_path)
            e_run_id = p_path.parent.parent.name
            a_pattern = re.compile("_A\d{1}$")
            if re.search(a_pattern, str(e_run_id)):
                e_run_id = re.sub(
                    str(a_pattern.search(str(e_run_id)).group()), "", e_run_id
                )
            else:
                pass
            ext_run_dict[e_run_id].append(m_path)
            e_project_id = p_path.parent.name
            if e_project_id in ext_project_id:
                pass
            else:
                ext_project_id.append(e_project_id)
        if len(ext_project_id) > 1:
            logger.error(
                "get_directory_paths: make_path: the sample id belongs to multiple project, please provide a unique sample id"
            )
            exit(1)
        glob_path = []
        for m_id, m_path in ext_run_dict.items():
            sort_m_path = sorted(m_path)
            glob_path.append(sort_m_path.pop())
    else:
        glob_path = glob.glob(glob_path)
        if len(glob_path) > 1:
            ext_project_id = []
            ext_run_dict = defaultdict(list)
            for m_path in glob_path:
                p_path = pathlib.Path(m_path)
                e_run_id = p_path.parent.parent.name
                a_pattern = re.compile("_A\d{1}$")
                if re.search(a_pattern, str(e_run_id)):
                    e_run_id = re.sub(
                        str(a_pattern.search(str(e_run_id)).group()), "", e_run_id
                    )
                else:
                    pass
                ext_run_dict[e_run_id].append(m_path)
                e_project_id = p_path.parent.name
                if e_project_id in ext_project_id:
                    pass
                else:
                    ext_project_id.append(e_project_id)
            glob_path = []
            for m_id, m_path in ext_run_dict.items():
                sort_m_path = sorted(m_path)
                glob_path.append(sort_m_path.pop())
        else:
            pass
    logger.debug(
        "get_directory_paths: make_path: glob glob_path: %s", glob_path)
    logger.info(
        "get_directory_paths: make_path: Finished making file path to search for files"
    )
    if run_id is None or request_id is None:
        return glob_path
    else:
        return "".join(glob_path)
