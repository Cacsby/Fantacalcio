import pandas as pd
import random

class Giocatore:
    def __init__(self, nome_giocatore: str, prezzo: int):
        self.nome_giocatore = nome_giocatore
        self.prezzo = prezzo

class Squadra:
    def __init__(self, nome_squadra: str):
        self.nome_squadra = nome_squadra
        self.crediti_totali = 500
        self.squadra = []

def fantacalcio(self):
    team1 = Squadra("milan")
    team2 = Squadra("roma")


    # Specifica il percorso del file .xlsx
    file_path = 'C:\\Users\\user\\Desktop\\Quotazioni_Fantacalcio_Stagione_2024_25.xlsx'

    # Legge il file Excel
    df = pd.read_excel(file_path)

    # Stampa il contenuto del file
    print(df)

    # Se vuoi accedere a un foglio specifico, puoi farlo così:
    df = pd.read_excel(file_path, sheet_name='Portieri', usecols='D')
    # Seleziona una colonna specifica
    # colonna_specifica = df['Nome']
    lista_giocatori = df.values.tolist()
    lista_giocatori.remove(lista_giocatori[0])

    while lista_giocatori:
        numero_random_lista_giocatori = random.randint(0, len(lista_giocatori))

        giocatore_estratto = lista_giocatori[numero_random_lista_giocatori]

        squadra_vincente_giocatore = "carico"

        if squadra_vincente_giocatore == "carico":
            crea_giocatore_inserisci_in_squadra(self,giocatore_estratto, 200, team1, lista_giocatori)


        elif squadra_vincente_giocatore == "cac":
            cac.squadra.append(giocatore_estratto)
            lista_giocatori.remove(giocatore_estratto)


    print(df)


def crea_giocatore_inserisci_in_squadra(self, nome_giocatore: str, prezzo: int, squadra_vincente_giocatore: Squadra, lista_giocatori: list):
    squadra_vincente_giocatore.squadra.append(Giocatore(nome_giocatore, prezzo))
    aggiorna_crediti_rimanenti(squadra_vincente_giocatore, prezzo)
    lista_giocatori.remove(nome_giocatore)

def aggiorna_crediti_rimanenti(squadra_vincente_giocatore: Squadra, prezzo:int):
    if(squadra_vincente_giocatore.crediti_totali > prezzo):
        squadra_vincente_giocatore.crediti_totali = squadra_vincente_giocatore.crediti_totali - prezzo
    else:
        print("crediti insufficienti")