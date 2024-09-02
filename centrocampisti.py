import random
import pandas as pd

from utilities import is_max_goalkeeper, print_all_team, \
    create_goalkeeper_and_insert_in_team, choose_team, choose_price, create_midfielder_and_insert_in_team, \
    is_max_midfielder


def execute_centrocampisti(self, file_path, fantacalcio:list):
    # Se vuoi accedere a un foglio specifico, puoi farlo così:
    df = pd.read_excel(file_path, sheet_name='Centrocampisti', usecols='D:E')
    # Seleziona una colonna specifica
    # colonna_specifica = df['Nome']
    lista_giocatori = df.values.tolist()
    squadra_vincente_giocatore = None
    prezzo_giocatore_estratto = None
    centrocampisti_invenduti = []

    # remove se si toglie prima riga file
    lista_giocatori.remove(lista_giocatori[0])


    while lista_giocatori:
        print(f"Numero di centrocampisti rimanenti: {len(lista_giocatori)}")

        numero_random_lista_giocatori = random.randint(0, len(lista_giocatori)-1)

        giocatore_estratto = lista_giocatori[numero_random_lista_giocatori]

        esito = "yes"
        print(f"Giocatore estratto: {giocatore_estratto}")

        while esito == "yes":
            try:
                print_all_team(self, fantacalcio, centrocampisti_invenduti)




                squadra_vincente_giocatore= choose_team(self, giocatore_estratto)
                prezzo_giocatore_estratto = choose_price(self, giocatore_estratto)

                if squadra_vincente_giocatore == 11:
                    centrocampisti_invenduti.append(giocatore_estratto)
                    if giocatore_estratto  in lista_giocatori:
                        lista_giocatori.remove(giocatore_estratto)

                print(f"Devi modificare qualcosa?")

                esito = input("yes/no").lower()

            except ValueError:
                print("Inserire un valore numerico")



        if 0 <= squadra_vincente_giocatore < len(fantacalcio):
            squadra = fantacalcio[squadra_vincente_giocatore]
            if not is_max_midfielder(self, squadra):
                create_midfielder_and_insert_in_team(self, giocatore_estratto, prezzo_giocatore_estratto, squadra,
                                                     lista_giocatori)



    return fantacalcio, centrocampisti_invenduti