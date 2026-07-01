# Analisi dei piloti Mondiale F1 2008

Progetto Python per l'analisi delle statistiche di piloti e costruttori del Mondiale di Formula 1 2008, a partire da un dataset CSV.

## Obiettivo

Elaborare i risultati di gara stagionali per calcolare classifiche piloti e costruttori secondo il regolamento punti 2008, e permettere la ricerca delle statistiche di un pilota specifico.

## Funzionalità

- **`conversione(posizione)`** — converte la posizione di arrivo in gara nel punteggio corrispondente al regolamento 2008 (1° = 10 punti, 2° = 8, ... fino all'8° posto)
- **`trova_pilota(lista_valori)`** — richiede in input il nome di un pilota e restituisce vittorie, podi e punti totali stagionali
- **`classifica_mondiale_piloti(lista_valori)`** — calcola e ordina la classifica piloti, esportata anche su file `.txt`
- **`classifica_mondiale_costruttori(lista_valori)`** — aggrega i punti dei piloti per team e restituisce la classifica costruttori ordinata

## Tecnologie

Python, modulo `csv`, dizionari e ordinamento con `sorted()`

## Dataset

File CSV con i risultati di gara della stagione 2008 (pilota, team, posizione per gara).

## Esempio di output

Il pilota Massa, ha totalizzato 97 punti, 6 vittorie e 10 podi totali.

Classifica piloti 2008:
Hamilton: 98
Massa: 97
Raikkonen: 75
...

Classifica costruttori 2008:
Ferrari: 172
McLaren: 151
BMW: 135
...

## Note
Progetto sviluppato come esame del Master Data Analyst (Profession.AI) — valutato e approvato dall'istruttore.

## File

- [notebook.ipynb](./notebook.ipynb) — notebook completo con codice ed esecuzione
