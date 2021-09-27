import os
from typing import Dict, List
from collections import OrderedDict
import datetime

def params_validation(params):
    assert NotImplemented

def get_level_mapping(level_mapping_string: List[Dict]):

    # key_value_s = [key_value.split(':') for key_value in level_mapping_string.split(',')]
    try:
        mapping = {int(from_to["from"]): from_to["to"] for from_to in level_mapping_string}
        return mapping
    except ValueError as e:
        raise ValueError("The key must be an integer. ", e)


def compute_columns_from_path(path_detail: Dict, mapping: Dict):
    path = path_detail["fullPath"]
    subdirectories_file = path_detail["pathElts"]
    res = OrderedDict()
    res["path"] = path
    filename, file_extension = os.path.splitext(path_detail["name"])
    if path_detail["name"][-7:] == ".tar.gz":
        filename = path_detail["name"][:-7]
        file_extension = ".tar.gz"
    res["basename"] = filename
    res["extension"] = file_extension[1:]
    res["depth"] = len(subdirectories_file)-1
    res['last_modified'] = datetime.datetime.fromtimestamp(path_detail["lastModified"]/1000.0)
    res["size"] = path_detail["size"]

    for key, value in mapping.items():
        try:
            res[value] = subdirectories_file[key]
        except IndexError:
            res[value] = ""
    return res
