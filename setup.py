import setuptools
from scripts.workflow import get_app_name, is_name_valid
from scripts.workflow import get_args,  is_args_valid
from scripts.workflow import create_dir, create_app, create_templates_folder, create_static_folder, create_dockerfile
from scripts.manual import print_manual
from scripts.messages import failure_msg, success_msg, empty_name

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='build-flask-app',  
    version='0.0.8',
    scripts=['build-flask-app'],
    author="Hans Maulloo",
    author_email="maulloohans@gmail.com",
    description="A flask app generator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kouul/create-flask-app",
    install_requires=['colorama'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Code Generators"
    ],
)