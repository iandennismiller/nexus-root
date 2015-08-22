# -*- coding: utf-8 -*-
# Ian Dennis Miller
# nexus5-root

from setuptools import setup

version = '0.1'

setup(version=version,
    name='nexus5-root',
    description="Root your Nexus5.",
    packages=[
    ],
    scripts=[
        "bin/nexus5-root.py",
    ],
    long_description="""Root your Nexus5.""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',
    author='Ian Dennis Miller',
    author_email='iandennismiller@gmail.com',
    url='http://iandennismiller.com',
    dependency_links=[
    ],
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
)
