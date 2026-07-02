import pandas as pd
import numpy as np

data = {
    "dipendente": ["luca rossi", "SARA BIANCHI", "Marco Verdi", "ELENA NERI", "paolo russo", "Giulia Costa"],
    "reparto": ["IT", "HR", "IT", "Vendite", "HR", "Vendite"],
    "ore_lavorate": [160, 145, 172, None, 155, 138],
    "tariffa_ora": [25, 18, 30, 22, 20, None],
    "assenze": [2, 5, 0, 8, 3, 4],
    "certificati": [2, 3, 0, 4, 1, 6],
    "anzianita": [3, 8, 12, 1, 6, 9]
}

df = pd.DataFrame(data)

def conta_assenze(row):
    # assenze non coperte da certificato, minimo 0
    risultato = row["assenze"] - row["certificati"]
    return max(risultato, 0)

def bonus_anzianita(anni):
    # 500€ ogni 5 anni di anzianità
    if anni >= 5:
        moltiplicatore = anni // 5
        return 500 * moltiplicatore
    else:
        return 0

def stipendio_finale(row):
    # applica penali e bonus, poi tassazione (23% sopra 4000, altrimenti 20%)
    risultato_stipendio = row["stipendio_lordo"] - row["penale"] + row["bonus_anzianità"]
    if risultato_stipendio > 4000:
        stip_finale = risultato_stipendio - (risultato_stipendio * 0.23)
    else:
        stip_finale = risultato_stipendio - (risultato_stipendio * 0.2)
    return stip_finale

def livello(stipendio):
    if stipendio > 3500:
        return "Top"
    elif stipendio > 2500:
        return "Mid"
    else:
        return "Base"


# controllo valori mancanti
print(df.isnull().sum())

# normalizza i nomi (Title Case)
df["dipendente"] = df["dipendente"].apply(lambda x: x.title())

# riempie i NaN con mediana/media di reparto
media_ore = df.groupby("reparto")["ore_lavorate"].transform("median")
media_tariffe = df.groupby("reparto")["tariffa_ora"].transform("mean")
df["ore_lavorate"] = df["ore_lavorate"].fillna(media_ore)
df["tariffa_ora"] = df["tariffa_ora"].fillna(media_tariffe)

# calcolo stipendio lordo
df["stipendio_lordo"] = df["ore_lavorate"] * df["tariffa_ora"]

# assenze non giustificate e relativa penale
df["assenze_non_giustificate"] = df.apply(conta_assenze, axis=1)
df["penale"] = df["assenze_non_giustificate"] * 50

# bonus anzianità
df["bonus_anzianità"] = df["anzianita"].apply(bonus_anzianita)

# stipendio netto finale e fascia di livello
df["stipendio_finale"] = df.apply(stipendio_finale, axis=1)
df["livello"] = df["stipendio_finale"].apply(livello)

# riepilogo per reparto
print(df.groupby("reparto").agg({"stipendio_finale": "mean", "penale": "sum", "ore_lavorate": "mean"}).sort_values("stipendio_finale", ascending=False))

df
