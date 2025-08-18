
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pingera-sdk",
    version="1.0.3",
    author="Pingera Team",
    author_email="privet@pingera.ru",
    description="A comprehensive Python SDK for the Pingera monitoring platform API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pingera/pingera-sdk",
    packages=find_packages(where="client"),
    package_dir={"": "client"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Monitoring",
    ],
    python_requires=">=3.9",
    install_requires=[
        "urllib3>=2.1.0,<3.0.0",
        "python-dateutil>=2.8.2",
        "pydantic>=2",
        "typing-extensions>=4.7.1",
    ],
    extras_require={
        "dev": [
            "pytest>=7.2.1",
            "pytest-cov>=2.8.1",
            "tox>=3.9.0",
            "flake8>=4.0.0",
            "types-python-dateutil>=2.8.19.14",
            "mypy>=1.5",
        ],
    },
    keywords=[
        "pingera",
        "monitoring",
        "api",
        "status-page",
        "uptime",
        "incidents",
        "components",
        "openapi",
    ],
    project_urls={
        "Documentation": "https://docs.pingera.ru",
        "Bug Reports": "https://github.com/pingera/pingera-sdk/issues",
        "Source": "https://github.com/pingera/pingera-sdk",
        "Homepage": "https://pingera.ru",
    },
)
