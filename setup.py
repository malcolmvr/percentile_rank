from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'percentile_rank',         # How you named your package folder (MyLib)
  packages = ['percentile_rank'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Returns the percentile of a value. Returns the same values as the Excel PERCENTRANK and PERCENTRANK.INC functions.',   # Give a short description about your library
  long_description = long_description,
  long_description_content_type="text/markdown",
  author = 'Malcolm van Raalte',                   # Type in your name
  author_email = 'malcolm@van.raalte.ca',      # Type in your E-Mail
  url = 'https://github.com/malcolmvr/percentile_rank',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/malcolmvr/percentile_rank/archive/v1.0.0.tar.gz',    # I explain this later on
  keywords = ['percentile', 'rank', 'percentrank', 'percentrank.inc', 'excel'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)