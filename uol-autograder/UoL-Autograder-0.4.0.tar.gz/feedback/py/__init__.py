import json
import subprocess
import sys, os
from collections import namedtuple
from tempfile import TemporaryFile
from pathlib import Path
from ..general import util
from ..general import Runner
from ..general.contants import *
from ..general.result import CheckResult
from ..py.py_eval_util import get_eval_util_path

class PyLookup(util.Lookup):
    _runner_feedback = "py_runner_feedback.json"
    _eval_feedback = "py_eval_feedback.json"

class PyRunner(Runner):
    def __init__(self, tmp_files, run_args={}):
        super(PyRunner, self).__init__(tmp_files, run_args)
        self.py_lookup = PyLookup(tmp_files.lookup_dir)
        if self.verbose: print(f"Working dir: {tmp_files.tmp_dir}")

        self._test_lookup = {
            "syntax": self.test_syntax,
            "functionality": self.test_functionality,
            "comments": self.test_comments,
        }


    def run_test(self, config):
        self.feedbacks = []

        for test in config:
            self._test_lookup[test["type"]](util.dict_to_namedtuple(test))

        return self.feedbacks
        

    def test_syntax(self, config):
        if self.verbose: print("Testing syntax")
        # Here we check whether the code runs
        retval, _, output = util.execute([PY_RUNNER, self.tested_path], self.tmp_dir)

        runs = retval == 0

        # Provide feedback
        with self.py_lookup.runner_feedback.open() as json_file:
            syntax_feedback = json.load(json_file)
        
        feedback = [syntax_feedback[PASS if retval == 0 else FAIL]]
        if not runs:
            feedback.append(util.as_md_code(output))
            if self.verbose: print(f"Error output:\n{output}")

        # create feedback dictionary file
        self.feedbacks.append(CheckResult(config, "syntax", 1 if retval == 0 else 0, '\n'.join(feedback)))


    def test_functionality(self, config):
        if self.verbose: print("Testing functionality")
        output_file = Path(self.tmp_files.tmp_dir.name, "result.json")
      
        # Run tester file that evaluates tested file
        args = [PY_RUNNER, config.tester_file.absolute().as_posix(), self.tested_path, output_file.absolute().as_posix(), get_eval_util_path()]
        _, stdout, stderr = util.execute(args, self.tmp_dir)
        if self.verbose: print(f"stdout:\n{stdout}\nstderr:\n{stderr}")

        if not output_file.is_file():
            self.feedbacks.append(CheckResult(config, "functionality", 0, "Test execution failed"))
        else:
            # Read results file
            with output_file.open() as json_file:
                result = json.load(json_file)
            
            # Combine scores from test feedback
            score = sum([test['mark'] * test['weight'] for test in result])

            for i, r in enumerate(result):
                self.feedbacks.append(
                    CheckResult(config, r["question"], r["mark"], r["feedback"], i + 1, r["weight"])
                )
