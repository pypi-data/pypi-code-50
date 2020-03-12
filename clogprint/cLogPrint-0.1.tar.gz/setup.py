from distutils.core import setup
setup(
  name = 'cLogPrint',         # How you named your package folder (MyLib)
  packages = ['cLogPrint'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Color for text in terminal and command prompt',   # Give a short description about your library
  author = 'Richard Hernandez',                   # Type in your name
  author_email = 'rhg101997@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/RHG101997/cLog',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/RHG101997/cLog/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Color', 'terminal color', 'color text'],   # Keywords that define your package best
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)


PATH="/Users/hakuna.matata/.local/bin:$/Users/richardhernandez/Library/Python/2.7/lib/python/site-packages"