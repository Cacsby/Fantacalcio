import pandas as pd
from src.portieri import execute_portieri
from src.difensori import execute_difensori
from src.centrocampisti import execute_centrocampisti
from src.attaccanti import execute_attaccanti

from src.classes import Squadra


class FantacalcioApp:
    def __init__(self, file_path):

        self.file_path = file_path

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

        response = execute_portieri(self, self.file_path, fantacalcio)
        response = execute_difensori(self, self.file_path, fantacalcio)
        response = execute_centrocampisti(self, self.file_path, fantacalcio)
        response = execute_attaccanti(self, self.file_path, fantacalcio)


        dfs = []
        for item in response[0]:
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
        dfinvenduti = pd.DataFrame(response[1])
        dfs.append(dfinvenduti)

        # Concatena tutti i DataFrame in uno solo
        combined_df = pd.concat(dfs, axis=1)

        # Scrivi il DataFrame combinato in un unico foglio Excel
        combined_df.to_excel("recap_squadre.xlsx", index=False)


        # Stampa il contenuto del file
        print(dfs)


def main():
    # Specifica il percorso del file .xlsx
    # file_path = 'C:\\Users\\user\\Desktop\\Quotazioni_Fantacalcio_Stagione_2024_25.xlsx'
    file_path = input("Inserisci il percorso del file: ")

    # Crea un'istanza della classe e avvia il processo
    app = FantacalcioApp(file_path)
    app.fantacalcio()


if __name__ == "__main__":
    main()









