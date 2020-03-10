from setuptools import setup
import setuptools.command.build_py

class BuildTestCommand(setuptools.command.build_py.build_py):
    """Custom build command."""

    def run(self):

        # run tests using doctest
        import doctest
        
        # filters folder
        from rawls import converter
        from rawls import merger

        print("==============================")
        print("Runs test command...")

        # pass test using doctest
        doctest.testmod(converter)
        doctest.testmod(merger)

        setuptools.command.build_py.build_py.run(self)


setup(
    name='rawls',
    version='0.0.4',
    description='RAW Light Simulation file reader/converter package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities'
    ],
    url='https://github.com/prise-3d/rawls',
    author='Jérôme BUISINE',
    author_email='jerome.buisine@univ-littoral.fr',
    license='MIT',
    packages=['rawls'],
    install_requires=[
        'numpy',
        'Pillow',
        'scipy',
    ],
    cmdclass={
        'build_py': BuildTestCommand,
    },
    zip_safe=False)
