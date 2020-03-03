import inspect
import linecache
import os
import ast
import readline
import sys
import traceback
from traceback import FrameSummary

from scrybe.internal.code_capture.source_code import CodeCapture
from scrybe.internal.util import get_module_name, is_site_package_file


class FrameHelper(object):
    @classmethod
    def __is_pycharm_interactive_fname__(cls, fname: str):
        return fname == '<input>'

    @classmethod
    def __is_pyinterpreter_fname__(cls, fname: str):
        return fname == '<stdin>'

    @classmethod
    def __is_interactive_fname__(cls, fname: str):
        return cls.__is_pycharm_interactive_fname__(fname=fname) or cls.__is_pyinterpreter_fname__(fname=fname)

    @classmethod
    def __extract_source_line__(cls, frame):
        # FIXME(msachdev): This has many issues at the moment and is unused...
        src_line = ""
        if frame.line and len(frame.line) > 0:
            src_line = frame.line
        elif cls.__is_pycharm_interactive_fname__(fname=frame.filename):
            prev_frame = inspect.currentframe().f_back
            if prev_frame and prev_frame.f_code.co_name == "runcode":
                source_lines = prev_frame.f_back.f_locals['source'].split('\n')
                src_line = source_lines[frame.lineno - frame.frame.f_code.co_firstlineno]
        elif cls.__is_pyinterpreter_fname__(fname=frame.filename):
            src_line = readline.get_history_item(readline.get_current_history_length())
        return src_line

    @staticmethod
    def is_same_frame(left_frame: FrameSummary, right_frame: FrameSummary):
        return left_frame.filename == right_frame.filename and \
               left_frame.lineno == right_frame.lineno

    @staticmethod
    def is_before_in_file(left_frame: FrameSummary, right_frame: FrameSummary):
        return left_frame.filename == right_frame.filename and \
               left_frame.lineno < right_frame.lineno

    @staticmethod
    def is_after_in_file(left_frame: FrameSummary, right_frame: FrameSummary):
        return left_frame.filename == right_frame.filename and \
               left_frame.lineno > right_frame.lineno

    @staticmethod
    def to_string(frame: FrameSummary):
        info = dict(fname=frame.filename, lineno=frame.lineno, fn_name=frame.name, src_line=frame.line)
        return "[{fname}:{lineno}] :: {src_line}".format(**info)

    @classmethod
    def is_interactive_input(cls, frame: FrameSummary):
        return cls.__is_interactive_fname__(fname=frame.filename)

    @classmethod
    def is_interperter_frame(cls, frame: FrameSummary):
        if CodeCapture.is_zeppelin() and not CodeCapture.is_ipython():
            return "__main__" in sys.modules and hasattr(sys.modules["__main__"], "__file__") and sys.modules[
                "__main__"].__file__ == frame.filename
        return "PyCharm" in frame.filename or 'IPython/core' in frame.filename or 'ipykernel' in frame.filename


