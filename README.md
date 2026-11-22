![Anagrams](https://raw.githubusercontent.com/HernanSaltiveri/hsanagrams/refs/heads/main/resources/headerreadme.png)

<div align="center">


![GitHub repo size](https://img.shields.io/github/repo-size/hernansaltiveri/hsanagrams)
![GitHub last commit](https://img.shields.io/github/last-commit/hernansaltiveri/hsanagrams)
![GitHub License](https://img.shields.io/github/license/hernansaltiveri/hsanagrams)
![Static Badge](https://img.shields.io/badge/Build-Sucessfull-Green)
![Static Badge](https://img.shields.io/badge/Test-Sucessfull-Green)



</div>


# Anagrams





This tool is designed to retrieve a list of anagram words based on a dictionary with all the posible words and a target search word. All the words in the retrieved list will be an anagram of the provided search word.


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Publish](#publish)
- [Contributing](#contributing)
- [License](#license)

## Features
This tool is designed to retrieve a list of anagram words based on a dictionary with all the posible words and a target search word. All the words in the retrieved list will be an anagram of the provided search word.

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

## Publish

This is how to push a new version to pypi. This code is also used by the publish.yml workflow.

```
python scripts/publish.py
```
## Contributing


## License

Distributed under the MIT License. See `LICENSE` for more information.