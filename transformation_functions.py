import re
import unicodedata
import datetime


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


def rsc(s: str) -> str:
    """Remove special chars."""
    return re.sub(r'[^A-Za-z0-9\s]', '', s)


def remove_diacritics(s: str) -> str:
    """Removes diacritics, strips them from strings. Useful when dealing with str's of different languages."""
    n_t = unicodedata.normalize('NFD', s)
    return ''.join(c for c in n_t if unicodedata.category(c) != 'Mn')


def to_datetime(s: str) -> datetime.datetime:
    """Basic datetime conversions."""
    if s:
        if '/' in s:
            return datetime.datetime.strptime(s, "%m/%d/%Y")
        elif s.endswith('+0000'):
            return datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%S.%f%z')
        else:
            return datetime.datetime.strptime(s, "%Y-%m-%d")
    else:
        return None