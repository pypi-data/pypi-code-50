from __future__ import unicode_literals

from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


def version():
    with open('virtual_ipm/VERSION') as f:
        return f.read()


setup(
    name='virtual-ipm',
    version=version(),
    description='Virtual-IPM is a software for simulating IPMs and other related devices.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    keywords=['IPM', 'BIF', 'beam instrumentation', 'beam diagnostics',
              'transverse profile monitor', 'simulation', 'framework'],
    url='https://gitlab.com/IPMsim/Virtual-IPM',
    author='Dominik Vilsmeier',
    author_email='d.vilsmeier@gsi.de',
    license='AGPL-3.0',
    packages=[
        'virtual_ipm',
        'virtual_ipm.control',
        'virtual_ipm.data',
        'virtual_ipm.di',
        'virtual_ipm.frontends',
        'virtual_ipm.frontends.gui',
        'virtual_ipm.frontends.gui.simulation',
        'virtual_ipm.frontends.gui.analysis',
        'virtual_ipm.simulation',
        'virtual_ipm.simulation.beams',
        'virtual_ipm.simulation.beams.bunches',
        'virtual_ipm.simulation.devices',
        'virtual_ipm.simulation.particle_generation',
        'virtual_ipm.simulation.particle_generation.ionization',
        'virtual_ipm.simulation.particle_tracking',
        'virtual_ipm.simulation.particle_tracking.em_fields',
        'virtual_ipm.simulation.particle_tracking.em_fields.guiding_fields',
        'virtual_ipm.simulation.particle_tracking.em_fields.guiding_fields.models',
        'virtual_ipm.tools',
        'virtual_ipm.utils',
        'virtual_ipm.utils.mathematics',
    ],
    entry_points={
        'console_scripts': [
            'virtual-ipm = virtual_ipm.run:main',
            'virtual-ipm-settle = virtual_ipm.settle:main',
            'vipm-cst-to-csv = virtual_ipm.tools.convert_cst_file_to_csv:main',
            'vipm-csv-to-xml = virtual_ipm.tools.convert_csv_output_to_xml_data_file:main',
            'vipm-out-to-in = virtual_ipm.tools.convert_output_to_input:main',
        ],
        'gui_scripts': [
            'virtual-ipm-gui = virtual_ipm.start_gui:main',
        ],
    },
    install_requires=[
        'anna==0.3.5',
        'injector==0.12.1',
        'ionics==0.2.3',
        'matplotlib==2.1.1',
        'numpy==1.18',
        'pandas==0.23.4',
        'pyhocon==0.3.38',
        'rx==1.5.9',
        'scipy==1.1.0',
        'six==1.11.0',
    ],
    include_package_data=True,
    zip_safe=False
)
