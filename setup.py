import io
import os
from setuptools import setup, find_packages


NAME = 'etlam'
DESCRIPTION = 'etlam - a basic structure for ETL projects'
URL = ''
EMAIL = 'malte.groth@gmx.net'
AUTHOR = 'Malte Groth'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1'


here = os.path.abspath(os.path.dirname(__file__))

try:
      with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
            long_description = '\n' + f.read()
except FileNotFoundError:
      long_description = DESCRIPTION


setup(
      name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=long_description,
      long_description_content_type='text/markdown',
      url=URL,
      author=AUTHOR,
      author_email=EMAIL,
      packages=find_packages(),
      install_requires=[
            'psycopg2',
            'sqlalchemy',
            'click',
            'pip-tools',
            'pytest',
            'celery'
      ],
      entry_points={
          'console_scripts': [
            'etlam = etlam.cli:main'
          ]
      }
)