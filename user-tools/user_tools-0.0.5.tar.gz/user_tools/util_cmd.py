#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Some functions related to command execution."""
import subprocess


def get_out_text(cmd):
    """Run command with arguments and return its output.

    cmd(list): Command to be executed.
        The cmd format is ["command", ["arg", "arg1",...]]
    """

    code = 0
    try:
        out_bytes = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        out_bytes = e.output
        code = e.returncode
    out_text = out_bytes.decode('utf-8')
    if code:
        out_text = "Error code is " + code + "\n" +\
                   "Output text is" + out_bytes.decode('utf-8')
    else:
        out_text = "Output text is" + out_bytes.decode('utf-8')
    return out_text
