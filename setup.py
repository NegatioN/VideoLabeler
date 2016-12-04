#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='VideoLabeler',
      version='0.1',
      description='Make labeled datasets from video.',
      author='Joakim Rishaug',
      author_email='joakimrishaug@gmail.com',
      url='https://github.com/NegatioN/VideoLabeler',
      packages=find_packages(exclude=("tests",)),

      # Entrypoints
      entry_points={
          "console_scripts": [
              "videolabeler = video_labeler:main"
          ]
      }
      )
