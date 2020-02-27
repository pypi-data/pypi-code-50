import difflib
import io
from dataclasses import dataclass

import cl_bindgen.processfile

@dataclass
class BatchEntry:
    batch_file : str # batchfile to process
    compare_to : str # file to compare the result to

@dataclass
class FileEntry:
    options: cl_bindgen.processfile.ProcessOptions
    compare_to :str

def perform_diff(result, original):
    """ Compares `result` to `original` """
    with open(result) as f:
        result_txt = f.readlines()
    with open(original) as f:
        original_txt = f.readlines()

    with io.StringIO() as output_stream:
        for line in  difflib.unified_diff(result, original):
            output_stream.write(line)
        return output_stream.get_value()

def test_batch_file(entry):
