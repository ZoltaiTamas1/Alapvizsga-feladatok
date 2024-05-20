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

def bekeres():
    sorszam = None
    while sorszam is None or not (1 <= sorszam <= 5):
        sorszam_input = input("Elem sorszáma (1-5): ")
        if sorszam_input.isdigit():
            sorszam = int(sorszam_input)
            if not (1 <= sorszam <= 5):
                print("Kérem, egy 1 és 5 közötti számot adjon meg!")
        else:
            print("Érvénytelen bemenet, kérem, egy számot adjon meg!")
    return sorszam

def main():
    bev_lista = []
    kilep = 'N'
    while kilep != 'I':
        sorszam = bekeres()
        tetel_hozzaadasa(sorszam, bev_lista)
        bevlista_megjelenites(bev_lista)
        kilep = input("Ki szeretne lépni [I/N]? ").strip().upper()
        print()

main()
