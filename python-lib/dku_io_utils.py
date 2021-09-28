from typing import List, Dict
import dataiku


def generate_path_list(folder: dataiku.Folder) -> List[Dict]:
    """Generate a dataframe of file paths in a Dataiku Folder matching a list of extensions
    Args:
        folder: Dataiku managed folder where files are stored
            This folder can be partitioned or not, this function handles both
        file_extensions: list of file extensions to match, ex: ["JPG", "PNG"]
            Expected format is not case-sensitive but should not include leading "."
        path_column: Name of the column in the output dataframe
    Returns:
        DataFrame with one column named `path_column` with all the file paths matching the list of `file_extensions`
    Raises:
        RuntimeError: If there are not files matching the list of `file_extensions`
    """
    path_list = []
    if folder.read_partitions:
        for partition in folder.read_partitions:
            path_list += folder.list_paths_in_partition(partition)
    else:
        path_list = folder.list_paths_in_partition()


    return [folder.get_path_details(path) for path in path_list]
