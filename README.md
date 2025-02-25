# Progetto dimostrativo di sicurezza con GitHub CodeQL e Checkov

Questo progetto è stato creato per dimostrare l'integrazione tra **GitHub CodeQL** (GitHub Code Scanning) e **Checkov** attraverso **GitHub Actions**, come descritto nell'[articolo di integrazione](https://www.google.com/url?sa=E&source=gmail&q=./INTEGRAZIONE_CODEQL_CHECKOV.md) **@TODO: Inserire link a TheRedCode.it**.

> **ATTENZIONE: Questo progetto contiene VULNERABILITÀ INTENZIONALI a scopo didattico. NON UTILIZZARE in ambienti di produzione.**

## Descrizione del Progetto

Questo repository contiene un semplice progetto Python Flask vulnerabile, file di configurazione Dockerfile, Kubernetes e Terraform anch'essi volutamente insicuri. L'obiettivo è mostrare come utilizzare **GitHub CodeQL** e **Checkov** integrati in un workflow di **GitHub Actions** per:

  * **Identificare vulnerabilità** nel codice sorgente (con CodeQL).
  * **Rilevare configurazioni errate di sicurezza** in infrastruttura come codice (IaC) come Dockerfile, Kubernetes e Terraform (con Checkov).

## Getting Started - Esecuzione dell'Applicazione Python (Solo per Test Locale)

> **ATTENZIONE:**  Eseguire l'applicazione localmente è **solo per scopi di test e dimostrativi**. NON esporre questa applicazione vulnerabile su reti pubbliche o internet.

**Prerequisiti:**

  * **Python 3.9+ Installato:** assicurati di avere Python 3.9 o superiore installato sul tuo sistema.

  * **Pip Installato:** assicurati di avere `pip`, il gestore di pacchetti di Python, installato.

  * **Dipendenze Python:** installa le dipendenze necessarie elencate nel file `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

    (Potrebbe essere necessario usare `pip3` invece di `pip` a seconda della tua configurazione Python.)

**Esecuzione dell'applicazione:**

1.  **Naviga alla directory del progetto** nel tuo terminale.

2.  **Esegui l'applicazione Python:**

    ```bash
    python app.py
    ```

    (o `python3 app.py`)

3.  **Accedi all'applicazione nel browser:** Apri il tuo browser web e vai all'indirizzo `http://127.0.0.1:5000`.

4.  **Esplora la rotta `/utente`:**  Puoi testare la rotta `/utente` (e le vulnerabilità SQL Injection nelle versioni iniziali) accedendo a URL come: `http://127.0.0.1:5000/utente?id=1`, `http://127.0.0.1:5000/utente?id=' OR '1'='1`, etc.

**Interruzione dell'applicazione:** Premi `Ctrl+C` nel terminale per fermare il server Flask.

## Correzione delle Vulnerabilità

L'[articolo di integrazione](https://www.google.com/url?sa=E&source=gmail&q=./INTEGRAZIONE_CODEQL_CHECKOV.md) **@TODO: Inserire link a TheRedCode.it. ** descrive in dettaglio come correggere le vulnerabilità presenti in questo progetto e come le scansioni di CodeQL e Checkov, dopo le correzioni, non dovrebbero più segnalare gli stessi problemi.

## Disclaimer Importante

**Questo progetto è a scopo puramente DIDATTICO.** Contiene **VULNERABILITÀ INTENZIONALI** e **NON DEVE ESSERE UTILIZZATO IN AMBIENTI DI PRODUZIONE.**

La sicurezza delle applicazioni e dell'infrastruttura è un aspetto critico. In applicazioni reali, è fondamentale seguire le *best practices* di sicurezza, eseguire test di sicurezza approfonditi e utilizzare strumenti di sicurezza automatizzati in modo continuo per ridurre i rischi e proteggere i dati e i sistemi.

## Licenza

MIT License (see [LICENSE.md](LICENSE.md)).

