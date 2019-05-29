#!/usr/bin/env python

PROJECT = 'zuulcli'

VERSION = '0.1'

from setuptools import setup, find_packages

setup(
    name=PROJECT,
    version=VERSION,

    description='CLI tool for Zuul API',

    author='Liu Sheng',
    author_email='liusheng2048@gmail.com',

    license='Apache 2.0',

    url='https://github.com/liu-sheng/zuulcli',

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Intended Audience :: Developers',
        'Environment :: Console',
    ],

    platforms=['Any'],

    scripts=[],

    provides=['zuulcli',
              ],
    install_requires=[
        'cliff>2.9.0',
    ],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'zuulctl = zuulcli.app:main',
        ],
        'zuulcli.commands': [
            'build_list = zuulcli.builds:BuildsList',
            'build_show = zuulcli.builds:BuildShow',
            'buildset_list = zuulcli.buildsets:BuildsetsList',
            'buildset_show = zuulcli.buildsets:BuildsetShow',
            'job_list = zuulcli.jobs:JobsList',
            'job_show = zuulcli.jobs:JobShow',
            'project_list = zuulcli.projects:ProjectsList',
            'project_show = zuulcli.projects:ProjectShow',
        ],
    },

    zip_safe=False,
)
