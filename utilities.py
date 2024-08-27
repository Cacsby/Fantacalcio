from classes import Giocatore, Squadra, Portiere


def is_max_portieri(self, squadra: Squadra):
    if (len(squadra.portieri) > 2):
        print("Numero massimo di portieri raggiunto")
        return True
    else:
        return False


def crea_portiere_inserisci_in_squadra(self, nome_giocatore: str, prezzo: int, squadra_vincente_giocatore: Squadra,
                                        lista_giocatori: list):
    portieri = Portiere()
    portieri.portieri.append(Giocatore(nome_giocatore, prezzo))
    squadra_vincente_giocatore.portieri.append(portieri)

    aggiorna_crediti_rimanenti(squadra_vincente_giocatore, prezzo)
    lista_giocatori.remove(nome_giocatore)


def aggiorna_crediti_rimanenti(squadra_vincente_giocatore: Squadra, prezzo: int):
    if (squadra_vincente_giocatore.crediti_totali > prezzo):
        squadra_vincente_giocatore.crediti_totali = squadra_vincente_giocatore.crediti_totali - prezzo
    else:
        return print("crediti insufficienti")

def stampa_tutte_squadre(self, fantacalcio: list):
    count = 0
    print("_____________________________________")
    for squadra in fantacalcio:
        print(f"Digitare {count} per la squadra {squadra.nome_squadra}. Crediti rimanenti: {squadra.crediti_totali}. Portieri: {len(squadra.portieri)}. Difensori: {len(squadra.difensori)}. Centrocampisti: {len(squadra.centrocampisti)}. Attaccanti: {len(squadra.attaccanti)}")
        count = count + 1
    print("_____________________________________")