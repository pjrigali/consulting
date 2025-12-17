import csv
import zipfile
from xml.etree.cElementTree import XML

# Read csv's.
def read_csv(path: str, nrows: int = 0) -> list:
    """Simple csv reader, fixes keys, returns the csv as a list of dicts."""
    # Check if file is a csv.
    if not path.endswith('.csv'):
        path = path + '.csv'

    with open(path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)

        # Catch and fix key names.
        if csv_reader.fieldnames:
            csv_reader.fieldnames = [name.lstrip("\ufeff") for name in csv_reader.fieldnames]

        # Only read in x lines.
        if nrows:
            return [next(csv_reader) for _ in range(nrows)]
        else:
            return [row for row in csv_reader]


# Save a list of dictionaries to a csv.
def save_csv(file_path: str, data: list, sort_columns: bool = False) -> None:
    """Takes a list of dictionaries and saves them to a csv. Assumes all the dict's have the same keys."""
    with open(file_path, mode='w', encoding='utf-8-sig', newline='') as file:
        # I know, first row? gross.
        cols = data[0].keys()
    
        if sort_columns:
            cols.sort()
        
        csv_writer = csv.DictWriter(file, fieldnames=cols, restval='', extrasaction='ignore')        
        csv_writer.writeheader()
        csv_writer.writerows(data)
        
    print(f'File created: ({file_path})')
    return None


# Read in a word doc file.
def read_docx(file_path: str) -> str:
    """Takes a file location/name and returns the contents of a word document as str."""
    # Capture the file.
    wn = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    p, t = wn + 'p', wn + 't'
    document = zipfile.ZipFile(file_path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)

    # Read in the paragraphs.
    paragraphs = []
    for paragraph in tree.iter(p):
        texts = [node.text for node in paragraph.iter(t) if node.text]
        if texts:
            paragraphs.append(''.join(texts))
    return '\n'.join(paragraphs)
