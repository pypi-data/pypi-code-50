#
# This command is python2 and 3 compatible
#

from __future__ import print_function

import os
import shutil
import subprocess
import sys
import textwrap

from docopt import docopt

from cloudmesh_cmsd.cmsd.__version__ import version
from cloudmesh.common.util import path_expand
from cloudmesh.common.StopWatch import StopWatch

DOCKERFILE = """
FROM python:3.8.2-buster

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y --no-install-recommends install \
    build-essential \
    git \
    curl \
    wget \
    sudo \
    net-tools \
    gnupg dos2unix

RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
RUN echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.2 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list

RUN apt-get -y update
RUN apt-get install -y mongodb-org-shell


#
# the display setting does not work
#
# CMD export DISPLAY =":0.0"

RUN pip install pip -U 
RUN pip install cloudmesh-installer

RUN mkdir cm
WORKDIR cm

RUN cloudmesh-installer get cms cloud openstack aws azure

RUN mkdir $HOME/.cloudmesh
RUN mkdir $HOME/.ssh

COPY init.sh /
RUN dos2unix /init.sh
RUN chmod +x /init.sh

ENTRYPOINT /bin/bash /init.sh; /bin/bash

#docker run --rm -d -v /aux/github/cm/docker/mongo_data:/data/db -p 127.0.0.1:27017:27017/tcp --name mongos mongo:4.2
#docker run --rm -it -v /aux/github/cm/docker/cloudmesh_home:/root/.cloudmesh -v ~/.ssh:/root/.ssh --net host --name cms-container cloudmesh-cms
"""

INIT_SH = """
#!/bin/bash

cloudmesh-installer git pull cms
cloudmesh-installer git pull cloud
cloudmesh-installer git pull aws
cloudmesh-installer git pull azure
cloudmesh-installer git pull openstack
"""

DEFAULT_CLOUDMESH_CONFIG_DIR = os.getenv(
    "CLOUDMESH_CONFIG_DIR",
    path_expand("~/.cloudmesh")
)
DEFAULT_SSH_DIR = path_expand("~/.ssh")

CMS_CONTAINER_NAME = "cloudmesh-cms"
MONGO_CONTAINER_NAME = "cloudmesh-mongo"
CMS_IMAGE_NAME = "cloudmesh/cms"
MONGO_IMAGE = "mongo:4.2"
MONGO_VOLUME_NAME = "cloudmesh-mongo-vol"


def _run_os_command(cmd_str):
    out = subprocess.check_output(cmd_str).decode("utf-8")
    return out.strip() if not None else None


def _docker_exec(cmd_str, container_name=CMS_CONTAINER_NAME):
    if isinstance(cmd_str, list):
        cmd = ["docker", "exec", container_name]
        cmd.extend(cmd_str)
        return _run_os_command(cmd)
    else:
        os.system(f"docker exec {container_name} " + cmd_str)


def _is_container_running(name):
    output = _run_os_command(["docker", "container", "ls",
                              "--filter", f"name={name}",
                              "--format", "\"{{.Names}}\""])

    return name in output


def _is_container_available(name):
    output = _run_os_command(["docker", "container", "ls", "-a",
                              "--filter", f"name={name}",
                              "--format", "\"{{.Names}}\""])

    return name in output

def _is_image_available(name):
    output = _run_os_command(["docker", "image", "ls"])
    return name in output


def _is_image_available(name):
    output = _run_os_command(["docker", "images", "--format",
                              "\"{{lower .Repository}}\"", name])
    return name.split(":")[0] in output


def _get_config_value(conf, docker=True):
    if docker:
        return _docker_exec(["cms", "config", "value", conf])
    else:
        return _run_os_command(["cms", "config", "value", conf])


# you can use writefile(filename, entry) to for example write a file. make
# sure to use path_expand and than create a dir. you can resuse commands form
# cloudmesh.common, but no other class