class SourceContext(object):
    STACK_FETCH_LIMIT = 15
    MAX_CONTEXT_LINES_BEFORE = 12
    SCRYBE_INTERNAL_PATH = os.path.join('scrybe', 'internal')

    def __init__(self):
        self.stack_frames = list()

    @classmethod
    def extract(cls, frame_gen, limit=None):
        # Code copied from traceback.StackSummary.extract and removed the code to cache the files
        import collections
        import itertools
        if limit is None:
            limit = getattr(sys, 'tracebacklimit', None)
            if limit is not None and limit < 0:
                limit = 0
        if limit is not None:
            if limit >= 0:
                frame_gen = itertools.islice(frame_gen, limit)
            else:
                frame_gen = collections.deque(frame_gen, maxlen=-limit)

        result = traceback.StackSummary()
        for f, lineno in frame_gen:
            co = f.f_code
            filename = co.co_filename
            # Doing a quick check to ignore Scrybe frames.
            # Checking frame using get_module_name turns out to be expensive
            # if get_module_name(f).startswith('scrybe'):
            #     continue
            if cls.SCRYBE_INTERNAL_PATH in filename:
                continue
            name = co.co_name
            if CodeCapture.is_zeppelin() and name and filename == "<stdin>":
                if name.startswith("<") and name.endswith(">"):
                    name = "%s:%s" % (name, CodeCapture.zeppelin_execution_key)
                elif name in CodeCapture.module_zeppelin_code_mapping:
                    name = "%s:%s" % (name, CodeCapture.module_zeppelin_code_mapping[name])
                elif hasattr(f, "f_locals") and "self" in f.f_locals:
                    try:
                        class_name = f.f_locals["self"].__class__.__name__
                        name = "%s.%s" % (class_name, name)
                        if name in CodeCapture.module_zeppelin_code_mapping:
                            name = "%s:%s" % (name, CodeCapture.module_zeppelin_code_mapping[name])
                    except:
                        pass
            result.append(FrameSummary(
                filename, lineno, name, lookup_line=False, locals=None))
        return result

    @classmethod
    def capture_current_context(cls):
        src_ctxt = SourceContext()
        frame_to_extract = sys._getframe()
        while frame_to_extract is not None:
            module_name = get_module_name(frame_to_extract)
            if module_name.startswith('scrybe'):
                frame_to_extract = frame_to_extract.f_back
            else:
                break
        src_ctxt.stack_frames = cls.extract(traceback.walk_stack(frame_to_extract), limit=cls.STACK_FETCH_LIMIT)
        return src_ctxt

    @classmethod
    def get_src_line_from_cache(cls, filename, lineno, name):
        if CodeCapture.is_zeppelin() and filename == "<stdin>":
            try:
                if not name:
                    return ""
                input_keys = name.split(":")
                if len(input_keys) <= 1:
                    return ""
                input_key = input_keys[-1]
                if input_key in CodeCapture.zeppelin_code_dict:
                    code = CodeCapture.zeppelin_code_dict[input_key]
                    code = code.split("\n")
                    line_index = lineno - 1
                    if line_index < len(code):
                        return code[line_index]
                return ""
            except:
                return ""
        else:
            return linecache.getline(filename, lineno)

    @classmethod
    def get_context_lines_for_frame(cls, frame: FrameSummary):
        min_strip = 10000
        src_lines_tmp = []
        src_lines = []
        for i in range(cls.MAX_CONTEXT_LINES_BEFORE):
            src_line = cls.get_src_line_from_cache(frame.filename, frame.lineno - i, frame.name)
            leading_spaces = len(src_line) - len(src_line.lstrip())
            stripped_line = src_line.strip()
            if stripped_line and min_strip > leading_spaces:
                min_strip = leading_spaces
            if stripped_line:
                src_lines_tmp.append((stripped_line, leading_spaces))
            if len(src_lines_tmp) > 0:
                src_lines = [' ' * (leading_spaces - min_strip) + s for s, leading_spaces in src_lines_tmp if
                             len(s) > 0]
                src_lines.reverse()
                if SourceContext._is_python_statement(text="\n".join(src_lines)):
                    break
        return src_lines

    def compare(self, other: 'SourceContext'):
        self_idx = len(self.stack_frames) - 1
        other_idx = len(other.stack_frames) - 1
        while self_idx >= 0 and other_idx >= 0:
            if FrameHelper.is_same_frame(left_frame=self.stack_frames[self_idx],
                                         right_frame=other.stack_frames[other_idx]):
                self_idx -= 1
                other_idx -= 1
            elif FrameHelper.is_before_in_file(left_frame=self.stack_frames[self_idx],
                                               right_frame=other.stack_frames[other_idx]):
                return -1
            elif FrameHelper.is_after_in_file(left_frame=self.stack_frames[self_idx],
                                              right_frame=other.stack_frames[other_idx]):
                return 1
            else:
                return -2
        return -1 if self_idx < other_idx else (1 if other_idx > self_idx else 0)

    @staticmethod
    def _is_python_statement(text):
        try:
            ast.parse(text)
            return True
        except Exception as e:
            return False

    @staticmethod
    def __find_highest_interpreter_frame__(frames):
        frame_idx = [i for i in range(len(frames)) if FrameHelper.is_interperter_frame(frames[i])]
        return frame_idx[0] if len(frame_idx) > 0 else -1

    def get_src_line_based_on_current_stack(self) -> FrameSummary:
        curr_stack_frames = self.capture_current_context().stack_frames
        first_non_interpreter_frame = SourceContext.__find_highest_interpreter_frame__(frames=self.stack_frames) - 1
        if first_non_interpreter_frame < 0:
            self_idx = len(self.stack_frames) - 1
            first_non_interpreter_frame = self_idx
        else:
            self_idx = first_non_interpreter_frame
        curr_idx = SourceContext.__find_highest_interpreter_frame__(frames=curr_stack_frames) - 1
        if curr_idx < 0:
            curr_idx = len(curr_stack_frames) - 1
        final_frame = None
        while self_idx >= 0 and curr_idx >= 0:
            self_frame = self.stack_frames[self_idx]
            curr_frame = curr_stack_frames[curr_idx]
            if FrameHelper.is_same_frame(left_frame=self_frame, right_frame=curr_frame):
                self_idx -= 1
                curr_idx -= 1
            elif self_frame.name != curr_frame.name and self_idx < first_non_interpreter_frame:
                # This is a very specific case -- basically we are saying that the previous frame was identical
                # down to the filename and lineno but next frame is occuring inside two different functions
                # This can happen in cases where you are doing inline execution, e.g.,
                # Example 1: a, b = (<expr-one>, <expr-two>)
                # Example 2: out = my_func(df['mycol']) -- in this case, the inner expression invokes __getitem__
                # In such cases, we should pick the previous frame since the execution diverged there itself
                final_frame = self.stack_frames[self_idx + 1]
                break
            else:
                final_frame = self_frame
                break
        final_frame_maybe_in_lib = final_frame
        while final_frame is not None and is_site_package_file(
                filename=os.path.abspath(final_frame.filename)) and self_idx < first_non_interpreter_frame:
            self_idx += 1
            final_frame = self.stack_frames[self_idx]
        if final_frame is not None and is_site_package_file(filename=os.path.abspath(final_frame.filename)):
            return final_frame_maybe_in_lib
        return final_frame
