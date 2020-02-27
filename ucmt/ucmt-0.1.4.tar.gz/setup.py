# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ucmt']

package_data = \
{'': ['*']}

install_requires = \
['docopt>=0.6.2,<0.7.0', 'tinydb>=3.15.2,<4.0.0']

entry_points = \
{'console_scripts': ['ucmt = ucmt.main:main']}

setup_kwargs = {
    'name': 'ucmt',
    'version': '0.1.4',
    'description': 'ucmt(User Config Management Tool) is the multiplatform(Windows, Mac, Linux) tool managing config in user space.',
    'long_description': '# ツールの概要\n\n管理したいユーザ空間の設定ファイルを一箇所に集めます．\n集めたところから元の path にシンボリックリンクを貼ることで，\n書くアプリケーションが問題なく設定ファイルを読み込めるようにします．\n\n# install\n\npip install ucmt\n\n## Note\n\nユーザ空間に install した場合， `~/.local/bin` に path を通してください．\n\n# Usage\nucmt add (<target>...)\n\n    指定したファイル・ディレクトリを管理対象に加える．\n\nucmt relocate\n\n    元の path にシンボリックリンクを貼り直す\n    新しい環境に設定を反映するときに有用である\n\nucmt del (<target>...)\n\n    指定したファイル・ディレクトリを管理対象から外す\n\n# TODO List\n+ 管理状況の可視化する\n+ github を利用して sync できるようにする\n+ OS に合わせた 元の path シンボリックリンクに貼るスクリプトを生成しておくようにする\n\n    Python のランタイムが入れられない環境で，シンボリックリンクの貼り直しだけは行えるようにするため',
    'author': 'Yuya.Nagai',
    'author_email': 'ynny.opem@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yn-git/User-Config-Management-Tool',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
