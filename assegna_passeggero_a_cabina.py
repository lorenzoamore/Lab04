
class AssegnaPasseggero:
    def __init__(self,codice_cabina,codice_passeggero):
        self.codice_cabina = codice_cabina
        self.codice_passeggero = codice_passeggero

    def __str__(self):
        return f" Cabina: {self.codice_cabina} | Passeggero: {self.codice_passeggero}"