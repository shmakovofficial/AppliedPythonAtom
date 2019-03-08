import sys
from homeworks.homework_02.charset_detect import charset
from homeworks.homework_02.formation_detect import formation
from homeworks.homework_02.file_tools import printing, testing

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except IndexError:
        raise SystemExit("Filename not specified")
    testing(file_name)
    file_charset = charset(file_name)
    file_format = formation(file_name, file_charset)
    printing(file_name, file_charset, file_format)
