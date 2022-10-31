"""1)	Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul dat
ca parametru.
Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’ """

import os


def sort_crescator(director):
    sorted_list = []
    for element in os.listdir(director):
        current_path = os.path.join(director, element)
        if os.path.isfile(current_path):
            ext = os.path.splitext(current_path)[1][1:]
            sorted_list.append(ext.lower())
    sorted_list = set(sorted_list)
    sorted_list = list(sorted_list)
    sorted_list.sort()

    return sorted_list


def main():

    path = ""
    sorted_list = sort_crescator(path)
    print(sorted_list)


if __name__ == "__main__":
    main()

