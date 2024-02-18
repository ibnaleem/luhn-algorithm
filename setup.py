from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Luhn Algorithm",
    version="1.0.3",
    author="Ibn Aleem",
    author_email="ibnaleem@outlook.com",
    description="Python implementation of Luhn's algorithm for validating credit card numbers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ibnaleem/luhn-algorithm",
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)
