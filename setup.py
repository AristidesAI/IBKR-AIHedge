#!/usr/bin/env python
"""
IBKR AI Hedge Fund Integration Setup Script
"""

import sys
from pathlib import Path
from setuptools import setup, find_packages

# Ensure we're using Python 3.8+
if sys.version_info < (3, 8):
    raise RuntimeError("Python 3.8 or higher is required")

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read requirements from requirements.txt
requirements = []
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Development requirements
dev_requirements = []
try:
    with open("requirements-dev.txt", "r", encoding="utf-8") as f:
        dev_requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]
except FileNotFoundError:
    pass

setup(
    name="ibkr-ai-hedge-fund",
    version="1.0.0",
    author="Aristides Lintzeris",
    author_email="contact@aristidesai.com",
    description="An automated trading integration that connects Interactive Brokers with AI-powered financial analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aristideslintzeris/ibkr-ai-hedge-fund",
    project_urls={
        "Bug Reports": "https://github.com/aristideslintzeris/ibkr-ai-hedge-fund/issues",
        "Source": "https://github.com/aristideslintzeris/ibkr-ai-hedge-fund",
        "Documentation": "https://github.com/aristideslintzeris/ibkr-ai-hedge-fund/tree/main/docs",
        "Twitter": "https://x.com/aristidesai",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    keywords="trading, ai, machine-learning, finance, interactive-brokers, algorithmic-trading, quantitative-finance, hedge-fund, automation",
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements,
        "test": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-mock>=3.11.1",
            "pytest-asyncio>=0.23.2",
        ],
        "docs": [
            "sphinx>=7.2.0",
            "sphinx-rtd-theme>=1.3.0",
            "myst-parser>=2.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ibkr-ai-hedge-fund=ibkr_integration:main",
            "ibkr-config=config:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml", "*.json"],
        "docs": ["*.md", "*.rst"],
    },
    zip_safe=False,
    platforms=["any"],
    license="MIT",
) 