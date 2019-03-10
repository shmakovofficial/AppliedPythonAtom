import sys
from charset_detect import charset
from formation_detect import formation
from file_tools import printing, testing

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Файл не валиден")
    else:
        try:
            testing(file_name)
        except SystemExit:
            print("Файл не валиден")
        else:
            try:
                file_charset = charset(file_name)
                file_format = formation(file_name, file_charset)
                printing(file_name, file_charset, file_format)
            except SystemExit:
                print("Формат не валиден")
