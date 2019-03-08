def _is_utf16(filename: str):
    try:
        with open(filename, encoding='utf16') as f:
            s = f.read(100)
    except UnicodeError:
        return False
    return True


def _is_utf8(filename: str):
    try:
        with open(filename, encoding='utf8') as f:
            s = f.read(100)
    except UnicodeError:
        return False
    return True


def charset(filename: str):
    if _is_utf16(filename):
        return 'utf16'
    elif _is_utf8(filename):
        return 'utf8'
    else:
        return 'cp1251'
