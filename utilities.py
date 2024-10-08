from src.classes import Giocatore, Squadra


def is_max_goalkeeper(self, squadra: Squadra):
    if (len(squadra.portieri) > 2):
        print("Numero massimo di portieri raggiunto")
        return True
    else:
        return False

def is_max_defender(self, squadra: Squadra):
    if (len(squadra.difensori) > 7):
        print("Numero massimo di difensori raggiunto")
        return True
    else:
        return False

def is_max_midfielder(self, squadra: Squadra):
    if (len(squadra.centrocampisti) > 7):
        print("Numero massimo di centrocampisti raggiunto")
        return True
    else:
        return False
def is_max_striker(self, squadra: Squadra):
    if (len(squadra.attaccanti) > 5):
        print("Numero massimo di attaccanti raggiunto")
        return True
    else:
        return False


def create_goalkeeper_and_insert_in_team(self, nome_giocatore: str, prezzo: int, squadra_vincente_giocatore: Squadra,
                                         lista_giocatori: list, ):
    # portieri = Portiere()
    squadra_vincente_giocatore.portieri.append(Giocatore(nome_giocatore, prezzo))

    update_remaining_credits(squadra_vincente_giocatore, prezzo)
    lista_giocatori.remove(nome_giocatore)

def create_defender_and_insert_in_team(self, nome_giocatore: str, prezzo: int, squadra_vincente_giocatore: Squadra,
                                         lista_giocatori: list, ):
    # portieri = Portiere()
    squadra_vincente_giocatore.difensori.append(Giocatore(nome_giocatore, prezzo))

    update_remaining_credits(squadra_vincente_giocatore, prezzo)
    lista_giocatori.remove(nome_giocatore)

def create_midfielder_and_insert_in_team(self, nome_giocatore: str, prezzo: int, squadra_vincente_giocatore: Squadra,
                                         lista_giocatori: list, ):
    # portieri = Portiere()
    squadra_vincente_giocatore.centrocampisti.append(Giocatore(nome_giocatore, prezzo))

    update_remaining_credits(squadra_vincente_giocatore, prezzo)
    lista_giocatori.remove(nome_giocatore)

def create_striker_and_insert_in_team(self, nome_giocatore: str, prezzo: int, squadra_vincente_giocatore: Squadra,
                                         lista_giocatori: list, ):
    # portieri = Portiere()
    squadra_vincente_giocatore.attaccanti.append(Giocatore(nome_giocatore, prezzo))

    update_remaining_credits(squadra_vincente_giocatore, prezzo)
    lista_giocatori.remove(nome_giocatore)


def update_remaining_credits(squadra_vincente_giocatore: Squadra, prezzo: int):
    if (squadra_vincente_giocatore.crediti_totali > prezzo):
        squadra_vincente_giocatore.crediti_totali = squadra_vincente_giocatore.crediti_totali - prezzo
    else:
        return print("crediti insufficienti")

def print_all_team(self, fantacalcio: list, lista_giocatori_invenduti: list):
    count = 1
    print("_____________________________________")
    print(f"Digitare 0 se il giocatore non ha ricevuto offerte. Numero giocatori invenduti: {len(lista_giocatori_invenduti)}")
    print("_____________________________________")
    for squadra in fantacalcio:
        print(f"Digitare {count} per la squadra {squadra.nome_squadra}. Crediti rimanenti: {squadra.crediti_totali}. Portieri: {len(squadra.portieri)}. Difensori: {len(squadra.difensori)}. Centrocampisti: {len(squadra.centrocampisti)}. Attaccanti: {len(squadra.attaccanti)}")
        count = count + 1
    print("_____________________________________")

def choose_team(self, giocatore_estratto: Giocatore):
    while True:
        try:
            squadra_vincente_giocatore = int(input(f"Inserisci il numero della squadra che ha acquistato:{giocatore_estratto}"))
            # if squadra_vincente_giocatore == 0:
            #     return squadra_vincente_giocatore

            if 0 < squadra_vincente_giocatore < 11:
                return squadra_vincente_giocatore
            else:
                print("Il numero della squadra deve essere compreso tra 1 e 10.")
        except ValueError:
            print("Inserisci un valore numerico valido.")


def choose_price(self, giocatore_estratto: Giocatore):
    while True:
        try:
            return int(input(f"Quanto è stato pagato il giocatore: {giocatore_estratto}"))
        except ValueError:
            print("Inserisci un valore numerico valido.")