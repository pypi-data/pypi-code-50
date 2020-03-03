from setuptools import setup, find_packages

setup(
    name='Hotel_Lite_VF',
    version='0.1',
    author='Lazaro Varela',
    author_email='lazarodecouso@gmail.com',
    description='Gestor sencillo de un hotel',
    long_description=open('README.rst').read(),
    long_description_content_type="text/markdown",
    license=open('LICENSE.txt').read(),
    url='https://github.com/lasaroh/Hotel_Lite',
    packages=find_packages(),
    test_suite='Test',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.6',
)
