from setuptools import setup, Extension
with open("readme.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()
setup(
  name = 'vk_audio',         # How you named your package folder (MyLib)
  packages = ['vk_audio'],   # Chose the same as "name"
  version = '6.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'audio vk Library',   # Give a short description about your library
  author = 'Ivan',                   # Type in your name
  long_description=long_description,
  long_description_content_type='text/markdown',
  author_email = 'imartemy1524@gmail.com',      # Type in your E-Mail
  url = 'https://vk.com/imartemy',   # Provide either the link to your github or to your website
  keywords = ['vk', 'audio', 'vkaudio','music','vkmusic'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'vk-api','datetime'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
  python_requires='>=3.4'
)