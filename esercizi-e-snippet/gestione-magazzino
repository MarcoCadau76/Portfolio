# ===========================
# FUNZIONI GESTIONE MAGAZZINO
# ===========================

def aggiungi_prodotto(magazzino):
  while True:

    prodotto = input("Inserisci un prodotto: ").strip().lower()
    if prodotto.isalpha():

      try:
        if prodotto in magazzino:
          # Prodotto già presente: sommo la quantità inserita a quella esistente
          magazzino[prodotto] += int(input("inserisci la quantità del prodotto: "))
          print("Prodotto aggiunto")
          break
        else:
          # Nuovo prodotto: lo aggiungo al dizionario
          magazzino[prodotto] = int(input("Inserisci la quantità: "))
          break
      except ValueError:
        print("Devi inserire un numero valido.")
    else:
      print("Il nome del prodotto deve essere una stringa.")

def rimuovi_prodotto(magazzino):
  while True:

    prodotto = input("Inserisci il prodotto da cercare: ")

    if prodotto in magazzino:
      eliminare = input("Vuoi eliminare il prodotto? Si/elimina, No/mantieni").strip().lower()

      match eliminare:
        case "si":
          magazzino.pop(prodotto)
          print(f"Il prodotto {prodotto} è stato eliminato.")
          break
        case "no":
          print("Nessun prodotto eliminato")
          break
        case _:
          # Scelta non valida: si ricomincia il ciclo per richiedere conferma
          print("Scelta non valida")
          
    else:
      print("Nessun prodotto presente.")
      break



def cerca_prodotto(magazzino):

  while True:
    prodotto = input("Inserisci il nome del prodotto da cercare (digita fine er uscire):").strip().lower()
    if prodotto == "fine":
      return "Ricerca annullata"

    if prodotto in magazzino:

      return f"Per il prodotto: {prodotto}, sono presenti {magazzino[prodotto]} unità"
    else:
      print("Prodotto non presente.")


def visualizza_soglia(magazzino):

  while True:
    try:
      soglia = int(input("Inserisci la sooglia di prodotti: "))
      break
    except ValueError:
      print("Input non valido")
  trovati = False
  for prodotto, numero in magazzino.items():
    if numero < soglia:
      print(f"{prodotto}: {numero}")
      trovati = True
  if not trovati:
      print("Nessun prodotto sotto soglia")

# ===========================
# PROGRAMMA PRINCIPALE
# ===========================


magazzino = {}

while True:
  print("1. Aggiungi prodotto")
  print("2. Rimuovi prodotto")
  print("3. Cerca prodotto")
  print("4. Visualizza prodotti sotto soglia")
  print("5. Esci")

  scelta = input("Scegli un opzione: ")

  match scelta:
    case "1":
      aggiungi_prodotto(magazzino)
    case "2":
      rimuovi_prodotto(magazzino)
    case "3":
      print(cerca_prodotto(magazzino))
    case "4":
      visualizza_soglia(magazzino)
    case "5":
      print("Uscita dal programma.")
      break
    case _:
      print("Scelta non valida, riprova.")
