import csv


# Read csv's.
def read_csv(path: str, nrows: int = 0) -> list:
    """Simple csv reader, fixes keys, returns the csv as a list of dicts."""
    # Check if file is a csv.
    if not path.endswith('.csv'):
        path = path + '.csv'

    with open(path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        # Catch and fix key names.
        if csv_reader.fieldnames:
            csv_reader.fieldnames = [name.lstrip("\ufeff") for name in csv_reader.fieldnames]

        # Only read in x lines.
        if nrows:
            return [next(csv_reader) for _ in range(nrows)]
        else:
            return [row for row in csv_reader]
