from setuptools import setup, find_packages

print find_packages()

setup(
    name='MinutiaeClassificator',
    version='0.0.9',
    license='MIT',
    description='Minutiae extraction and classification tool',
    author='Jakub Arendac',
    author_email='jakub.arendac105@gmail.com',
    url='https://github.com/jakubarendac/MinutiaeClassificator/tree/dev/publish',
    download_url='https://github.com/jakubarendac/MinutiaeClassificator/archive/0.0.5.tar.gz',
    keywords=['minutiae', 'extraction', 'classification', 'biometrics'],
    # TODO : add needed packages
    install_requires=[],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    packages=['MinutiaeClassificator.ClassifyNet', 'MinutiaeClassificator.constants','MinutiaeClassificator.utils']
)