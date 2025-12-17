import re
import unicodedata


def check_bool(s: str) -> bool:
    """Detects value level bool's."""
    if isinstance(s, str):
        if s in ('TRUE', 'True', 'true'):
            return True
        elif s in ('FALSE', 'False', 'false'):
            return False
        else:
            raise AttributeError(f'Unexpected bool value found ({s}).')
    elif isinstance(s, bool):
        return s
    else:
        raise AttributeError(f'Unexpected dataType found ({type(s)}) for ({s}).')


def rsc(t: str) -> str:
    """Remove special chars."""
    return re.sub(r'[^A-Za-z0-9\s]', '', t)


def remove_diacritics(input_string: str) -> str:
    """Removes diacritics, strips them from strings. Useful when dealing with str's of different languages."""
    normalized_string = unicodedata.normalize('NFD', input_string)
    return ''.join(c for c in normalized_string if unicodedata.category(c) != 'Mn')
