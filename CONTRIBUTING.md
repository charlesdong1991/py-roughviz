# Contributing code

In this project, we follow a strict pull request process. Work in short-lived branches and submit a pull request when ready.
Reviewer merges if everything is okay, but typically you will get feedback.

## Code style
[PEP 8](https://www.python.org/dev/peps/pep-0008/) with the following modifications:
- line length = 100 rather than 79 
- [Google DocStrings](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings)
- Use `'` instead of `"` as string quote.

## Pre-commit checks
Before each commit, make sure that:

- all tests work by running `pytest`
- there are no `flake8` warnings

The `black` code formatter is not officially supported, but is suggested.

## Running tests
In root of repo, simply run `pytest`.
