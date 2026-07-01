# Analisi dei disastri aerei dal 1919 al 2023

Progetto Python di analisi esplorativa (EDA) su un dataset storico di incidenti aerei, con l'obiettivo di individuare trend, pattern e i velivoli più pericolosi.

## Obiettivo

- Analizzare l'andamento dei disastri aerei nel tempo, valutando l'impatto dell'attentato dell'11/09/2001
- Identificare le nazioni con il maggior numero di incidenti e vittime
- Valutare la sicurezza delle compagnie aeree, distinguendo quelle con meno incidenti
- Evidenziare le compagnie con il maggior numero di incidenti e vittime
- Individuare i velivoli che hanno causato più vittime, sia in totale sia in media per incidente
- Analizzare in quali giorni della settimana si sono verificati più incidenti e più vittime

## Struttura del progetto

**Step 1 — Creazione, analisi e pulizia del dataframe**
- Importazione dati da CSV con Pandas
- Verifica di valori mancanti, duplicati e uniformità dei dati
- Pulizia e trasformazione dei dati

**Step 2 — Insight e visualizzazioni**
- Top 10 nazioni per numero di incidenti e per numero di vittime (bar chart)
- Compagnie aeree più sicure (bar chart)
- Andamento degli incidenti per anno dal 1919 al 2023, con evidenza del trend post 11/09/2001 (line chart)
- Velivoli con il maggior numero di vittime, totali e in media per incidente (bar chart)
- Apparecchi più sicuri in base agli incidenti causati (bar chart)
- Analisi degli incidenti per giorno della settimana (bar chart)

## Tecnologie

Python, Pandas, Matplotlib (Pyplot)

## Dataset

CSV con lo storico degli incidenti aerei dal 1919 al 2023 (data, tipo velivolo, operatore, vittime, località, nazione, anno).

## File

- [notebook.ipynb](./notebook.ipynb) — notebook completo con codice, grafici e analisi
