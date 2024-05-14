def prova():
    with open("FastApi_Botiga/llista_productes.csv", "r", encoding="UTF-8") as fitxer:
            saltLinia = fitxer.readline()
            linia = fitxer.readline()
            list_elements = []
            while linia:
                list_elements = linia.split(",")
                print (list_elements)
                linia = fitxer.readline()
def main():
     t = prova()

if __name__ == "__main__":
    main()