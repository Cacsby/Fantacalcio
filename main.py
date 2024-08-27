import pandas as pd
import random
from portieri import execute_portieri
from classes import Squadra

def fantacalcio(self):
    team0 = Squadra("roma")
    team1 = Squadra("2")
    team2 = Squadra("2")
    team3 = Squadra("milan")
    team4 = Squadra("roma")
    team5 = Squadra("milan")
    team6 = Squadra("roma")
    team7 = Squadra("milan")
    team8 = Squadra("roma")
    team9 = Squadra("milan")

    fantacalcio = []
    fantacalcio.append(team0)
    fantacalcio.append(team1)
    fantacalcio.append(team2)
    fantacalcio.append(team3)
    fantacalcio.append(team4)
    fantacalcio.append(team5)
    fantacalcio.append(team6)
    fantacalcio.append(team7)
    fantacalcio.append(team8)
    fantacalcio.append(team9)


    # Specifica il percorso del file .xlsx
    file_path = 'C:\\Users\\user\\Desktop\\Quotazioni_Fantacalcio_Stagione_2024_25.xlsx'

    execute_portieri(self, file_path, fantacalcio)

    # Stampa il contenuto del file
    print(df)











