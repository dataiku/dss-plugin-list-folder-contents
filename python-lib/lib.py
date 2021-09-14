from typing import Dict, List

def params_validation(params):
    assert NotImplemented

def get_level_mapping(level_mapping_string: List[Dict]):

    # key_value_s = [key_value.split(':') for key_value in level_mapping_string.split(',')]
    try:
        mapping = {int(from_to["from"]): from_to["to"] for from_to in level_mapping_string}
        return mapping
    except ValueError as e:
        raise ValueError("The key must be an integer. ", e)


def compute_columns_from_path(path: str, mapping: Dict):
    subdirectories_file = path.split('/')
    res = {}
    for key, value in mapping.items():
        try:
            res[value] = subdirectories_file[key]
        except IndexError:
            res[value] = ""
    res["path"] = path
    return res
