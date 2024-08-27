import random
import pandas as pd

from classes import Squadra
from utilities import is_max_portieri, stampa_tutte_squadre, \
    crea_portiere_inserisci_in_squadra


def execute_portieri(self, file_path, fantacalcio:list):
    # Se vuoi accedere a un foglio specifico, puoi farlo così:
    df = pd.read_excel(file_path, sheet_name='Portieri', usecols='D:E')
    # Seleziona una colonna specifica
    # colonna_specifica = df['Nome']
    lista_giocatori = df.values.tolist()

    # remove se si toglie prima riga file
    lista_giocatori.remove(lista_giocatori[0])

    while lista_giocatori:
        print(f"Numero di portieri rimanenti: {len(lista_giocatori)}")

        numero_random_lista_giocatori = random.randint(0, len(lista_giocatori))

        giocatore_estratto = lista_giocatori[numero_random_lista_giocatori]

        esito = "yes"
        print(f"Giocatore estratto: {giocatore_estratto}")

        while esito == "yes":
            try:
                stampa_tutte_squadre(self, fantacalcio)

                if giocatore_estratto not in lista_giocatori:
                    lista_giocatori.remove(giocatore_estratto)

                print(f"Quale squadra si è aggiudicato {giocatore_estratto}?")

                squadra_vincente_giocatore = int(input(""))

                print(f"Quanto è stato pagato: {giocatore_estratto}")

                prezzo_giocatore_estratto = int(input(""))

                print(f"Devi modificare qualcosa?")

                esito = input("yes/no")

            except ValueError:
                print("Inserire un valore numerico")

        # squadra_vincente_giocatore = "carico"

        if squadra_vincente_giocatore == 0:
            if is_max_portieri(self, fantacalcio[0]) == False:
                crea_portiere_inserisci_in_squadra(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[0],
                                                    lista_giocatori)

        elif squadra_vincente_giocatore == 1:
            if is_max_portieri(self, fantacalcio[0]) == False:
                crea_portiere_inserisci_in_squadra(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[1],
                                                    lista_giocatori)
        elif squadra_vincente_giocatore == 2:
            if is_max_portieri(self, fantacalcio[0]) == False:
                crea_portiere_inserisci_in_squadra(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[2],
                                                    lista_giocatori)
        elif squadra_vincente_giocatore == 3:
            if is_max_portieri(self, fantacalcio[0]) == False:
                crea_portiere_inserisci_in_squadra(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[3],
                                                    lista_giocatori)
        elif squadra_vincente_giocatore == 4:
            if is_max_portieri(self, fantacalcio[0]) == False:
                crea_portiere_inserisci_in_squadra(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[4],
                                                    lista_giocatori)
        elif squadra_vincente_giocatore == 5:
            if is_max_portieri(self, fantacalcio[0]) == False:
                crea_portiere_inserisci_in_squadra(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[5],
                                                    lista_giocatori)
        elif squadra_vincente_giocatore == 6:
            if is_max_portieri(self, fantacalcio[0]) == False:
                crea_portiere_inserisci_in_squadra(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[6],
                                                    lista_giocatori)
        elif squadra_vincente_giocatore == 7:
            if is_max_portieri(self, fantacalcio[0]) == False:
                crea_portiere_inserisci_in_squadra(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[7],
                                                    lista_giocatori)
        elif squadra_vincente_giocatore == 8:
            if is_max_portieri(self, fantacalcio[0]) == False:
                crea_portiere_inserisci_in_squadra(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[8],
                                                    lista_giocatori)
        elif squadra_vincente_giocatore == 9:
            if is_max_portieri(self, fantacalcio[9]) == False:
                crea_portiere_inserisci_in_squadra(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[9],
                                                    lista_giocatori)


    return fantacalcio