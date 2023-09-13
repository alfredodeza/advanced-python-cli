# Practice Lab: Build a JSON formatter Command Line tool
In this practice lab, you will build a command line tool that will format JSON data. The tool will take JSON input as `stdin` and output formatted JSON to `stdout`. The tool will also support a `--file` option that will allow the user to specify a file to read JSON from.

**Learning objectives:**

- Use a command line framework like `Click` to handle arguments and options
- Practice error-handling techniques in Python
- Use logging to debug and troubleshoot your code
- Package and distribute your code as a Python package

**Steps:**

1. Create a new repository in your account for your Python project. Use the [Python template repository](https://github.com/alfredodeza/python-cli-example) to quickly generate one for your own account. Use this link to [create it in one step](https://github.com/alfredodeza/python-cli-example/generate).
1. Use the Click framework to handle arguments and options. Refer to the [advanced examples](./examples/2-complex) in this repository as a guide
1. Use the `json` module to parse JSON data from `stdin` or a file

**Bonus challenge:** Add options for your tool so that you can control the indentation level and sorting of keys in the JSON output. Use the `--help` option to display the available options. The indentation and sorting options are supported by the JSON module. Refer to the [documentation](https://docs.python.org/3/library/json.html#basic-usage) for more details.

Tips on reading input from  `stdin`:

Although `stdin` has not been covered in the examples of this course, here is a quick example of how to read from `stdin` using the `Click` framework:

```python
import click
import sys

@click.command()
@click.argument('input', type=click.File('r'), default=sys.stdin)
def cli(input):
    click.echo(input.read())
```

**Concepts Covered:**

- [x] Build a command line tool with arguments and options
- [x] Use a standard library module to parse JSON data
- [x] Use packaging tools to install dependencies and distribute your tool
- [x] Use logging to debug and troubleshoot your code

By completing this lab, you will have practical experience on building command line tools that can be applied to your own projects. This should also allow you to be more efficient and automate tasks in Data Engineering, DevOps, Systems Engineering, or Data Scientist roles.

# Bonus Practice Lab: Package and distribute your tool:

# Practice Lab: Package and Release a Python JSON Formatting Command Line Tool

In this practice lab, you will take your existing Python command line tool for formatting JSON data and focus on packaging and releasing it as a Python package. This process will make it easy for others to install and use your tool as a Python module.

**Learning Objectives:**

- Package your Python command line tool as a Python package.
- Make your tool available for others to install and use as a Python module.
- Understand the process of creating a distributable Python package.
- Explore the practical aspects of packaging and distributing Python software.

**Steps:**

1. Ensure your existing JSON formatting command line tool is working correctly and that it has been implemented following the previous lab instructions.

2. Reuse the same repository for your JSON formatting tool or create a new one with [the template in one step](https://github.com/alfredodeza/python-cli-example/generate).

3. Define your project's metadata in a `setup.py` file. This file will contain information about your project, such as its name, version, author, and description. Here's an example `setup.py`:

   ```python
   from setuptools import setup, find_packages

   setup(
       name="json-formatter",
       version="0.1.0",
       author="Your Name",
       description="A Python command line tool for formatting JSON data.",
       packages=find_packages(),
   )
   ```

4. Organize your code into a Python package structure if it's not already structured that way. Ensure that your command line tool's entry point (main function) is clearly defined and easily accessible.

5. Consider adding a `requirements.txt` file if your tool depends on external packages. List the required packages and their versions in this file.

6. Build your Python package by using the `build` package or using `setup.py` with `setuptools`:

   ```bash
   python setup.py sdist bdist_wheel
   ```

   This command will create a distribution package of your tool.

7. Once the distribution package is built, you can publish it to the Python Package Index (PyPI) or another package repository. PyPI is the most commonly used repository for Python packages.

8. To distribute your tool widely, you can publish it on PyPI. You'll need to create an account on PyPI if you don't have one, and then you can use tools like `twine` to upload your package.


**Bonus challenge:** Explore creating a user-friendly documentation page for your tool, either on your GitHub repository or a dedicated documentation platform. Consider using tools like Sphinx to generate documentation from docstrings in your code.

**Concepts Covered:**

- [x] Packaging and distributing a Python command line tool as a Python package.
- [x] Defining project metadata in a `setup.py` file.
- [x] Organizing code into a Python package structure.
- [x] Building a distribution package with `setuptools`.
- [x] Publishing and distributing Python packages on PyPI.
- [x] Documentation best practices for Python projects.

By completing this lab, you will have taken your Python command line tool to the next level by packaging and releasing it as a Python package. This experience will help you understand the practical aspects of sharing Python software and prepare you for real-world scenarios where you need to package and distribute your Python tools.
