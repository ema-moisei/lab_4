"""3)Să se scrie o funcție ce primește ca parametru un string my_path.
Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului.
Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count),
sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere
cu acea extensie. Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru. """

import os


def count(my_tuple):
    return my_tuple[1]


def fisier_sau_director(path):
    caractere = ""
    directoare = []
    ext_list = []
    # for file path
    if os.path.isfile(path):
        handler = open(path, "r")
        line = handler.readline().strip()
        while line:
            # check the lenght of the current line
            line_dif = 20 - len(line)
            # if the lenght is greater than 20 we save the last 20 chr
            if line_dif <= 0:
                caractere = line[-20:]
            # if the lenght of the current line is smaller than 20
            else:
                # the string is the last (20 - lenght of line) chr from the last string + current line
                caractere = caractere[-line_dif:] + line
            line = handler.readline().strip()
        handler.close()
    # for folder path
    if os.path.isdir(path):
        # Listing the contents of a folder recursively
        for dirpath, dirnames, filenames in os.walk(path):
            for file in filenames:
                # get the extension
                ext = os.path.splitext(file)[1]
                ext = ext.lower()
                # check if is the first time we encounter it
                if ext not in ext_list:
                    ext_list.append(ext)
                    my_list = [ext, 1]
                    directoare.append(my_list)
                else:
                    # if we did increment the counter
                    for element in directoare:
                        if ext == element[0]:
                            element[1] += 1
        directoare.sort(reverse=True, key=count)
    final_list = []
    for element in directoare:
        final_list.append(tuple(element))

    return caractere, final_list


def main():

    path = ""
    caractere, directoare = fisier_sau_director(path)
    if caractere:
        print("The path is representing a file and the last 20 characters form this file are: ", caractere)
    else:
        print("The path is representing a folder and in this folder you can find the following files: ", directoare)


if __name__ == "__main__":
    main()
