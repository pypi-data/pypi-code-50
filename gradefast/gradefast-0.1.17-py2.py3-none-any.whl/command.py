"""
Command module allows executing ad hoc commands
"""
import os
import signal
import logging
import datetime
import subprocess

from gradefast import logconfig

logger = logconfig.configure_and_get_logger(__name__)

class Command:
    """
    A runnable command

    A command in :class:`gradefast.test.GFCommandTest` gets executed to
    return a result, comment and exceptions.
    
    Alternatively, a command can be executed before or after a test runs
    like for moving student's code before execution and deleting it when
    test is done. 
    
    A long running command can be started before a test like a socket server
    that listens for input.

    Parameters
    ----------
    name: str 
        Identifier of the command. If multiple words, use "_" (underscores) to
        concatenate them

    command_builder: function
        A function that gets called with submission, *args and **kwargs

    long_running: bool, optional
        Is the function long running? Default is False

    working_directory: str, optional
        Directory from where the command is executed

    timeout: float, optional 
        Seconds to wait before the process completes
    
    log_directory: str, optional
        Writes log at specified directory. Default is current working directory

    args: tuple, optional
        Arguments passed to command_builder

    kwargs: namedtuple, optional
        Named arguments passed to command_builder

    Attributes
    ----------
    name: str

    command_builder: function

    long_running: bool

    cwd: str

    timeout: float

    args: tuple

    kwargs: namedtuple

    """
    def __init__(self, name, command_builder, *args, working_directory='.', long_running=False,
    timeout=None, log_directory='.', **kwargs):
        self.name = name
        self.command_builder = command_builder
        self.long_running = long_running
        self.cwd = working_directory
        self.timeout = timeout
        self.log_directory = log_directory
        self.args = args
        self.kwargs = kwargs

    def build_command(self, submission):
        return self.command_builder(submission, *self.args, **self.kwargs)

    def create_and_write_message_to_file(self, message, file_type):
        if message != None:
            if not os.path.exists(self.log_directory):
                os.makedirs(self.log_directory)
                
            output_file_path = os.path.join(self.log_directory, 
            file_type + '_command{}.txt'.format('_' + self.name))

            with open(output_file_path, 'a') as output_file:
                # write date and time for context
                output_file.write(datetime.datetime.now().strftime("%c") + " - ")
                # write name of the command
                output_file.write(self.name + "\n")
                output_file.write(message)

    def write_logs(self, out, err):
        self.create_and_write_message_to_file(out, 'output')
        self.create_and_write_message_to_file(err, 'error')

    def run(self, submission):
        """
        Runs the command on a single submission. Creates log files that contains output
        (stdout) and error (stderr) obtained from running the command.

        Parameters
        ----------
        submission: `~gradefast.submission.Submission`

        Returns
        -------

        """
        command = self.build_command(submission)
        if type(command) == str:
            shell = True
        elif type(command) == list:
            shell = False
        
        self.proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
        shell=shell, preexec_fn=os.setsid, cwd=self.cwd)
        out, err = None, None
        self.status = 'RUNNING'
        if not self.long_running:
            out, err = self.proc.communicate(timeout=self.timeout)
            self.status = 'FINISHED'
        if out != None:
            out = out.decode('utf-8')
        if err != None:
            err = err.decode('utf-8')
            if err != '':
                logger.error("Error when attempting to run command {} ".format(self) \
                + "on submission {} and the error was {}".format(submission, err), exc_info=None)
        self.write_logs(out, err)
        return self.proc, out, err

    def kill(self):
        """
        Kills the running command

        Returns
        -------
        out, err 

        """
        os.killpg(os.getpgid(self.proc.pid), signal.SIGTERM)
        out, errs = self.proc.communicate()
        return out, errs
