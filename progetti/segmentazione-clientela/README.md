# Segmentazione della clientela — FinTech Solutions S.p.A.

Progetto Python di clustering per segmentare i clienti di un'azienda fittizia di servizi finanziari, a partire da un dataset di possessori di carte di credito, con l'obiettivo di identificare cluster utili a strategie di marketing mirate.

## Obiettivo

Sviluppare un modello di segmentazione della clientela basato sui pattern di utilizzo della carta di credito (saldo, acquisti, anticipi contanti, pagamenti), per individuare gruppi omogenei di clienti a cui indirizzare azioni di marketing specifiche.

## Struttura del progetto

1. **Caricamento e analisi esplorativa** — importazione dataset, controllo valori nulli, statistiche descrittive
2. **Definizione funzioni** — funzioni riutilizzabili per il preprocessing e la valutazione
3. **Preprocessing** — gestione valori mancanti, standardizzazione delle feature (StandardScaler)
4. **Scelta del numero di cluster** — metodo elbow e silhouette score per identificare il numero ottimale di cluster
5. **Allenamento modello e visualizzazione** — clustering con KMeans, riduzione dimensionale con PCA per la visualizzazione
6. **Interpretazione dei cluster e strategie di marketing** — analisi dei profili emersi e proposte operative

## Tecnologie

Python, Pandas, NumPy, scikit-learn (`KMeans`, `StandardScaler`, `PCA`, `silhouette_score`), Matplotlib

## Dataset

Dataset di 8.950 clienti possessori di carta di credito, con 18 variabili (saldo, frequenza acquisti, anticipi contanti, limite di credito, pagamenti, tenure, ecc.)

## Note

Progetto sviluppato come esame del Master Data Analyst (Profession.AI) — valutato e approvato dall'istruttore.

## File

- [notebook.ipynb](./notebook.ipynb) — notebook completo con codice, analisi e grafici
