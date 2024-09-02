import random
import pandas as pd

from utilities import is_max_goalkeeper, print_all_team, \
    create_goalkeeper_and_insert_in_team, choose_team, choose_price


def execute_portieri(self, file_path, fantacalcio:list):
    # Se vuoi accedere a un foglio specifico, puoi farlo così:
    df = pd.read_excel(file_path, sheet_name='Portieri', usecols='D:E')
    # Seleziona una colonna specifica
    # colonna_specifica = df['Nome']
    lista_giocatori = df.values.tolist()
    squadra_vincente_giocatore = None
    prezzo_giocatore_estratto = None
    portieri_invenduti = []

    # remove se si toglie prima riga file
    lista_giocatori.remove(lista_giocatori[0])

    lista_giocatori = ["Cristiano Ronchi",
                       "Gianluigi Donnarumma"]

    while lista_giocatori:
        print(f"Numero di portieri rimanenti: {len(lista_giocatori)}")

        numero_random_lista_giocatori = random.randint(0, len(lista_giocatori)-1)

        giocatore_estratto = lista_giocatori[numero_random_lista_giocatori]

        esito = "yes"
        print(f"Giocatore estratto: {giocatore_estratto}")

        while esito == "yes":
            try:
                print_all_team(self, fantacalcio, portieri_invenduti)




                squadra_vincente_giocatore= choose_team(self, giocatore_estratto)
                prezzo_giocatore_estratto = choose_price(self, giocatore_estratto)

                if squadra_vincente_giocatore == 11:
                    portieri_invenduti.append(giocatore_estratto)
                    if giocatore_estratto  in lista_giocatori:
                        lista_giocatori.remove(giocatore_estratto)

                print(f"Devi modificare qualcosa?")

                esito = input("yes/no").lower()

            except ValueError:
                print("Inserire un valore numerico")

        # if squadra_vincente_giocatore == 0:
        #     create_goalkeeper_and_insert_in_team(self, giocatore_estratto, prezzo_giocatore_estratto, portieri_invenduti,
        #                                          lista_giocatori)

        if 0 <= squadra_vincente_giocatore < len(fantacalcio):
            squadra = fantacalcio[squadra_vincente_giocatore]
            if not is_max_goalkeeper(self, squadra):
                create_goalkeeper_and_insert_in_team(self, giocatore_estratto, prezzo_giocatore_estratto, squadra,
                                                     lista_giocatori)

        # if squadra_vincente_giocatore == 1:
        #     if is_max_goalkeeper(self, fantacalcio[1]) == False:
        #         create_goalkeeper_and_insert_in_team(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[1],
        #                                              lista_giocatori)
        # elif squadra_vincente_giocatore == 2:
        #     if is_max_goalkeeper(self, fantacalcio[2]) == False:
        #         create_goalkeeper_and_insert_in_team(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[2],
        #                                              lista_giocatori)
        # elif squadra_vincente_giocatore == 3:
        #     if is_max_goalkeeper(self, fantacalcio[3]) == False:
        #         create_goalkeeper_and_insert_in_team(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[3],
        #                                              lista_giocatori)
        # elif squadra_vincente_giocatore == 4:
        #     if is_max_goalkeeper(self, fantacalcio[4]) == False:
        #         create_goalkeeper_and_insert_in_team(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[4],
        #                                              lista_giocatori)
        # elif squadra_vincente_giocatore == 5:
        #     if is_max_goalkeeper(self, fantacalcio[5]) == False:
        #         create_goalkeeper_and_insert_in_team(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[5],
        #                                              lista_giocatori)
        # elif squadra_vincente_giocatore == 6:
        #     if is_max_goalkeeper(self, fantacalcio[6]) == False:
        #         create_goalkeeper_and_insert_in_team(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[6],
        #                                              lista_giocatori)
        # elif squadra_vincente_giocatore == 7:
        #     if is_max_goalkeeper(self, fantacalcio[7]) == False:
        #         create_goalkeeper_and_insert_in_team(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[7],
        #                                              lista_giocatori)
        # elif squadra_vincente_giocatore == 8:
        #     if is_max_goalkeeper(self, fantacalcio[8]) == False:
        #         create_goalkeeper_and_insert_in_team(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[8],
        #                                              lista_giocatori)
        # elif squadra_vincente_giocatore == 9:
        #     if is_max_goalkeeper(self, fantacalcio[9]) == False:
        #         create_goalkeeper_and_insert_in_team(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[9],
        #                                              lista_giocatori)
        # elif squadra_vincente_giocatore == 10:
        #     if is_max_goalkeeper(self, fantacalcio[10]) == False:
        #         create_goalkeeper_and_insert_in_team(self, giocatore_estratto, prezzo_giocatore_estratto, fantacalcio[10],
        #                                              lista_giocatori)

    return fantacalcio