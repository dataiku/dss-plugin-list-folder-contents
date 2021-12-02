# -*- coding: utf-8 -*-
import pandas as pd

import dataiku
from dataiku.customrecipe import get_recipe_config, get_input_names_for_role, get_output_names_for_role

from lib import get_level_mapping, compute_columns_from_path
from dku_io_utils import generate_path_list

input_folder = dataiku.Folder(get_input_names_for_role("input_folder")[0])
output_dataset = dataiku.Dataset(get_output_names_for_role("output_dataset")[0])
level_mapping_string = get_recipe_config().get('level_mapping')

mapping = get_level_mapping(level_mapping_string)

path_details_list = generate_path_list(input_folder)

list_row_path = pd.DataFrame([compute_columns_from_path(path_detail, mapping) for path_detail in path_details_list])

output_dataset.write_with_schema(list_row_path)