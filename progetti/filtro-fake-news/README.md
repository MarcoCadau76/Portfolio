# Filtro Fake News (NLP)

Progetto Python di Natural Language Processing per rilevare fake news con tecniche di classificazione testuale, pensato come motore per un plug-in Chrome che segnala in tempo reale l'affidabilità delle notizie lette dall'utente.

## Obiettivo

Sviluppare un modello di Machine Learning in grado di distinguere notizie vere da fake news a partire dal testo, con l'obiettivo di integrarlo in un'estensione browser che fornisca un'indicazione di veridicità in tempo reale.

## Struttura del progetto

1. **Importazione delle librerie** — Pandas, spaCy, NLTK, scikit-learn
2. **Creazione funzioni** — pulizia del testo (lowercase, rimozione punteggiatura, stopwords, lemmatizzazione), vettorizzazione TF-IDF, analisi delle parole più frequenti
3. **Caricamento, analisi esplorativa e preprocessing del testo** — unione dataset fake/true news, pulizia e normalizzazione
4. **Train/Test Split e vettorizzazione** — suddivisione del dataset e trasformazione TF-IDF
5. **Addestramento dei modelli e valutazione delle performance** — confronto tra Logistic Regression, Linear SVC, Naive Bayes, MLP Classifier
6. **Test su nuove notizie** — verifica del modello su notizie non presenti nel training set
7. **Conclusioni**

## Tecnologie

Python, Pandas, spaCy, NLTK, scikit-learn (`TfidfVectorizer`, `LogisticRegression`, `LinearSVC`, `MultinomialNB`, `MLPClassifier`), pickle (per l'esportazione del modello)

## Dataset

Due dataset separati (Fake.csv e True.csv) con titoli e testi di notizie, rispettivamente false e vere, per un totale di oltre 44.000 articoli.

## Note

Il modello è stato esportato in formato `pickle` per un utilizzo successivo (integrazione plug-in), tecnica approfondita autonomamente oltre il programma del corso.

## File

- [notebook.ipynb](./notebook.ipynb) — notebook completo con codice, preprocessing NLP e valutazione modelli
