"""
The function details the files within a given folder. Useful for discovering what extracts/csv's that you have captured.
"""
from pathlib import Path
import datetime
from file_handling_functions import read_csv


def _file(file) -> dict:
    """Collects file level information. Returns a dictionary."""
    # If CSV, include the columns in the file.
    cols = ()
    if file.suffix == '.csv':
        lst = read_csv(path=str(file.parent) + '\\' + str(file.name), nrows=1)
        if lst:
            cols = tuple(lst[0].keys())

    return {'location': str(file.resolve()), 
            'folder_name': str(file.parent), 
            'file_name': file.name, 
            'file_type': file.suffix, 
            'file_size': f'{round(file.stat().st_size / (1024 * 1024), 4)} mbs', 
            'dt_access': datetime.datetime.fromtimestamp(file.stat().st_atime), 
            'dt_modified': datetime.datetime.fromtimestamp(file.stat().st_mtime), 
            'dt_created': datetime.datetime.fromtimestamp(file.stat().st_ctime),
            'columns': cols}


def _gather(location) -> list:
    """Grabs the individual file infomation."""
    temp = []
    if location.is_dir():
        for item in location.iterdir():
            if item.is_file():
                temp.append(_file(file=item))
    elif location.is_file():
        temp.append(_file(file=location))
    else:
        raise ValueError("Not files or directory found.")
    return temp


# TODO
# Collect file information inside a given folder.
# Include columns when csv
# Export to its own csv
# create hyperlinks for each file. So they are openable from the export csv.
def describe_folder(folder: str | list) -> list:
    """Folder can be a single str of a folder or a list of folder locations."""
    lst = []
    # Single folder
    if isinstance(folder, str):
        root_location = Path(folder)
        lst.extend(_gather(location=root_location))

    # List of folders.
    elif isinstance(folder, list):
        for f in folder:
            root_location = Path(f)
            lst.extend(_gather(location=root_location))
    return lst
