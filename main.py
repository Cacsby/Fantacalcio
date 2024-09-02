import pandas as pd
import random
from portieri import execute_portieri
from classes import Squadra, Portiere, Difensore, Centrocampista, Attaccante


def fantacalcio(self):


    team1 = Squadra("team1")
    team2 = Squadra("team2")
    team3 = Squadra("team3")
    team4 = Squadra("team4")
    team5 = Squadra("team5")
    team6 = Squadra("team6")
    team7 = Squadra("team7")
    team8 = Squadra("team8")
    team9 = Squadra("team9")
    team10 = Squadra("team10")


    fantacalcio = []
    fantacalcio.append(team1)
    fantacalcio.append(team2)
    fantacalcio.append(team3)
    fantacalcio.append(team4)
    fantacalcio.append(team5)
    fantacalcio.append(team6)
    fantacalcio.append(team7)
    fantacalcio.append(team8)
    fantacalcio.append(team9)
    fantacalcio.append(team10)


    # Specifica il percorso del file .xlsx
    file_path = 'C:\\Users\\user\\Desktop\\Quotazioni_Fantacalcio_Stagione_2024_25.xlsx'

    response = execute_portieri(self, file_path, fantacalcio)

    # df = pd.DataFrame(response)
    # df.to_excel("example.xlsx", index=False)

    # Lista per raccogliere tutti i DataFrame
    portiere1 = Portiere("Mimmo", 31)
    portier2 = Portiere("Mimmo", 31)
    portiere3 = Portiere("Mimmo", 31)

    difensore1 = Difensore("Massi", 31)
    difensore2 = Difensore("Massi", 31)
    difensore3 = Difensore("Massi", 31)

    centrocampista1 = Centrocampista("Dovbick", 31)
    centrocampista2 = Centrocampista("Dovbick", 31)
    centrocampista3 = Centrocampista("Dovbick", 31)

    attaccante1 = Attaccante("Ciccio", 31)
    attaccante2 = Attaccante("Ciccio", 31)
    attaccante3 = Attaccante("Ciccio", 31)


    for squadra in fantacalcio:
        squadra.portieri.append(portiere1)
        squadra.portieri.append(portier2)
        squadra.portieri.append(portiere3)

        squadra.centrocampisti.append(centrocampista1)
        squadra.centrocampisti.append(centrocampista2)
        squadra.centrocampisti.append(centrocampista3)

        squadra.difensori.append(difensore1)
        squadra.difensori.append(difensore2)
        squadra.difensori.append(difensore3)

        squadra.attaccanti.append(attaccante1)
        squadra.attaccanti.append(attaccante2)
        squadra.attaccanti.append(attaccante3)

    dfs = []
    for item in response:
        dfsi=[]
        all_players = []
        all_players.append({
            'Squadra': item.nome_squadra,
            'Crediti Rimanenti': item.crediti_totali
                             })

        for portiere in item.portieri:
            all_players.append({
                'Nome': portiere.nome_giocatore,
                'Prezzo': portiere.prezzo
            })# Converti la lista di dizionari in un DataFrame



        for difensore in item.difensori:
            all_players.append({
                'Nome': difensore.nome_giocatore,
                'Prezzo': difensore.prezzo
            })
            # Converti la lista di dizionari in un DataFrame



        for centrocampista in item.centrocampisti:
            all_players.append({
                'Nome': centrocampista.nome_giocatore,
                'Prezzo': centrocampista.prezzo
            })
            # Converti la lista di dizionari in un DataFrame



        for attaccante in item.attaccanti:
            all_players.append({
                'Nome': attaccante.nome_giocatore,
                'Prezzo': attaccante.prezzo
            })

        all_players.append({
            '': ""        })

        # Converti la lista di dizionari in un DataFrame
        dfa = pd.DataFrame(all_players)
        dfs.append(dfa)

    # Concatena tutti i DataFrame in uno solo
    combined_df = pd.concat(dfs, axis=1)

    # Scrivi il DataFrame combinato in un unico foglio Excel
    combined_df.to_excel("example_combined.xlsx", index=False)

    # Stampa il contenuto del file
    print(dfs)











