# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nlp_tools']

package_data = \
{'': ['*']}

install_requires = \
['nltk>=3.4.5,<4.0.0', 'numpy>=1.18.1,<2.0.0', 'pandas>=1.0.1,<2.0.0']

setup_kwargs = {
    'name': 'nlp-tools-py-lib',
    'version': '0.1.0',
    'description': 'simple nlp library',
    'long_description': "# nlp-tools-py-lib\npython simple nlp library\n\n## installation\n\n````shell script\npip install nlp-tools-py-lib\n````\n\n## usage\n\n````python\n# main.py\nfrom nlp_tools.preprocessing import Preprocessing\nfrom nlp_tools.loaders import MdLoader\nfrom nlp_tools.representations import MergedMatrixRepresentation\nfrom nlp_tools.classifiers import ClassificationProcessor, NaiveBayseTfIdfClassifier\n\nTRAIN_PATH = './training.md'\n\ndef build_classifier():\n    loader = MdLoader(TRAIN_PATH)\n    processor = Preprocessing(loader)\n    repres = MergedMatrixRepresentation(processor.data)\n    classifier = ClassificationProcessor(NaiveBayseTfIdfClassifier(), repres)\n    classifier.train()\n\n    def predict(text: str):\n        message = repres.process_new_data(processor.process_sentence(text))\n        intent, score = classifier.predict(message)\n        return intent, score\n    return predict\n````\n\n``training.md`` example :\n\n````markdown\n# intents\n\n## my_first_intent_name\n\n### responses\n\n- ...\n\n### example\n\n- ...\n````",
    'author': 'thomas.marquis.dev',
    'author_email': 'thomas.marquis.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/thomas-marquis/nlp-tools-py-lib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
