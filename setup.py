#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

import pip
import semver

if 10 >= semver.parse(pip.__version__)['major']:
    import pip._internal.download as pip_download
    from pip._internal.req import parse_requirements
else:
    import pip.download as pip_download
    from pip.req import parse_requirements

exec(open('steenzout/object/metadata.py').read())

setup(name='steenzout.object',
      version=__version__,
      description=__description__,
      author=__author__,
      author_email=__author_email__,
      maintainer=__maintainer__,
      maintainer_email=__maintainer_email__,
      url=__url__,
      namespace_packages=['steenzout'],
      packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
      package_data={'': ['LICENSE', 'NOTICE.md']},
      install_requires=[
          str(pkg.req) for pkg in parse_requirements(
              'requirements.txt', session=pip_download.PipSession())],
      tests_require=[
          str(pkg.req) for pkg in parse_requirements(
              'requirements-test.txt', session=pip_download.PipSession())],
      license=__license__,
      classifiers=__classifiers__)
