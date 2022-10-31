"""7) Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si
returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier,
file_size = dimensiunea fisierului in octeti, file_extension = extensia fisierului (daca are) sau "",
can_read, can_write = True/False daca se poate citi din/scrie in fisier."""

import os


def path_dict(path):
    my_dict = {"full_path": "", "file_size": 0, "file_extension": "", "can_read": False, "can_write": False}
    my_dict["full_path"] = path
    my_dict["file_size"] = os.path.getsize(path)
    my_dict["file_extension"] = os.path.splitext(path)[1]
    if os.access(path, os.R_OK):
        my_dict["can_read"] = True
    if os.access(path, os.W_OK):
        my_dict["can_write"] = True

    return my_dict


def main():

    path = ""
    my_dict = path_dict(path)
    print(my_dict)


if __name__ == "__main__":
    main()
