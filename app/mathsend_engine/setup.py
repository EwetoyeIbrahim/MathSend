import pathlib
from setuptools import setup
HERE=pathlib.Path(__file__).parent

README=(HERE/"README.md").read_text

setup(
    name="HumanMath",
    version="1.0.0",
    description="for converting from human readable mathematical expression into python form and can subsequently solve it",
    long_description=README,
    long_description_content_type="text/markdown",
    author="EWETOYE, Ibrahim",
    author_email="i.ewetoye@gmail.com",
    maintainer="EWETOYE, Ibrahim",
    maintainer_email="i.ewetoye@gmail.com",
    url="https://github.com/EwetoyeIbrahim/HumanMath",
    download_url="https://github.com/EwetoyeIbrahim/HumanMath",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["HumanMath"],
    include_package_data=True,
    install_requires=["Sympy"],
    entry_points={
        "console_scripts": [
            "human_math=HumanMath.__main__:main",
        ]
    },
)