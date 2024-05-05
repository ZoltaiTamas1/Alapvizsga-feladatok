class Kor:
    def __init__(self, sor: str):
        # Rajtszám;Versenyző;Konstruktőr;Szakasz;Futott idő
        adatok: list[str] = sor.strip().split(';')
        
        self.rajtszam = adatok[0]
        self.versenyzo = adatok[1]
        self.konstruktor = adatok[2]
        self.szakasz = adatok[3]
        self.futott_ido = adatok[4]
        
        
    def futott_ido_masodpercben(self) -> int:
        masodpercben = int(self.futott_ido.split(':')[0]) * 60 + float(self.futott_ido.split(':')[1])
        return masodpercben