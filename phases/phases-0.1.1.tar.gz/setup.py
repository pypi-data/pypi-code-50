# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['phases', 'phases.commands', 'phases.util']

package_data = \
{'': ['*'],
 'phases': ['generate-template/*',
            'generate-template/docs/*',
            'generate-template/{{name}}/*',
            'static-template/*']}

install_requires = \
['PyYAML>=5.3,<6.0',
 'docopt>=0.6,<0.7',
 'pyPhases>=0.0,<0.1',
 'pystache>=0.5,<0.6']

entry_points = \
{'console_scripts': ['phases = phases.cli:main']}

setup_kwargs = {
    'name': 'phases',
    'version': '0.1.1',
    'description': 'A Framework for creating a boilerplate template for ai projects that are ready for MLOps',
    'long_description': '# pyPhase Project-builder\n\nThis Generator will create a ready-to-go pyPhase-Project, based on a config-Yaml. \n\n## Setup\n\n`pip install phases`\n\n## create `project.yaml`\n\n### minimal\n```YAML\nname: "myProject"\nnamespace: myGroup\nphases:\n    stage1:\n        - name: Phase1\n          description: my first phase\n          exports:\n            - myData\n    stage2:\n        - name: Phase2\n          description: my second phase\n```\n\nrun with `python myProject`\n\n### complete\n```YAML\nname: "sleepClassificationCNN"\nnamespace: tud.ibmt\nexporter:\n    - ObjectExporter\n    - KerasExporter\npublisher:\n    - DotSience\nphases:\n    prepareData:\n        - name: DataWrapper\n          description: get EDF Data\n          exports: \n            - trainingRaw\n            - validationRaw\n            - evaluationRaw\n        - name: EDF4SleepStages\n          description: Prepare EDF Data for sleep stage recognition\n          exports: \n            - trainingTransformed\n            - validationTransformed\n    train:\n        - name: SleepPhaseDetectionModel\n          description: Create Model for sleep stage recognition\n          exports: \n            - model\n    evaluate:\n        - name: SleepPhaseDetectionModel\n          description: Create Model for sleep stage recognition\n```\n\n### Generate\n\n`phases create`\n\n\n### Development\n\nThe generator will create stubs for each phase, publisher, storage, exporter and generator that \ndoes not exists in the pyPhase-Package. The stubs are in the project folder and implement empty\nmethod that are required.\n\nTo implement your project, you only need to fill those methods. For the minimal example you need\nto fill the `main`-methods of Phase1 (`myProject/phases/Phase1.py`) and Phase2.\n\n### Execute\n\nIf you want to run the whole Project run: `python [ProjectName]` for the minimal example: `python myProject`\n\nTo run a single stage: `python [ProjectName] [StageName]` for the minimal example: `python myProject stage2`\n\n## additional files\n\n- `doc/` placeholder for automated documentation\n- `.editorconfig` some settings for supporting IDE about File encoding and formats (see https://editorconfig.org/)\n- `.gitignore` some folders and files that should be ignored by git (see https://git-scm.com/docs/gitignore)\n\n- `requirements.txt` the python requirements (just pyPhases in an empty project)\n- `setup.py` a python setup-file with some data (https://docs.python.org/3/installing/index.html#installing-index)\n- `README.md` an Readme file that is used for git and python packages\n- `Dockerfile` a simple dockerfile that can be used to run the project in a container (The `FROM` image should properly changed)\n- `docker-compose.yml` this is a helper to create and run the container. simply run `docker-compose up` or `docker compose run --rm [projectname] [stagename]`\n- `.gitlab-ci.yml` a Configuration for the Gitlab-CI Pipeline, that will be automaticly run if there is a push to gitlab\n',
    'author': 'fehrlich',
    'author_email': 'fehrlichd@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/tud.ibmt/phases',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
