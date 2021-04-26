import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="crypto-coins",
    version="1.0.0",
    description="read README.md from github",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gravitywolfLaCanneAPeche/crypto-coins",
    author="Canne à pêche",
    author_email="gravitywolf.loup@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9.4",
    ],
    packages=["crypto_coins"],
    include_package_data=True,
    
)
