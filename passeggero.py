
class Passeggero:
    def __init__(self, codice_passeggero, nome, cognome):
        self.codice_passeggero = codice_passeggero
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f"Codice passeggero: {self.codice_passeggero} | Nome: {self.nome} | Cognome: {self.cognome}"