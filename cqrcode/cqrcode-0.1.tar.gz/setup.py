import setuptools

with open('README.md', 'r', encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(name='cqrcode',
                 version='0.1',
                 description='Generate a QR code that can adapt to the cylinder',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 author='jiaming',
                 author_email='837357785@qq.com',
                 url = '',
                 install_requires = [
                    'Pillow>=6.1.0',
                 ],
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
                 keywords='cylinder qrcode',
                 packages=setuptools.find_packages('src/cylinder_qrcode'),
                 package_dir = {'':'src/cylinder_qrcode'},
                 zip_safe=False,
                 include_package_data=True,
)