from csv import reader
from cabina import Cabina
from tipologie_cabine import CabinaAnimali, CabinaDeluxe
from passeggero import Passeggero


class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self.listaCabine = []
        self.listaPasseggeri = []
        self.listaCabinePasseggeri = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            with open(file_path, newline='') as csvfile:
                file = reader(csvfile)
                for line in file:
                    if "CAB" in line[0]:
                        if len(line) == 4:
                            codice_cabina, numero_letti, numero_ponte, prezzo = line
                            cabina = Cabina(codice_cabina,numero_letti, numero_ponte, prezzo)
                            self.listaCabine.append(cabina)
                        elif line[4] == "Moderna" or line[4]=="Lussuosa" or line[4]=="Classica":
                            codice_cabina, numero_letti, numero_ponte, prezzo, tipologia = line
                            cabina = CabinaDeluxe(codice_cabina,numero_letti, numero_ponte, prezzo, tipologia)
                            cabina.ottimizza_prezzo(prezzo)
                            self.listaCabine.append(cabina)
                        else:
                            codice_cabina, numero_letti, numero_ponte, prezzo, max_animali = line
                            cabina = CabinaAnimali(codice_cabina,numero_letti, numero_ponte, prezzo, max_animali)
                            cabina.ottimizza_prezzo(prezzo)
                            self.listaCabine.append(cabina)
                    else:
                        codice_passeggero, nome, cognome = line
                        passeggero = Passeggero(codice_passeggero, nome, cognome)
                        self.listaPasseggeri.append(passeggero)
        except FileNotFoundError:
            print("File not found")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        from assegna_passeggero_a_cabina import AssegnaPasseggero
        trovato = False
        for cabina in self.listaCabine:
            if codice_cabina == cabina.codice_cabina:
                trovato = True
                break
        if not trovato:
            raise Exception ("Cabina non esistente")

        trovato = False
        for passeggero in self.listaPasseggeri:
            if codice_passeggero == passeggero.codice_passeggero:
                trovato = True
                break
        if not trovato:
            raise Exception ("Passeggero non esistente")

        trovato = False
        for prenotazione in self.listaCabinePasseggeri:
            if codice_cabina == prenotazione.codice_cabina or codice_passeggero == prenotazione.codice_passeggero:
                trovato = True
                raise Exception ("Passeggero o cabina occupati")
        if not trovato:
            prenotazione = AssegnaPasseggero(codice_cabina, codice_passeggero)
            self.listaCabinePasseggeri.append(prenotazione)

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        #self.listaCabine.sort(key=lambda cabina: cabina.prezzo)
        #return self.listaCabine
        listaOrdinata = []
        listaOrdinata = sorted(self.listaCabine)
        return listaOrdinata




    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for passeggero in self.listaPasseggeri:
            trovato = False
            for prenotazione in self.listaCabinePasseggeri:
                if passeggero.codice_passeggero == prenotazione.codice_passeggero:
                    for cabina in self.listaCabine:
                        if cabina.codice_cabina == prenotazione.codice_cabina:
                            print(f"{passeggero} ha prenotato la cabina: {cabina}")
                            trovato = True
                            break
            if not trovato:
                print(passeggero)




