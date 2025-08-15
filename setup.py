from setuptools import find_packages, setup

setup(
    name="a7df32de3a60dfdb7a0b",
    version="0.11.8",
    packages=find_packages(),
    install_requires=[
        "snscrape",
        "exorde_data",
        "aiohttp",
        "python-dotenv",
        "pathlib",
        "lxml>=4.9",
        "selenium==4.21.0",
        "requests",
    ],
    extras_require={"dev": ["pytest", "pytest-cov", "pytest-asyncio"]},
)
