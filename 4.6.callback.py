"""6)	Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că
primește un parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută în
procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru."""

import os

file_list = []


def to_search_file(target, to_search):
    global file_list
    handler = open(target, "r")
    line = handler.readline().strip()
    while line:
        if to_search in line:
            file_list.append(target)
            break
        line = handler.readline().strip()
    handler.close()


def to_search_dir(target, to_search):
    for dirpath, dirnames, filenames in os.walk(target):
        for file in filenames:
            current_path = os.path.join(dirpath, file)
            to_search_file(current_path, to_search)


def print_exception(e):
    print(e)


def check(target, to_search, callback):
    try:
        if os.path.isdir(target):
            to_search_dir(target, to_search)
        elif os.path.isfile(target):
            to_search_file(target, to_search)
        else:
            raise ValueError("The argument does not represent a file path or a folder path")

    except ValueError as e:
        callback(e)


def main():

    path = ""
    check(path, "", print_exception)
    global file_list
    if file_list:
        print(file_list)


if __name__ == "__main__":
    main()
