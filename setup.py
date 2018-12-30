import pathlib
from setuptools import setup, find_packages


CWD = pathlib.Path(__file__).parent
README = (CWD / "README.md").read_text()


setup(
    name="micropython-cozir",
    version="0.0.1",
    author="Dmitry Larkin",
    author_email="dmitry.larkin@gmail.com",
    description="COZIR CO2 Sensor Library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dml/micropython-cozir",
    packages=find_packages(exclude=("tests",)),
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
    ],
)