class CmsdCommand:

    def update(self):
        """
        Updates container docker repos
        :return:
        """
        print(f"\nUpdating cloudmesh repos in {CMS_CONTAINER_NAME}")
        _docker_exec("/bin/bash /init.sh")

    @staticmethod
    def run(command=""):
        """
        run the command via the docker container

        :param command: the cms command to be run in the container
        """
        _docker_exec(command)

    @staticmethod
    def cms(command=""):
        """
        run the command via the docker container

        :param command: the cms command to be run in the container
        """
        _docker_exec("cms " + command)

    @staticmethod
    def up():
        """
        starts up the containers for cms
        """
        success = False

        if _is_container_available(CMS_CONTAINER_NAME):
            os.system(f"docker start {CMS_CONTAINER_NAME}")
            success = True

        if _is_container_available(MONGO_CONTAINER_NAME):
            os.system(f"docker start {MONGO_CONTAINER_NAME}")
            success = True

        if not success:
            print("WARNING: No containers available for starting!")

    @staticmethod
    def ps():
        """
        docker-compose ps
        """
        os.system(f"docker ps")

    @staticmethod
    def stop():
        """
        docker-compose stop
        """
        success = False

        if _is_container_running(CMS_CONTAINER_NAME):
            os.system(f"docker stop {CMS_CONTAINER_NAME}")
            success = True

        if _is_container_running(MONGO_CONTAINER_NAME):
            os.system(f"docker stop {MONGO_CONTAINER_NAME}")
            success = True

        if not success:
            print("WARNING: No containers available for stopping!")

    @staticmethod
    def shell():
        """
        docker-compose stop
        """
        os.system(f"docker exec -it {CMS_CONTAINER_NAME} /bin/bash")

    def setup(self):
        """
        this will copy the docker compose yaml and json file into the config_path
        only if the files do not yet exist
        :return:
        """
        cloudmesh_config_dir = DEFAULT_CLOUDMESH_CONFIG_DIR

        print(f"\nUsing CLOUDMESH_CONFIG_DIR={cloudmesh_config_dir}")
        print(f"\nRunning cms help on host OS...")
        _run_os_command(["cms", "help"])

        if not os.path.exists(cloudmesh_config_dir):
            os.mkdir(cloudmesh_config_dir)

        if _is_image_available(CMS_IMAGE_NAME):
            print(f"\n{CMS_IMAGE_NAME} image available!")
        else:
            print(f"\n{CMS_IMAGE_NAME} image not found! Building...")

            temp_dir = cloudmesh_config_dir + '/temp'
            os.mkdir(temp_dir)

            with open(temp_dir + '/Dockerfile', 'w') as f:
                f.write(DOCKERFILE)

            with open(temp_dir + '/init.sh', 'w') as f:
                f.write(INIT_SH)

            os.system(f"docker build -t {CMS_IMAGE_NAME} {temp_dir}")

            shutil.rmtree(temp_dir)

        if _is_container_running(CMS_CONTAINER_NAME):
            print(f"\n{CMS_CONTAINER_NAME} container running!")
        else:
            print(f"\n{CMS_CONTAINER_NAME} container not running! Starting...")
            res = os.system(f"docker run -d -it "
                            f"-v {cloudmesh_config_dir}:/root/.cloudmesh "
                            f"-v ~/.ssh:/root/.ssh --net host "
                            f"--name {CMS_CONTAINER_NAME} {CMS_IMAGE_NAME}")
            if res != 0:
                print(f"\nERROR: Unable to start container "
                      f"{CMS_CONTAINER_NAME}! Exiting setup...")
                return

        if "TBD" in _get_config_value('profile.user'):
            print(f"\nWARNING: cloudmesh profile not set!")
            self.gui("profile")

        if _is_container_running(MONGO_CONTAINER_NAME):
            print(f"\n{MONGO_CONTAINER_NAME} container running!")
        else:
            print(
                f"\n{MONGO_CONTAINER_NAME} container not running! Starting...")

            mongo_pw = _get_config_value("data.mongo.MONGO_PASSWORD")

            if "TBD" in mongo_pw:
                print(f"\nWARNING: Mongo credentials not set!")
                self.gui("mongo user")
                mongo_pw = _get_config_value("data.mongo.MONGO_PASSWORD")

            print(f"\nCreating a docker volume for mongodb...")
            os.system(f"docker volume create {MONGO_VOLUME_NAME}")

            _docker_exec("cms config set data.mongo.MODE=running")

            res = os.system(f"docker run -d --name {MONGO_CONTAINER_NAME} "
                            f"-v {MONGO_VOLUME_NAME}:/data/db "
                            f"-p 127.0.0.1:27017:27017/tcp "
                            f"-e MONGO_INITDB_ROOT_USERNAME=admin "
                            f"-e MONGO_INITDB_ROOT_PASSWORD={mongo_pw} "
                            f" {MONGO_IMAGE} ")
            if res != 0:
                print(f"\nERROR: Unable to start container "
                      f"{MONGO_CONTAINER_NAME}! Exiting setup...")
                return

    def setup_mongo(self):
        cloudmesh_config_dir = DEFAULT_CLOUDMESH_CONFIG_DIR

        print(f"\nUsing CLOUDMESH_CONFIG_DIR={cloudmesh_config_dir}")
        print(f"\nRunning cms help on host OS...")
        _run_os_command(["cms", "help"])

        if _is_container_running(MONGO_CONTAINER_NAME):
            print(f"\n{MONGO_CONTAINER_NAME} container running!")
        else:
            print(
                f"\n{MONGO_CONTAINER_NAME} container not running! Starting...")

            mongo_pw = _get_config_value("data.mongo.MONGO_PASSWORD",
                                         docker=False)

            if "TBD" in mongo_pw:
                print(f"\nWARNING: Mongo credentials not set!")
                self.gui("mongo user")
                mongo_pw = _get_config_value("data.mongo.MONGO_PASSWORD",
                                             docker=False)

            print(f"\nCreating a docker volume for mongodb...")
            os.system(f"docker volume create {MONGO_VOLUME_NAME}")

            _run_os_command("cms config set data.mongo.MODE=running".split(" "))

            res = os.system(f"docker run -d --name {MONGO_CONTAINER_NAME} "
                            f"-v {MONGO_VOLUME_NAME}:/data/db "
                            f"-p 127.0.0.1:27017:27017/tcp "
                            f"-e MONGO_INITDB_ROOT_USERNAME=admin "
                            f"-e MONGO_INITDB_ROOT_PASSWORD={mongo_pw} "
                            f" mongo:4.2 ")
            if res != 0:
                print(f"\nERROR: Unable to start container "
                      f"{MONGO_CONTAINER_NAME}! Exiting setup...")
                return

    def clean(self, force=None):
        """
        remove the ~/.cloudmesh/cmsd dir
        :return:
        """
        print("\nStopping containers ...")
        self.stop()

        print("\nRemoving containers ...")
        if _is_container_available(CMS_CONTAINER_NAME):
            os.system(f"docker container rm {CMS_CONTAINER_NAME}")

        if _is_container_available(MONGO_CONTAINER_NAME):
            os.system(f"docker container rm {MONGO_CONTAINER_NAME}")

            print("\nRemoving volumes ...")
            os.system(f"docker volume rm {MONGO_VOLUME_NAME}")
            
        if force:
            print("\nRemoving images ...")
            if _is_image_available(CMS_IMAGE_NAME):
                os.system(f"docker image rm {CMS_IMAGE_NAME}")
                
            if _is_image_available(MONGO_IMAGE):
                os.system(f"docker image rm {MONGO_IMAGE}")

        if _is_image_available(CMS_IMAGE_NAME):
            print("\nRemoving images ...")
            os.system(f"docker image rm {CMS_IMAGE_NAME}")

    @staticmethod
    def version():
        os.system("docker images | fgrep cmsd_cloudmesh")

    def gui(self, command):
        from cloudmesh.gui.command.gui import GuiCommand

        gui = GuiCommand()

        gui.do_gui(command)

        print("Executed gui cmd: ", command)

    def do_cmsd(self):
        """
        ::

          Usage:
            cmsd --help
            cmsd --setup [--mongo]
            cmsd --clean [--force]
            cmsd --version
            cmsd --update
            cmsd --start
            cmsd --stop
            cmsd --ps
            cmsd --gui COMMAND...
            cmsd --shell
            cmsd --pipe
            cmsd COMMAND...


          This command passes the arguments to a docker container
          that runs cloudmesh.

          Arguments:
              COMMAND the commands we bass along

          Description:

            cmsd --help

                prints this manual page

            cmsd --setup [--mongo]

                sets up cmsd containers.

                If --mongo flag is passed, only the mongo container will be
                setup.

            cmsd --clean [--force]

                stops and removes cmsd containers

                If --clean flag is passed, container images will also be
                removed.

            cmsd --version

                prints out the version of cmsd and the version of the container

            cmsd --update

                updates the cloudmesh repositories inside the cms-container

            cmsd --start

                starts cmsd containers

            cmsd --stop

                stops cmsd containers

            cmsd --ps

                lists the container processes

            cmsd --gui help

                find out which gui commands are available

            cmsd --gui quick

                runs cloudmesh gui on the docker container

            cmsd --shell

                enters the cms container and starts an interactive shell

            cmsd --pipe

                You can pipe commands or scripts to the cmsd container

                    echo "banner a" | cmsd --pipe

            cmsd COMMAND

                The command will be executed within the container, just as in
                case of cms.

            cmsd

                When no command is specified, cmsd will be run in interactive
                mode.

        """

        StopWatch.start("run")


        if len(sys.argv) == 1:
            # if arguments["COMMAND"] is None
            print("start cms interactively")
            os.system(
                f"docker exec -ti {CMS_CONTAINER_NAME} /usr/local/bin/cms")
            return ""

        elif not sys.argv[1].startswith("--"):

            # print("start cms interactively")
            # os.system("docker exec -ti cmsd /bin/bash")

            command = ' '.join(sys.argv[1:])
            self.cms(command)

            return ""

        doc = textwrap.dedent(self.do_cmsd.__doc__)
        arguments = docopt(doc, help=False)


        if arguments["--setup"]:

            if arguments['--mongo']:
                self.setup_mongo()
            else:
                self.setup()

        elif arguments["--version"]:
            print("cmsd:", version)
            self.version()

        elif arguments["--clean"]:
            self.clean(arguments['--force'])

        elif arguments['--help']:
            print(doc)

        elif arguments["--stop"]:
            self.stop()

        elif arguments["--start"]:
            self.up()

        elif arguments["--ps"]:
            self.ps()

        elif arguments["--update"]:
            self.update()

        elif arguments["--shell"]:
            self.shell()

        elif arguments["--gui"]:
            self.gui(" ".join(arguments["COMMAND"]))

        # not implemented
        elif arguments["--pipe"]:
            os.system(
                f"docker exec -i  {CMS_CONTAINER_NAME} /bin/bash -c /usr/local/bin/cms")
            return ""

        # "cat setup.json |  docker run -i  ubuntu /bin/bash -c 'cat'"
        else:
            print(doc)

        StopWatch.stop("run")
        print()
        StopWatch.print("Run time", "run")
        print()



        return ""


def main():
    command = CmsdCommand()
    command.do_cmsd()


if __name__ == "__main__":
    main()
