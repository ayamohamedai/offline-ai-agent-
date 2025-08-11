#!/usr/bin/env python3
"""
Setup script for Offline AI Agent
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    # Remove comments and empty lines
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

setup(
    name="offline-ai-agent",
    version="1.0.0",
    author="Aya Mohamed",
    author_email="your.email@example.com",  # Replace with your email
    description="An intelligent offline AI agent for local document processing and question answering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ayamohamedai/offline-ai-agent",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
            "pre-commit>=3.3.0",
        ],
        "gpu": [
            "faiss-gpu>=1.7.4",
        ],
    },
    entry_points={
        "console_scripts": [
            "offline-ai-agent=offline_ai_agent.main:main",
            "ai-agent=offline_ai_agent.cli:cli",
        ],
    },
    include_package_data=True,
    package_data={
        "offline_ai_agent": [
            "config/*.yaml",
            "data/*.json",
            "templates/*.txt",
        ],
    },
    keywords=[
        "artificial intelligence",
        "AI agent",
        "offline processing",
        "document analysis",
        "natural language processing",
        "machine learning",
        "RAG",
        "vector search",
        "local AI",
    ],
    project_urls={
        "Bug Reports": "https://github.com/ayamohamedai/offline-ai-agent/issues",
        "Source": "https://github.com/ayamohamedai/offline-ai-agent",
        "Documentation": "https://github.com/ayamohamedai/offline-ai-agent/wiki",
    },
)
