"""4)	Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la
linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.

Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista
finală. """

import sys
import os


def extensii_unice(director):
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

    if len(sys.argv) != 2:
        sys.exit("Programul primeste exact un parametru")
    if not os.path.isdir(sys.argv[1]):
        sys.exit("Calea pusa la dispozitie nu reprezinta un directoar valid")

    extensii = extensii_unice(sys.argv[1])
    print(extensii)


if __name__ == "__main__":
    main()
