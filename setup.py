# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-22 08:41:23
# @Last Modified time: 2018-08-03 20:48:15
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
# from setuptools import find_packages
from setuptools import setup

# Install dependencies from requirements.txt
# For pip >= 10
# https://stackoverflow.com/a/49867265/5951529
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session='hack')

# reqs is a list of requirements
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(
    install_requires=reqs,
    # packages=find_packages()
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('', ['README.md'])],
    # long_description=long_description
)
