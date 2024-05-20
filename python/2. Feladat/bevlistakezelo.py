# bevlistakesz.py

bevlist = ["Alma", "Kenyér", "Tej", "Tojás", "Vaj"]

def tetel_hozzaadasa(sorszam, lista):
    tetel = bevlist[sorszam - 1]
    lista.append(tetel)
    print(f"A bevásárlólistához hozzáadva: {tetel}")
    print()


def bevlista_megjelenites(lista):

    print("Aktuális bevásárlólista:")
    for i, item in enumerate(lista, 1):
        print(f"{i}. {item}")
    print()
