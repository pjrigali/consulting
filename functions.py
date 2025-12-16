import csv

# Read csv's.
def read_csv(path: str, nrows: int = 0) -> list:
    # Check if file is a csv.
    if not path.endswith('.csv'):
        path = path + '.csv'

    with open(path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        if csv_reader.fieldnames:
            csv_reader.fieldnames = [name.lstrip("\ufeff") for name in csv_reader.fieldnames]

        if nrows:
            return [next(csv_reader) for _ in range(nrows)]
        else:
            return [row for row in csv_reader]
