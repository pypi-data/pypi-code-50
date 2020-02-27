from setuptools import setup

setup(name='warpy',
      version='0.6',
      description='A simple cli to get WARP+ as WireGuard configuration',
      url='https://github.com/warp-plus/warpy-python',
      download_url='https://github.com/warp-plus/warpy-python/archive/v_05.tar.gz',
      keywords = ['warpy', 'warp+', 'warp-plus', 'warp wireguard'],
      license='gpl',
      author='Arian Amiramjadi',
      author_email='me@arian.lol',
      packages=['warpy'],
      install_requires=['pynacl', "requests"],
      entry_points={'console_scripts': [
            'warpy = warpy.__main__',
        ]},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
        ],
      )
