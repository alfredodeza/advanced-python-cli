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