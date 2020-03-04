import logging
import tempfile

from cliff.command import Command

import cray.jobs as jobs


class Submit(Command):
    "Submits the current working directory to the batch processing system"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Submit, self).get_parser(prog_name)
        parser.add_argument(
            "-t",
            "--ticket",
            required=True,
            help="Jira ticket identifier",
            type=str,
            dest="ticket",
        )
        parser.add_argument(
            "-d",
            "--description",
            required=True,
            help="A description of the job",
            type=str,
            dest="desc",
        )
        parser.add_argument(
            "-s",
            "--ssh-dir",
            required=False,
            default="",
            help="Path to the ssh directory, if not provided, will not bind the SSH directory",
            type=str,
            dest="ssh_dir",
        )
        parser.add_argument(
            "--docker-image",
            required=False,
            default="senseyeio/cray-builder:latest",
            help="Docker image used to build the job",
            type=str,
            dest="docker_image",
        )
        parser.add_argument(
            "-w",
            "--fix-windows-path",
            required=False,
            default=False,
            help="This will fix paths on windows to make them unixlike",
            dest="fix_windows_path",
            action="store_true",
        )
        parser.add_argument(
            "-c",
            "--config",
            required=False,
            default="",
            help="Path to configuration file",
            type=str,
            dest="config",
        )
        parser.add_argument(
            "--tempdir",
            required=False,
            default="",
            help="Directory to use in place of tempdir",
            type=str,
            dest="tempdir",
        )
        parser.add_argument(
            "-e",
            "--env",
            required=False,
            nargs="+",
            action="append",
            help="Add optional environment variables to be passed to build process",
        )
        return parser

    def take_action(self, parsed_args):
        ticket = parsed_args.ticket
        desc = parsed_args.desc.replace(" ", "_")
        jobID = "{}#{}".format(ticket, desc)
        ssh_dir = parsed_args.ssh_dir
        fix_windows_path = parsed_args.fix_windows_path
        docker_image = parsed_args.docker_image
        config = parsed_args.config
        alt_tempdir = parsed_args.tempdir
        environment = parsed_args.env
        if environment:
            environment = [ei[0] for ei in environment]
        self.log.debug("Ticket={} Desc={} JobID={}".format(ticket, desc, jobID))

        if jobs.exists(jobID):
            raise Exception("Duplicate job: '{}'".format(jobID))

        if alt_tempdir:
            jobs.build_job_archive(
                alt_tempdir,
                config,
                ssh_dir,
                fix_windows_path,
                docker_image,
                environment,
            )
            jobs.submit_job_zip("{}/job.zip".format(alt_tempdir), jobID)
        else:
            with tempfile.TemporaryDirectory() as tempdir:
                jobs.build_job_archive(
                    tempdir,
                    config,
                    ssh_dir,
                    fix_windows_path,
                    docker_image,
                    environment,
                )
                jobs.submit_job_zip("{}/job.zip".format(tempdir), jobID)

        self.log.info("Created job {}".format(jobID))
