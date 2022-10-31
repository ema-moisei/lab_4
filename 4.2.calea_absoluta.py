"""2) Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a
fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A. """

import os


def cale_absoluta(director, fisier):
    for element in os.listdir(director):
        current_path = os.path.join(director, element)
        if os.path.isfile(current_path):
            if element.startswith("A"):
                if not os.path.isfile(fisier):
                    handler = open(fisier, "w")
                    handler.write(current_path)
                    handler.write("\n")
                else:
                    handler = open(fisier, "a")
                    handler.write(current_path)
                    handler.write("\n")
                handler.close()
    return 0


def main():

    director = ""
    fisier = ""
    cale_absoluta(director, fisier)


if __name__ == "__main__":
    main()
