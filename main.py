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

    fantacalcio = []
    fantacalcio.append(team1)
    fantacalcio.append(team2)


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

    #remove se si toglie prima riga file
    lista_giocatori.remove(lista_giocatori[0])

    while lista_giocatori:
        numero_random_lista_giocatori = random.randint(0, len(lista_giocatori))

        giocatore_estratto = lista_giocatori[numero_random_lista_giocatori]

        esito = "yes"
        print(f"Giocatore estratto: {giocatore_estratto}")

        while esito == "yes":

            if giocatore_estratto not in lista_giocatori:
                lista_giocatori.remove(giocatore_estratto)
            print(f"Quale squadra si è aggiudicato {giocatore_estratto}?")
            stampa_tutte_squadre(self, fantacalcio)

            squadra_vincente_giocatore = int(input(""))

            print(f"Quanto è stato pagato: {giocatore_estratto}")

            prezzo_giocatore_estratto = int(input(""))

            print(f"Devi modificare qualcosa?")

            esito = input("yes/no")


        # squadra_vincente_giocatore = "carico"

        if squadra_vincente_giocatore == 0:
            if is_max_portieri(self, team1) == False:
                crea_giocatore_inserisci_in_squadra(self,giocatore_estratto, prezzo_giocatore_estratto, team1, lista_giocatori)


        elif squadra_vincente_giocatore == 1:
            if is_max_portieri(self, team2) == False:
                crea_giocatore_inserisci_in_squadra(self, giocatore_estratto, prezzo_giocatore_estratto, team2,
                                                lista_giocatori)

    print(df)


def crea_giocatore_inserisci_in_squadra(self, nome_giocatore: str, prezzo: int, squadra_vincente_giocatore: Squadra, lista_giocatori: list):
    squadra_vincente_giocatore.squadra.append(Giocatore(nome_giocatore, prezzo))
    aggiorna_crediti_rimanenti(squadra_vincente_giocatore, prezzo)
    lista_giocatori.remove(nome_giocatore)

def aggiorna_crediti_rimanenti(squadra_vincente_giocatore: Squadra, prezzo:int):
    if(squadra_vincente_giocatore.crediti_totali > prezzo):
        squadra_vincente_giocatore.crediti_totali = squadra_vincente_giocatore.crediti_totali - prezzo
    else:
        return print("crediti insufficienti")

def stampa_tutte_squadre(self, fantacalcio: list):
    count = 0
    for squadra in fantacalcio:
        print (f"Digitare {count} per la squadra {squadra.nome_squadra}. Crediti rimanenti: {squadra.crediti_totali}")
        count = count + 1

def is_max_portieri(self, squadra: Squadra):
    if(len(squadra.squadra) > 2):
        print("Numero massimo di portieri raggiunto")
        return True
    else
        return False
