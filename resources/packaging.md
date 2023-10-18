# Python Packaging

Is very complicated, has many different tools and many different ways that want to accomplish the task of packaging and publishing your project. Although it has been announced for newer version of Python that `setup.py` is deprecated, it is still the most common way to package your project.

## Setup.py

The `setup.py` file is a Python script that is used to build and install your project. It is also used to package your project into a distribution. The `setup.py` file is usually located in the root of your project directory. This project has one and is very simple, reading the requirements from the `requirements.txt` file and using the `setuptools` module to package the project.

```python  
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
```

## Pyproject.toml

Alternatively, you can have a configuration file that works in the same way as `setup.py` but is meant for other tools to use it. Here is an example of a `pyproject.toml` file:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```
This project also has a `pyproject.toml` file that works in the same way as the `setup.py` file. You can use the `build` package and command to build your project. This will create a `dist` directory with the distribution files.

```bash
pip install build
$ python -m build
```


## Create a wheel

A wheel is a binary distribution format that is meant to be installed on a system. It is a compressed archive that contains all the files that are needed to install the project. You can create a wheel using the `bdist_wheel` sub-command with `setup.py` although because it is deprecated you might want to use the `build` command instead.

Here is how to do this with `setup.py`:

```
$ python setup.py bdist_wheel
```

To use `build` you will need to `pip install build`. Here is how to do this with `build`:

```
$ python -m build --wheel
```

## Using Pip

You can install a Python package with `pip` for development purposes using the _editable_ flag `-e`:

```bash
$ pip install -e .
```

This will have the same effect as `python setup.py develop` and will install the package in editable mode. This means that you can make changes to the source code and they will be reflected in the installed package.

## Publishing to PyPI

PyPI is the Python Package Index and is the official repository for Python packages. You can publish your package to PyPI using the `twine` package. You can install it with `pip install twine`. You will also need to create an account on PyPI and create an API token. You can do this by going to [https://pypi.org/](https://pypi.org/) and clicking on your username in the top right corner. Then click on _Account Settings_ and then _API Tokens_. Click on _Add API Token_ and enter a description and click on _Generate Token_. Copy the token and save it somewhere safe in your system.

You can now publish your package to PyPI using the `twine` package:

```bash
$ python -m twine upload --repository pypi dist/*
```
