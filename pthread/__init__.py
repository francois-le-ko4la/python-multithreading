#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# pthread
## Description:

This package provide a simple way to manage multithreading in python project.

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
..
├── last_check.log
├── LICENSE
├── Makefile
├── MANIFEST.in
├── pictures
│   ├── classes_pthread.png
│   └── packages_pthread.png
├── pthread
│   ├── __about__.py
│   ├── __init__.py
│   └── thread.py
├── README.md
├── requirements.txt
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

## License

This package is distributed under the [GPLv3 license](./LICENSE)

"""


import pthread.__about__
from pthread.thread import PThread
