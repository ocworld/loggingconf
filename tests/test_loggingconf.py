# -*- coding: utf-8 -*-

import os
import pytest
import loggingconf


@pytest.fixture
def resource_dir_path():
    current_path = os.path.realpath(__file__)
    current_dir_path = os.path.dirname(current_path)
    resources_dir_path = os.path.join(current_dir_path, 'resources')
    yield resources_dir_path


def test_file_config_ini(resource_dir_path):
    logconf_path = os.path.join(resource_dir_path, 'logconf.ini')
    loggingconf.file_config(logconf_path)


def test_file_config_yaml(resource_dir_path):
    logconf_path = os.path.join(resource_dir_path, 'logconf.yaml')
    loggingconf.file_config(logconf_path)


def test_file_config_json(resource_dir_path):
    logconf_path = os.path.join(resource_dir_path, 'logconf.json')
    loggingconf.file_config(logconf_path)
