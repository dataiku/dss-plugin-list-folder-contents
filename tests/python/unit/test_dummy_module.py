# -*- coding: utf-8 -*-
# This is a test file intended to be used with pytest
# pytest automatically runs all the function starting with "test_"
# see https://docs.pytest.org for more information
import collections

import pytest
from lib import get_level_mapping, compute_columns_from_path
import datetime


def test_get_level_mapping_1():
    param = [{"from": "1", "to": "Chat"}]
    res = get_level_mapping(param)
    expected = {1: "Chat"}
    assert res == expected


def test_get_level_mapping_2():
    param = [{"from": "1", "to": "Chat"}, {"from": "2", "to": "Chien"}]
    res = get_level_mapping(param)
    expected = {1: "Chat", 2: "Chien"}
    assert res == expected


def test_get_level_mapping_exception():
    param = [{"from": "salut", "to": "Chat"}, {"from": "2", "to": "Chien"}]
    with pytest.raises(ValueError):
        res = get_level_mapping(param)


def test_compute_columns_from_path_1():
    param = [{"from": "1", "to": "Chat"}, {"from": "2", "to": "Chien"}]
    mapping = get_level_mapping(param)
    path_detail = {'pathElts': ['', 'a', 'b', 'c', 'chien.com'], 'fullPath': "/a/b/c/chien.com", 'name': "chien.com",
                   'lastModified': 160000000, 'size': 12345}

    res = compute_columns_from_path(path_detail, mapping)
    expected = collections.OrderedDict()
    expected["path"] = "/a/b/c/chien.com"
    expected["basename"] = "chien"
    expected["extension"] = "com"
    expected["depth"] = 4
    expected['last_modified'] = datetime.datetime.fromtimestamp(160000000 / 1000.0)
    expected["size"] = 12345
    expected["Chat"] = "a"
    expected["Chien"] = "b"

    assert res == expected
