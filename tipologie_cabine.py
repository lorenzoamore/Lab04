from cabina import Cabina

class CabinaAnimali(Cabina):
    def __init__(self, codice_cabina,numero_letti, numero_ponte, prezzo, max_animali):
        super().__init__(codice_cabina,numero_letti, numero_ponte, prezzo)
        self.max_animali = int(max_animali)

    def ottimizza_prezzo(self,prezzo):
        self.prezzo = float(prezzo)*(1 + 0.1 * float(self.max_animali))

    def __str__(self):
        return f"{super().__str__()} | Numero massimo animali: {self.max_animali}"

class CabinaDeluxe(Cabina):
    def __init__(self,codice_cabina,numero_letti,numero_ponte,prezzo,tipologia):
        super().__init__(codice_cabina,numero_letti,numero_ponte,prezzo)
        self.tipologia = tipologia
        self.prezzo = float(prezzo)*1.2

    def __str__(self):
        return f"{super().__str__()} |Tipologia:  {self.tipologia}"

    def ottimizza_prezzo(self,prezzo):
        self.prezzo = float(prezzo)*1.2

