# =============================
# CLASSE STUDENTE
# =============================
class Studente:

    def __init__(self, nome, eta, voti):
        self.nome = nome
        self.eta = eta
        self.voti = voti  # dizionario materia:voto

    def media(self):
        """Calcola la media dei voti dello studente, arrotondata a 2 cifre"""
        return round(sum(self.voti.values()) / len(self.voti), 2)

    def __str__(self):
        """Ritorna una rappresentazione leggibile dello studente"""
        voti_str = ", ".join([f"{mat}: {voto}" for mat, voto in self.voti.items()])
        return f"Nome: {self.nome}, Età: {self.eta}, Voti: {voti_str}"

    def aggiungi_materia(self, nome_materia, voto):
        """
        Aggiunge o aggiorna una materia.
        Se la materia esiste, aggiorna il voto e stampa un messaggio.
        """
        if nome_materia in self.voti:
            print(f"La materia {nome_materia} è già presente. Aggiorno il voto.")
        self.voti[nome_materia] = voto


# =============================
# FUNZIONI PER IL REGISTRO
# =============================

def aggiungi_studente(registro):
    """Permette di aggiungere un nuovo studente al registro, con validazione del nome"""
    while True:
        nome_studente = input("Inserisci il nome dello studente: ")

        if nome_studente.lower() == "fine":
            return

        if not nome_studente:
            print("Devi inserire un nome valido.")
            continue

        if any(char.isdigit() for char in nome_studente):
            print("Il nome non può contenere numeri.")
            continue

        if nome_studente in registro:
            print("Esiste già uno studente con questo nome.")
            continue

        break

    # Input età con controllo
    while True:
        try:
            eta = int(input("Inserisci l'età dello studente: "))
            if eta > 0:
                break
            else:
                print("L'età deve essere positiva.")
        except ValueError:
            print("Devi inserire un numero intero.")

    # Numero di materie con controllo
    while True:
        try:
            n = int(input("Quante materie vuoi inserire: "))
            if n > 0:
                break
            else:
                print("Il numero deve essere maggiore di zero.")
        except ValueError:
            print("Devi inserire un numero valido.")

    # Inserimento materie e voti
    lista_materie = {}
    for _ in range(n):
        materia = input("Inserisci la materia: ")
        while True:
            try:
                voto = float(input("Inserisci il voto (0-10): "))
                if 0 <= voto <= 10:
                    break
                else:
                    print("Il voto deve essere tra 0 e 10.")
            except ValueError:
                print("Devi inserire un numero valido.")
        lista_materie[materia] = voto

    # Creazione oggetto Studente e inserimento nel registro
    studente = Studente(nome_studente, eta, lista_materie)
    registro[nome_studente] = studente
    print(f"Studente {nome_studente} aggiunto con successo!\n")


def visualizza_registro(registro):
    """Stampa tutti gli studenti del registro con la loro media"""
    if not registro:
        print("Nessuno studente presente.\n")
    else:
        print("\n--- Registro Studenti ---")
        for stud in registro.values():
            print(stud)
            print("Media:", stud.media())
            print("-" * 30)
        print()


def cerca_studente(registro):
    """Cerca uno studente per nome e stampa i suoi dati e la media"""
    nome_studente = input("Inserisci lo studente da cercare: ")
    if nome_studente in registro:
        stud = registro[nome_studente]
        print(stud)
        print("Media:", stud.media())
    else:
        print("Studente non presente.\n")


def aggiungi_materia_a_studente(registro):
    """Permette di aggiungere o aggiornare una materia a uno studente già presente"""
    nome = input("A quale studente vuoi aggiungere una materia? ")
    if nome not in registro:
        print("Studente non trovato.")
        return
    studente = registro[nome]

    materia = input("Inserisci la nuova materia: ")
    while True:
        try:
            voto = float(input("Voto per questa materia (0-10): "))
            if 0 <= voto <= 10:
                break
            else:
                print("Il voto deve essere tra 0 e 10.")
        except ValueError:
            print("Voto non valido.")

    # Usa il metodo della classe per aggiungere/aggiornare la materia
    studente.aggiungi_materia(materia, voto)
    print(f"Materia {materia} aggiunta/aggiornata a {nome}!\n")


def elimina_studente(registro):
    """Elimina uno studente dal registro, previa conferma"""
    nome_studente = input("Inserisci il nome dello studente da eliminare: ")
    if nome_studente in registro:
        conferma = input("Sei sicuro? si/no ").strip().lower()
        if conferma == "si":
            del registro[nome_studente]
            print(f"Studente {nome_studente} rimosso.\n")
        else:
            print("Operazione annullata.\n")
    else:
        print("Studente non presente.\n")


def media_piu_alta(registro):
    """Trova lo studente (o gli studenti, in caso di parità) con la media più alta"""
    if not registro:
        print("Nessuno studente nel registro.")
        return

    media_alta = max(stud.media() for stud in registro.values())
    nomi = [stud.nome for stud in registro.values() if stud.media() == media_alta]
    print(f"Studente/i con la media più alta ({media_alta}): {', '.join(nomi)}")


# =============================
# PROGRAMMA PRINCIPALE
# =============================
registro = {}  # registro vuoto iniziale

while True:
    print("1. Aggiungi studente")
    print("2. Visualizza registro")
    print("3. Cerca studente per nome")
    print("4. Aggiungi una materia ad uno studente")
    print("5. Rimuovi uno studente")
    print("6. Studente con media più alta")
    print("7. Esci")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        aggiungi_studente(registro)
    elif scelta == "2":
        visualizza_registro(registro)
    elif scelta == "3":
        cerca_studente(registro)
    elif scelta == "4":
        aggiungi_materia_a_studente(registro)
    elif scelta == "5":
        elimina_studente(registro)
    elif scelta == "6":
        media_piu_alta(registro)
    elif scelta == "7":
        print("Uscita dal programma.")
        break
    else:
        print("Scelta non valida, riprova.\n")
