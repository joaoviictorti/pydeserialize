#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages
import os,sys

meta = {}
here = os.path.abspath(os.path.dirname(__file__))

with open(f"{here}/pydeserialize/__meta__.py") as arquivo:
    exec(arquivo.read(), meta)

with open(f"{here}/requirements.txt", "r", encoding="utf-8") as f:
    requires = f.read().splitlines()
    if not requires:
        print("Não foi possível ler os requisitos do arquivo requirements.txt"
              "Isso indica que esta cópia do código-fonte está incompleta.")
        sys.exit(2)

with open("README.md", "r",encoding="utf-8") as arq:
    readme = arq.read()

setup(name=meta["__title__"],
    version=meta["__version__"],
    license='MIT License',
    author=meta["__author__"],
    url=meta["__url__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email=meta["__author_email__"],
    keywords='serialize insegura desserialize   ',
    description=meta["__description__"],
    packages=find_packages(),
    zip_safe=False,
    install_requires=requires,
    python_requires=">=3.6, <4",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "Topic :: System :: Operating System",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities"
    ],
    entry_points={'console_scripts': [
        'pydeserialize=pydeserialize.pydeserialize:argumentos',
        ]
    })