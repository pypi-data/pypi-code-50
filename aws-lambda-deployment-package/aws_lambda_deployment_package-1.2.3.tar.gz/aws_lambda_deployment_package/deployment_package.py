import logging
import os
import subprocess
import uuid

from typing import Optional, List

logr = logging.getLogger(__name__)


class DeploymentPackage:
    def __init__(self, project_src_path: str, environment: Optional[str] = None):
        self.__project_src_path = project_src_path
        self.__environment = environment or 'none'
        self.__dir = os.path.dirname(os.path.abspath(__file__))

        # Generate a semi-random path for a deployment package for this session.
        self.__root = f'/tmp/aws-lambda-deployment-package/{str(uuid.uuid4())}'
        logr.info(f'Working root path: {self.__root}.')

        self.__venv_path = f'{self.__root}/venv'
        logr.info(f'Venv path: {self.__venv_path}.')

        self.__install_path = f'{self.__root}/install'
        logr.info(f'Install directory: {self.__install_path}.')

        self.__package_path = f'{self.__root}/package/package.zip'
        logr.info(f'Path to deployment package zip file: {self.__package_path}.')

        self.__pre_install = [
            os.path.join(self.__dir, 'lambda_pre_install.sh'),
            self.__venv_path
        ]

        self.__install = [
            os.path.join(self.__dir, 'lambda_install.sh'),
            self.__environment,
            self.__project_src_path,
            self.__venv_path
        ]

        self.__post_install = [
            os.path.join(self.__dir, 'lambda_post_install.sh'),
            self.__venv_path,
            '--omit_wheels',
            '--omit_pip',
            '--omit_setup',
            '--omit_cfnlint',
            '--omit_pycountry_locales',
            '--omit_moto'
        ]

        self.__pre_build = [
            os.path.join(self.__dir, 'lambda_pre_build.sh'),
            self.__venv_path,
            self.__install_path,
            self.__project_src_path
        ]

        self.__build = [
            os.path.join(self.__dir, 'lambda_build.sh'),
            self.__install_path,
            self.__package_path
        ]

        self.__post_build = [
            os.path.join(self.__dir, 'lambda_post_build.sh'),
            self.__venv_path,
            self.__install_path,
        ]

    @property
    def path_to_deployment_package(self) -> str:
        return self.__package_path

    @property
    def path_to_install_dir(self) -> str:
        return self.__install_path

    def pre_install(self) -> None:
        logr.info('Pre-installing...')
        self.__call(self.__pre_install)

    def install(self) -> None:
        logr.info('Installing...')
        self.__call(self.__install)

    def post_install(self) -> None:
        logr.info('Post-installing...')
        self.__call(self.__post_install)

    def pre_build(self) -> None:
        logr.info('Pre-building...')
        self.__call(self.__pre_build)

    def build(self) -> None:
        logr.info('Building...')
        self.__call(self.__build)

    def post_build(self) -> None:
        logr.info('Post-building...')
        self.__call(self.__post_build)

    def create(self) -> None:
        self.pre_install()
        self.install()
        self.post_install()
        self.pre_build()
        self.build()
        self.post_build()

    @staticmethod
    def __call(command: List[str]) -> str:
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT)
            output = output.decode()
            logr.info(output)
            return output
        except subprocess.CalledProcessError as ex:
            logr.error(ex.output.decode())
            raise
