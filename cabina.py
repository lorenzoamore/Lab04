
class Cabina:
    def __init__(self, codice_cabina,numero_letti, numero_ponte, prezzo):
        self.codice_cabina = codice_cabina
        self.numero_letti = numero_letti
        self.numero_ponte = numero_ponte
        self.prezzo = float(prezzo)

    def __str__(self):
        return f"{self.codice_cabina} | Numero letti: {self.numero_letti} | Numero Ponte: {self.numero_ponte} | Prezzo: {self.prezzo}"

    def __lt__(self, other):
        return self.prezzo < other.prezzo