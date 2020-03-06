# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyPhases',
 'pyPhases.decorator',
 'pyPhases.exporter',
 'pyPhases.publisher',
 'pyPhases.storage',
 'pyPhases.util']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.18.1,<2.0.0', 'pandas>=1.0.1,<2.0.0', 'pyarrow>=0.16.0,<0.17.0']

setup_kwargs = {
    'name': 'pyphases',
    'version': '0.1.1',
    'description': 'A Framework for creating progress based applications, like machine learning algroithms',
    'long_description': '# pyPhases\n\nA small framework for python projects that are mainly progress based.\n\nThe main princible of the framework are `Phases`.\n\n# Architecure\n\n![arch](assets/achitektur.svg)\n\n## Project\n\nA Project is the composition of phases and the backend.\n\n## Phase\nA Phase has a `main` Method and can export data.\n\n## Stage\n\nA stage is a group of Phases and only have a name. A Stage can be run seperatly with `project.run("stagename")`\n\n## Decorators\n\n# Compontents\n\n## Storage and Exporters\n\n### Storage\n\nYou can add diffrent storage-engines to your project, with `project.addStorage(Engine())`. A storage you be inherited from `pyPhases.storage.Storage` and implement the methods `read(path: str)` and `write(path: str, data: bytes)`.\nThe order is important and the Storages should be ordered from fast to slow.\n\nBy Default there is a memory storage, that will save the data in the project, but is not persitent. The default persistent data layer is the filesystem(`storage.FileStorage`).\n\n### Exporter\n\nAn Exporter can be registered to transform an Instance or primitive type into a `byte` string (`export(obj : MyObject): bytes`) and vice versa (`importData(bytes): MyObject`).\n\nThere is a default `ObjectExporter`, that is based on [pyarror](https://pypi.org/project/pyarrow/) and is compatible with diffrent fromats like pandas Dataframes and numpy arrays.\n\n### register Data\nWhen a phase wants to register data (`self.project.registerData("myDataId", myData)` within the phase), the data is passed to an exporter. If an exporter is found the data will be passed to alle the storages. They will save the data somewhere (persitent or not).\n\nexample:\n\n![seq](assets/seq-save-data.svg)\n\n### reading the data\nA phase can request data with `self.project.getData("myDataId", MyDataType)`. The Data will be passed sequential to the storage layer and will pass the data from the first storage that is able to get it. If no storage can provide the data, the project will search for a phase that exports this data-id and run that specific phase.\n\nexample:\n\n![get-data](assets/seq-get-data.svg)\n\n\n### example\n\nThis is a example data layer with 3 storages: memory, file, database (`not default`)\n![data-layer](assets/data-layer.svg)\n',
    'author': 'fehrlich',
    'author_email': 'fehrlichd@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/tud.ibmt/pyphases',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
