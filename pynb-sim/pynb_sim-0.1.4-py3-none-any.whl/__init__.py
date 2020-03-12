__version__ = "0.1.4"
from .ji import widget, progress_text
from .progress import ProgressFileReader
from IPython.core.display import display, HTML


def simulate(command, progress_reader=None):
    from IPython.display import clear_output
    import subprocess, base64
    process = subprocess.Popen(command, shell=True)

    if progress_reader:
        for progress_message in progress_reader.listen(process):
            clear_output()
            display(HTML("Simulated " + str(progress_message.progression) + " out of " + str(progress_message.duration) + " milliseconds"))
