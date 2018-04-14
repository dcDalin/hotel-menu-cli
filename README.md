# Menu CLI API

[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/dcDalin/hotel-menu-cli) [![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://github.com/dcDalin/hotel-menu-cli) ![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)

This is a Python Click CLI backed by a Python Flask API implementation of a relatively simple Hotel Menu ordering sort of system.

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#### Install

Clone the repository

```sh
$ git clone https://github.com/dcDalin/hotel-menu-cli.git
```

Change Directory to the now cloned folder

```sh
$ cd hotel-menu-cli
```

Create a virtual environment

```sh
$ python3.6 -m venv venv
```

Activate the virtual environment

```sh
$ source venv/bin/activate
```

Install the project dependencies

```sh
$ pip install -r requirements.txt
```

Install the CLI on the virtual environment

```sh
$ pip install --editable .
```

Project depends on [Python 3.6](https://www.python.org/downloads/) and [pip](https://pypi.python.org/pypi).

#### Usage

Run the server - Start the API service

```sh
$ python3.6 run.py
```

Run the CLI, get help

```sh
$ mymenu --help
```

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/dcDalin/)

**Dalin Oluoch**

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/dcDalin/hotel-menu-cli/blob/master/LICENSE) file for details
