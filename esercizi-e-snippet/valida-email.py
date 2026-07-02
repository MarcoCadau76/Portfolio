def valida_email(email):
    # Divide l'indirizzo in nome utente e dominio, separati da "@"
    parti = email.split("@")

    # Un'email valida ha esattamente una "@"
    if not len(parti) == 2:
        return False

    nome, dominio_completo = parti

    # Il nome utente non può essere vuoto
    if not nome:
        return False

    # Il nome può contenere ".", "_", "-" oltre a lettere/numeri:
    # li rimuoviamo temporaneamente per verificare che il resto sia alfanumerico
    if not nome.replace(".", "").replace("_", "").replace("-", "").isalnum():
        return False

    nome = list(nome)

    # Il primo carattere del nome deve essere una lettera
    if not nome[0].isalpha():
        return False

    # Divide il dominio in nome dominio ed estensione, separati da "."
    dominio_completo = dominio_completo.split(".")

    # Deve esserci esattamente un punto (es. "gmail.com")
    if not len(dominio_completo) == 2:
        return False

    dominio, ext = dominio_completo

    # Il dominio deve essere alfanumerico (no simboli)
    if not dominio.isalnum():
        return False

    dominio = list(dominio)

    # Il dominio deve iniziare con una lettera e non finire con un numero
    if not dominio[0].isalpha() or dominio[-1].isdigit():
        return False

    # L'estensione deve avere tra 1 e 3 lettere (es. "it", "com")
    if len(ext) < 1 or len(ext) > 3 or not ext.isalpha():
        return False

    return True


def filtra_email(lista_email):
    # Filtra la lista tenendo solo le email valide, poi le ordina alfabeticamente
    mail_filtrate = list(filter(valida_email, lista_email))
    mail_filtrate.sort()
    return mail_filtrate
