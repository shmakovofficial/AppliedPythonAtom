import sys
from file_tools import charset
from json_tools import print_json
from tsv_tools import print_tsv

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        file_charset = charset(file_name)
        try:
            print_json(file_name, file_charset)
        except ValueError:
            print_tsv(file_name, file_charset)
    except (FileNotFoundError, IndexError):
        print("Файл не валиден")
    except (ValueError, RuntimeError) as e:
        print(e.args[0])
