#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="autoknow",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tree-sitter==0.20.2",
        "networkx==3.1",
        "click==8.1.7",
        "pytest==7.4.0",
    ],
    entry_points={
        "console_scripts": [
            "autoknow=autoknow.cli:main",
        ],
    },
    author="Femirins",
    description="Autonomous Code Knowledge Graph for AI Agents",
    license="MIT",
    keywords="ai, code, knowledge-graph, cli",
)