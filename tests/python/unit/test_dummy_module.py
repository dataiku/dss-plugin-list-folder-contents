# -*- coding: utf-8 -*-
# This is a test file intended to be used with pytest
# pytest automatically runs all the function starting with "test_"
# see https://docs.pytest.org for more information
import pytest
from lib import get_level_mapping, compute_columns_from_path


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
    path_detail = {'fullPath': "/a/b/c/chien.com", 'name': "chien.com", 'lastModified': 160000000/1000, 'size': 12345}

    res = compute_columns_from_path(path_detail, mapping)
    expected = {"Chat": "a", "Chien": "b", "path": "/a/b/c/chien.com", "filename": 'chien', "extension": "com", "depth": 4, "last_modified": datetime.datetime.fromtimestamp(160000000/1000), "size": 12345}
    assert res == expected