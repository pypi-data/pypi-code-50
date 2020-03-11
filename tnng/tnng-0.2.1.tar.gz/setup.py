import setuptools
from pathlib import Path

p = Path(__file__)


setup_requires = [
    'numpy',
    'pytest-runner'
]

install_requires = [
]
test_require = [
    'pytest-cov',
    'pytest-html',
    'pytest',
]

setuptools.setup(
    name="tnng",
    version='0.2.1',
    python_requires='>3.5',
    author="Koji Ono",
    author_email="koji.ono@exwzd.com",
    description="Toy Neural Network Generator.",
    url='https://github.com/0h-n0/toy_neural_network_generator',
    long_description=(p.parent / 'README.md').open(encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=test_require,
    extras_require={
        'docs': [
            'sphinx >= 1.4',
            'sphinx_rtd_theme']},
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: MIT License",
    ],
)
