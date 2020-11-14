"""
DiscordDBPlus
---------

A simple database which uses a Discord channel to store data.

"""


import re
import os

from setuptools import setup, find_packages


def __get_version():
    with open("discordDBPlus/__init__.py") as package_init_file:
        return re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', package_init_file.read(), re.MULTILINE).group(1)


requirements = [
    "discord.py",
]


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='DiscordDBPlus',
    author='AtaeKurri',
    url='https://github.com/AtaeKurri/DiscordDBPlus',
    version=__get_version(),
    packages=find_packages(),
    license='MIT',
    description='A simple database which uses a Discord channel to store data.',
    long_description=long_description,
    include_package_data=True,
    install_requires=requirements,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Utilities',
    ]
)
