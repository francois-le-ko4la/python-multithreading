#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# pthread
## Description:

This package provide a simple way to manage multithreading in python project.

## Why:
- Clean the main code
- Simplify multithreading use with general objectives

## Why we will never use it:
- :x: All the code use multithreading
- :x: We use complex mecanisme between object: sync between object or data
  issue

## Setup:
```shell
git clone https://github.com/francois-le-ko4la/python-multithreading.git
cd python-multithreading
make install
```

## Test:
```shell
make test
```

## Use:

Take a look in the dev part.

## Project Structure
```
.
├── last_check.log
├── LICENSE
├── Makefile
├── pictures
│   ├── classes_pythread.png
│   └── packages_pythread.png
├── pythread
│   ├── __about__.py
│   ├── __init__.py
│   └── thread.py
├── README.md
├── runtime.txt
├── setup.cfg
├── setup.py
└── tests
    ├── test_doctest.py
    └── test_pycodestyle.py

```

## Todo:

- [X] Create the project
- [X] Write code and tests
- [X] Test installation and requirements (setup.py and/or Makefile)
- [X] Test code
- [X] Validate features
- [X] Write Doc/stringdoc
- [X] Run PEP8 validation
- [X] Clean & last check
- [X] Release
- [X] change (un)install process
- [X] remove MANIFEST.in
- [X] manage global var: __version__....
- [X] improve the doc
- [X] Release : 0.1.1
- [X] improve Makefile
- [X] Release : 0.1.2
- [X] validate (un)install process
- [X] rename module : pthread => pythread
- [X] Release : 1.0.0
- [X] fix setup
- [X] improve docstring
- [X] update doc
- [X] Release : 1.1.0

## License

This package is distributed under the [GPLv3 license](./LICENSE)

"""


from pytconfig.__about__ import (
    __version__,
    __email__,
    __author__,
    __url__,
    __license__
)
from pythread.thread import PThread
