class Giocatore:
    def __init__(self, nome_giocatore: str, prezzo: int):
        self.nome_giocatore = nome_giocatore
        self.prezzo = prezzo

class Portiere:
    def __init__(self):
        self.portieri = []

class Difensore(Giocatore):
    def __init__(self, nome_giocatore: str, prezzo: int):
        super().__init__(nome_giocatore, prezzo)

class Centrocampista(Giocatore):
    def __init__(self, nome_giocatore: str, prezzo: int):
        super().__init__(nome_giocatore, prezzo)

class Attaccante(Giocatore):
    def __init__(self, nome_giocatore: str, prezzo: int):
        super().__init__(nome_giocatore, prezzo)

class Giocatori:
    def __init__(self, nome_squadra: str):
        self.nome_squadra = nome_squadra
        self.crediti_totali = 500
        self.squadra = Giocatori

class Squadra:
    def __init__(self, nome_squadra: str):
        self.nome_squadra = nome_squadra
        self.crediti_totali = 500
        self.portieri = []
        self.difensori = []
        self.centrocampisti = []
        self.attaccanti = []
