from setuptools import setup

setup(install_requires = [
          'tqdm',
          'argparse',
          'pycryptodome',
          'm3u8',
          'requests',
          'beautifulsoup4',
      ],
      scripts = ['scripts/jabledl']
     )
