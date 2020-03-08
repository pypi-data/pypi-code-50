import setuptools

setuptools.setup(name='cqrcode',
                 version='0.2',
                 description='Generate a QR code that can adapt to the cylinder',
                 long_description=open('README.md', 'r', encoding='utf-8').read(),
                 author='jiaming',
                 author_email='837357785@qq.com',
                 url = 'https://pypi.org/project/cqrcode/',
                 license='MIT',
                 install_requires = [
                    'Pillow>=6.1.0',
                 ],
                 keywords='cylinder qrcode',
                 classifiers=[
                     "Natural Language :: Chinese (Simplified)",
                     "Development Status :: 3 - Alpha",
                     "Operating System :: OS Independent",
                     "Programming Language :: Python",
                     "Programming Language :: Python :: 3.4",
                     "Programming Language :: Python :: 3.5",
                     "Programming Language :: Python :: 3.6",
                     "Programming Language :: Python :: 3.7",
                     "License :: OSI Approved :: MIT License",
                     "Topic :: Utilities"
                 ],
)