import setuptools
from distutils.core import setup

setup(name='scicolor',
      version='0.1',
      description = 'Collections of color maps for scientific visualizations',
      author = 'Kaicheng Yang',
      author_email = 'yangkc@iu.edu',
      url="https://github.com/yangkcatiu/scicolor",
      license = 'MIT',
      install_requires=[
          'matplotlib',
          'numpy',
          'pandas'
      ],
      packages = ['scicolor']
)
