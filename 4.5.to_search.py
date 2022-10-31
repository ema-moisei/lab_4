"""5) Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și
returneaza o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier,
se caută doar in fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director.
 Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError
 cu un mesaj corespunzator."""

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


def check(target, to_search):
    try:
        if os.path.isdir(target):
            to_search_dir(target, to_search)
        elif os.path.isfile(target):
            to_search_file(target, to_search)
        else:
            raise ValueError("The argument does not represent a file path or a folder path")

    except ValueError as Value_Error:
        print(Value_Error)


def main():

    path = ""
    check(path, "")
    global file_list
    if file_list:
        print(file_list)


if __name__ == "__main__":
    main()
