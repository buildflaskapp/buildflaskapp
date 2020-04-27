import setuptools
from buildflaskapp.scripts.__version__ import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='buildflaskapp',
    version=__version__,
    author="Hans Maulloo",
    author_email="maulloohans@gmail.com",
    description="A flask app generator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/askyourkode/buildflaskapp",
    packages=setuptools.find_packages(),
    install_requires=['tabulate'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: Freely Distributable",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Code Generators"
    ],
    entry_points={"console_scripts": ["buildflaskapp=buildflaskapp.buildflaskapp:main"]}
)