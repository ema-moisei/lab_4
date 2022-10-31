"""8) Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un
director aflat pe disc. Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina
directorului dir_path.

Exemplu apel funcție: functie("C:\\director") va returna ["C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]

Calea "C:\\director" are pe disc următoarea structură:
C:\\director\\fisier1.txt <- fișier
C:\\director\\fisier2.txt <- fișier
C:\\director\\director1 <- director
C:\\director\\director2 <- director"""

import os


def cai_abs_rad(dir_path):
    lista_cai = []
    for element in os.listdir(dir_path):
        current_path = os.path.join(dir_path, element)
        if os.path.isfile(current_path):
            lista_cai.append(current_path)
    return lista_cai


def main():

    dir_path = ""
    lista_cai = cai_abs_rad(dir_path)
    print(lista_cai)


if __name__ == "__main__":
    main()
