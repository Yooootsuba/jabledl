from setuptools import setup, find_packages

setup(name             = "jabledl",
      version          = "1.0.0",
      description      = "A video downloader for Jable",
      author           = "Yooootsuba",
      license          = "MIT",
      packages         = find_packages(),
      install_requires = [
          'tqdm',
          'argparse',
          'pycryptodome',
          'm3u8',
          'requests',
          'beautifulsoup4',
      ],
      entry_points = {
          'console_scripts': ['jabledl=jabledl.jabledl:main'],

      }
)
