![Anagrams](https://raw.githubusercontent.com/HernanSaltiveri/hsanagrams/refs/heads/main/resources/headerreadme.png)


# Anagrams

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/hernansaltiveri/hsanagrams/build.yml?label=Build)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/hernansaltiveri/hsanagrams/test.yml?label=Test)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/hernansaltiveri/hsanagrams/publish.yml?label=Publish)
![GitHub last commit](https://img.shields.io/github/last-commit/hernansaltiveri/hsanagrams)
![GitHub License](https://img.shields.io/github/license/hernansaltiveri/hsanagrams)
![GitHub repo size](https://img.shields.io/github/repo-size/hernansaltiveri/hsanagrams?color=green)


This tool is designed to retrieve a list of anagram words based on a dictionary with all the posible words and a target search word. All the words in the retrieved list will be an anagram of the provided search word.


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Publish](#publish)
- [Organization](#organization)
- [License](#license)

## Features

Given a words.txt file containing a newline-delimited list of dictionary
words, this project will retrieve the list of items containing all the anagrams from words.txt for a given word.

Examples:

> For the word: 'plates' some anagrams are 'palest', 'pastel', 'petals', 'plates' and 'staple'. If the provided list contains those values they will be retrieved.

'plates' > 'palest', 'pastel', 'petals', 'plates' and 'staple'
    
> Another example would be for the word 'eat' some posible retrieve values are 'ate', 'eat' are 'tea' (if they where on the input list)

## Installation

- How to install it from pypi
```
pip install hsanagrams
```

- How to build it from source

```
python scripts/build.py
```

- How to install it from source

After building
```
pip install dist/hsanagrams-0.5.0-py3-none-any.whl
```

## Usage

```
#
hsanagrams 'eat' pathtofilewithwords/words.txt
['ate', 'eat', 'tea']

```

also a usage can be explored [here](test/tests.ipynb)

## Publish

This is how to push a new version to pypi. This code is also used by the publish.yml workflow.

https://pypi.org/project/hsanagrams/

```
python scripts/publish.py
```
## Organization

```
.
├── LICENSE.md
├── README.md
├── VERSION.txt
├── __init__.py
├── __pycache__
│   └── __init__.cpython-313.pyc
├── app.py
├── dist
│   └── hsanagrams-0.6.19-py3-none-any.whl
├── docs
│   ├── AUTHORS.md
│   ├── CODE_OF_CONDUCT.md
│   ├── CONTRIBUTING.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── SECURITY.md
│   └── SUPPORT.md
├── header.svg
├── pyproject.toml
├── requirements.txt
├── resources
│   ├── github-header-banner.png
│   └── headerreadme.png
├── scripts
│   ├── build.py
│   ├── codequality.py
│   ├── publish.py
│   ├── run_tests.py
│   └── tomlversion.py
├── src
│   ├── __init__.py
│   └── hsanagrams
│       ├── __init__.py
│       ├── __main__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-313.pyc
│       │   ├── __main__.cpython-313.pyc
│       │   └── anagrams.cpython-313.pyc
│       ├── anagrams.py
│       └── anagrams.pyi
├── test
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   └── testanagrams.cpython-313-pytest-9.2.0.pyc
│   ├── testanagrams.py
│   ├── tests.ipynb
│   └── words.txt
├── test-results
│   └── report.xml
└── uv.lock
```

## License

Distributed under the MIT License. See `LICENSE` for more information.