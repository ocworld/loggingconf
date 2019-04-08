# loggingconf
[![PyPI version shields.io](https://img.shields.io/pypi/v/ansicolortags.svg)](https://pypi.org/project/loggingconf/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.org/project/loggingconf/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

## Description
This Module helps to load a configration file for logging module

## Install
```bash
pip install -U loggingconf
```

## Example
```python
import loggingconf
loggingconf.file_config('logconf.ini')
loggingconf.file_config('logconf.yaml')
loggingconf.file_config('logconf.json')
```

## Python Versions
Python 2.7, 3.4, 3.5, 3.6, 3.7
