import click
import datetime
import base64
from slims_lisp.slims import Slims

@click.group()
def cli():
    """ \b
A high-level CLI for SLIMS REST API
    """
    pass

@cli.command()
@click.option('--url',
    help = 'SLIMS REST URL (ex: https://<your_slims_address>/rest/rest).',
    prompt = 'SLIMS REST URL (ex: https://<your_slims_address>/rest/rest)',
    required = True)
@click.option('--proj',
    default = '',
    help = 'Project name (if any).',
    prompt = 'Project name (if any)')
@click.option('--exp',
    help = 'Experiment name.',
    prompt = 'Experiment name',
    required = True)
@click.option('--step',
    default = 'data_collection',
    help = 'Experiment step name.',
    prompt = 'Experiment step name',
    required = True,
    show_default = True)
@click.option('--active',
    help = 'Search only in active or inactive steps (or in both).',
    type = click.Choice(['true', 'false', 'both'],
        case_sensitive = False),
    default = 'true',
    required = False,
    show_default = True)
@click.option('--attm',
    help = 'Attachment name.',
    prompt = 'Attachment name',
    required = True)
@click.option('--linked',
    help = 'Search only linked or unlinked attachments (or both).',
    type = click.Choice(['true', 'false', 'both'],
        case_sensitive = False),
    default = 'true',
    required = False,
    show_default = True)
@click.option('--output_dir',
    default = '',
    help = 'Output directory [default: working directory].',
    prompt = 'Output directory')
@click.option('-v', '--verbose',
    is_flag = True,
    help = 'Print various messages.')
@click.option('-u', '--username',
    help = 'User name.',
    prompt = 'User name',
    required = True)
@click.option('-p', '--pwd',
    help = 'Password.',
    prompt = 'Password',
    hide_input = True,
    required = True)
def fetch(url, username, pwd, proj, exp, step, active, attm, linked, output_dir, verbose):
    """\b
Download a file from a SLIMS experiment attachment step.


Return:

    Returns the HTTP GET request response.


Output:

    Generates two files (by default in the working directory):

        -<output_dir>/<attm>               The requested file\n
        -<output_dir>/<attm>_metadata.txt  Associated metadata in a JSON format


Example:

    $ slims-lisp fetch --url <your_slims_url> \
--proj <your_project_name> \
--exp <your_experiment_name> \
--step <your_attachment_step_name> \
--attm <your_attachment_name>
    """

    slims = Slims(url = url,
        username = username,
        pwd = pwd)
    response = slims.download_attachment(proj = proj,
        exp = exp,
        step = step,
        active = active,
        attm = attm,
        linked = linked,
        output_dir = output_dir,
        verbose = verbose
    )
    return response

@cli.command()
@click.option('--url',
    help = 'SLIMS REST URL. ex: https://<your_slims_address>/rest/rest',
    prompt = 'SLIMS REST URL (ex: https://<your_slims_address>/rest/rest)',
    required = True)
@click.option('--proj',
    default = '',
    help = 'Project name (if any).',
    prompt = 'Project name (if any)')
@click.option('--exp',
    help = 'Experiment name.',
    prompt = 'Experiment name',
    required = True)
@click.option('--step',
    default = 'results',
    help = 'Experiment step name.',
    prompt = 'Experiment step name',
    required = True,
    show_default = True)
@click.option('--active',
    help = 'Search only in active or inactive steps (or in both).',
    type = click.Choice(['true', 'false', 'both'],
        case_sensitive = False),
    default = 'true',
    required = False,
    show_default = True)
@click.option('--file',
    help = 'Path to the file that will be uploaded.',
    prompt = 'Path to the file that will be uploaded',
    required = True)
@click.option('--attm',
    help = 'A name to give to the attachement that will be created. [default: same as --file]',
    required = False)
@click.option('-v', '--verbose',
    is_flag = True,
    help = 'Print various messages.')
@click.option('-u', '--username',
    help = 'User name.',
    prompt = "User name",
    required = True)
@click.option('-p', '--pwd',
    help = 'Password.',
    prompt = 'Password',
    hide_input = True,
    required = True)
def add(url, username, pwd, proj, exp, step, active, file, attm, verbose):
    """\b
Upload a file to a an existing SLIMS experiment attachment step.


Return:

    Returns the HTTP POST request response.


Example:

    $ slims-lisp add --url <your_slims_url> \
--proj <your_project_name> \
--exp <your_experiment_name> \
--step <your_attachment_step_name> \
--file <path/to/your/file>
    """

    slims = Slims(url = url,
        username = username,
        pwd = pwd)
    response = slims.upload_attachment(proj = proj,
        exp = exp,
        step = step,
        active = active,
        file = file,
        attm = attm,
        verbose = verbose
    )
    return response

@cli.command()
@click.option('--url',
    help = 'SLIMS REST URL. ex: https://<your_slims_address>/rest/rest',
    prompt = 'SLIMS REST URL (ex: https://<your_slims_address>/rest/rest)',
    required = True)
@click.option('--proj',
    default = '',
    help = 'Project name (if any).',
    prompt = 'Project name (if any)')
@click.option('--exp',
    help = 'Experiment name.',
    prompt = 'Experiment name',
    required = True)
@click.option('--files',
    help = 'Comma-delimited paths to the files that will be uploaded.',
    prompt = 'Comma-delimited paths to the files that will be uploaded',
    required = True)
@click.option('--title',
    default = '',
    help = 'The title of the attachment block that will be created for the dataset in SLIMS.  [default: dataset_<ISO 8601 timestamp>]',
    prompt = 'The title of the attachment block that will be created for the dataset in SLIMS.  [default: dataset_<ISO 8601 timestamp>]')
@click.option('-v', '--verbose',
    is_flag = True,
    help = 'Print various messages.')
@click.option('-u', '--username',
    help = 'User name.',
    prompt = 'User name',
    required = True)
@click.option('-p', '--pwd',
    help = 'Password.',
    prompt = 'Password',
    hide_input = True,
    required = True)
def add_dataset(url, username, pwd, proj, exp, files, title, verbose):
    """\b
Create a new SLIMS experiment attachment step and upload multiple files to it \
(useful to upload a whole dataset containing multiple data and/or metadata files at once).


Return:

    Returns HTTP POST requests responses in a dictionary.


Example:

    $ slims-lisp add-dataset --url <your_slims_url> \
--proj <your_project_name> \
--exp <your_experiment_name> \
--files <file1>,<file2>,<file3> \
--title <your_dataset_name>
    """

    if title == "":
        title = "dataset_" + datetime.datetime.now(
                datetime.timezone.utc
            ).isoformat(sep='T')

    slims = Slims(url = url,
        username = username,
        pwd = pwd)
    response = dict()
    response[title] = slims.create_attachment_step(proj = proj,
        exp = exp,
        title = title,
        verbose = verbose
    )

    for file in files.strip().split(','):
        with open(file, "rb") as f:
            response[file] = slims.post(table = "/repo",
                    headers = {"Content-Type":"application/json"},
                    json = {"atln_recordTable":"ExperimentRunStep",
                    "atln_recordPk":str(response[title].json()["entities"][0]['pk']),
                    "attm_name":file,
                    "contents":base64.b64encode(f.read()).decode("utf-8")},
                    stream = True
            )
        if verbose is True and response[file].status_code == 200:
            print("Added '" + file +
            "'. to step '" + title +
            "'."
            )
        elif response[file].status_code != 200:
            print("Warning: could not add '" + file +
            "' to step '" + title +
            "'. Response status " + str(response[file].status_code)
            )

    return response

if __name__ == '__main__':
    cli()
