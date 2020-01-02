import setuptools
from scripts.workflow import get_app_name, is_name_valid
from scripts.workflow import get_args,  is_args_valid
from scripts.workflow import create_dir, create_app, create_templates_folder, create_static_folder, create_dockerfile
from scripts.manual import print_manual
from scripts.Colors import bcolors

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='build-flask-app',  
    version='0.0.3',
    scripts=['build-flask-app'] ,
    author="Hans Maulloo",
    author_email="maulloohans@gmail.com",
    description="A flask app generator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kouul/create-flask-app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)