def _is_utf16(filename: str):
    try:
        with open(filename, encoding='utf16') as f:
            s = f.read(8)
    except UnicodeError:
        return False
    return True


def _is_utf8(filename: str):
    try:
        with open(filename, encoding='utf8') as f:
            s = f.read(8)
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


def printing(list_of_lists: list, headers=True):
    if len(list_of_lists) < 1:
        raise ValueError("Формат не валиден")
    for i in list_of_lists:
        if len(i) != len(list_of_lists[0]) or len(i) == 0:
            raise ValueError("Формат не валиден")
    lengths = list()
    for i in range(len(list_of_lists[0])):
        current_length = 0
        for j in list_of_lists:
            current_length = max(len(str(j[i])), current_length)
        lengths.append(current_length)
    print("-" * (sum(lengths) + 5 * len(lengths) + 1))
    if headers:
        data_headers = list_of_lists.pop(0)
        for i, j in enumerate(data_headers):
            print("|  {:^{width}}  ".format(j, width=lengths[i]), end='')
        print("|")
    for i in list_of_lists:
        for j, k in enumerate(i):
            output = "|  {:" + (">" if j == len(i) - 1 else "<") + "{width}}  "
            print(output.format(k, width=lengths[j]), end='')
        print("|")
    print("-" * (sum(lengths) + 5 * len(lengths) + 1))
