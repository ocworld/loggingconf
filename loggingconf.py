# -*- coding: utf-8 -*-

import os
import logging.config
import yaml
import json
import io


def file_config(fname, encoding='utf-8'):
    fmt2func = {'.yaml': _yaml_config,
                '.yml': _yaml_config,
                '.json': _json_config,
                '.ini': _ini_config}

    _, ext = os.path.splitext(fname)
    fmt2func[ext](fname, encoding)


def _yaml_config(fname, encoding='utf-8'):
    with io.open(fname, mode='r', encoding=encoding) as f:
        data = yaml.safe_load(f)
        logging.config.dictConfig(data)


def _json_config(fname, encoding='utf-8'):
    with io.open(fname, mode='r', encoding=encoding) as f:
        data = json.load(f)
        logging.config.dictConfig(data)


def _ini_config(fname, *unused):
    del unused
    logging.config.fileConfig(fname)

