# Progetto Dimostrativo di Sicurezza con GitHub CodeQL e Checkov

Questo progetto è stato creato per dimostrare l'integrazione tra **GitHub CodeQL** (GitHub Code Scanning) e **Checkov** attraverso **GitHub Actions**, come descritto nell'[articolo di integrazione](https://www.google.com/url?sa=E&source=gmail&q=./INTEGRAZIONE_CODEQL_CHECKOV.md).

**ATTENZIONE: Questo progetto contiene VULNERABILITÀ INTENZIONALI a scopo didattico. NON UTILIZZARE in ambienti di produzione.**

## Descrizione del Progetto

Questo repository contiene un semplice progetto Python Flask vulnerabile, file di configurazione Dockerfile, Kubernetes e Terraform anch'essi volutamente insicuri. L'obiettivo è mostrare come utilizzare **GitHub CodeQL** e **Checkov** integrati in un workflow di **GitHub Actions** per:

  * **Identificare vulnerabilità** nel codice sorgente (con CodeQL).
  * **Rilevare configurazioni errate di sicurezza** in infrastruttura come codice (IaC) come Dockerfile, Kubernetes e Terraform (con Checkov).

Questo progetto è **puramente dimostrativo ed educativo**. Le vulnerabilità presenti sono state introdotte intenzionalmente per scopi didattici e non devono essere replicate in applicazioni reali. La sicurezza delle applicazioni e dell'infrastruttura è di fondamentale importanza in contesti di produzione.

## Vulnerabilità Intenzionali Presenti nel Progetto

Questo progetto include le seguenti vulnerabilità **a scopo didattico**:

  * **`app.py` (Python Flask Application):**
      * **SQL Injection (corretta in versioni successive):**  La versione iniziale dell'applicazione è vulnerabile a SQL Injection tramite string formatting. (Corretta nelle versioni successive per mostrare il rilevamento e la correzione).
      * **Memorizzazione Password in Chiaro (solo per scopo dimostrativo, poi rimossa):**  In versioni intermedie, la tabella `utenti` memorizza le password sia in chiaro (insicuro) che in hash (sicuro) per evidenziare i rischi della memorizzazione non sicura. (Poi corretta per memorizzare solo hash).
  * **`Dockerfile`:**
      * **Esecuzione come utente root (corretta in versioni successive):**  La versione iniziale del Dockerfile esegue il container come utente root all'interno del container. (Corretta in versioni successive per usare un utente non-root).
  * **`kubernetes/deployment.yaml`:**
      * **Container in modalità privilegiata (`privileged: true`) (corretta in versioni successive):** La versione iniziale del file Kubernetes imposta il container in modalità privilegiata. (Corretta in versioni successive).
      * **Mancanza di limiti di risorse (CPU e Memoria) (vulnerabilità persistente in alcune versioni per dimostrazione Checkov):** Alcune versioni del file Kubernetes volutamente non definiscono limiti di risorse per mostrare come Checkov può rilevare questa configurazione errata.
  * **`terraform/main.tf`:**
      * **Bucket S3 con ACL pubblico di lettura (`acl = "public-read"`) (corretta in versioni successive):** La versione iniziale del file Terraform crea un bucket S3 con ACL pubblico in lettura. (Corretta in versioni successive).
      * **Mancanza di crittografia lato server predefinita nel bucket S3 (vulnerabilità persistente in alcune versioni per dimostrazione Checkov):** Alcune versioni del file Terraform volutamente non configurano la crittografia lato server predefinita per mostrare come Checkov può rilevare questa configurazione errata.

## Scansione di Sicurezza Automatizzata con GitHub Actions

Il repository include un workflow di GitHub Actions (`.github/workflows/security-scan.yml`) che automatizza le seguenti scansioni di sicurezza ad ogni `push` o `pull request` sul branch `main`:

1.  **CodeQL Scan:** Analisi statica del codice Python con GitHub CodeQL per identificare vulnerabilità di sicurezza e problemi di qualità del codice.
2.  **Checkov Scan:** Analisi statica dei file di infrastruttura come codice (Dockerfile, Kubernetes, Terraform) con Checkov per rilevare configurazioni errate e violazioni delle *best practices* di sicurezza.

**Per eseguire le scansioni di sicurezza:**

1.  **Abilita GitHub Actions (se non già abilitato):**  Verifica che GitHub Actions sia abilitato per il tuo repository GitHub. Solitamente è abilitato di default.
2.  **Effettua un `push` o apri una `pull request` sul branch `main`:**  Appena effettui un `push` di codice al branch `main` o apri una `pull request` verso `main`, il workflow `security-scan.yml` verrà eseguito automaticamente da GitHub Actions.
3.  **Visualizza i risultati di CodeQL:**
      * Vai alla sezione **"Security"** del tuo repository GitHub.
      * Clicca su **"Code scanning alerts"**.
      * Qui potrai vedere gli eventuali avvisi di sicurezza rilevati da CodeQL nel codice Python. [Image of CodeQL Security Alert for SQL Injection] *(Sostituisci questo con uno screenshot reale se disponibile)*
4.  **Visualizza i risultati di Checkov:**
      * Vai alla sezione **"Actions"** del tuo repository GitHub.
      * Trova l'esecuzione del workflow **"Security Scan"**.
      * Clicca sul nome del job **"security-checks"**.
      * Scorri l'output del job per trovare la sezione **"Checkov scan results"**. Qui potrai vedere i risultati della scansione Checkov sui file Dockerfile, Kubernetes e Terraform, incluse le violazioni di policy identificate. [Image of Checkov Scan Results in GitHub Actions Output] *(Sostituisci questo con uno screenshot reale se disponibile)*

## Getting Started - Esecuzione dell'Applicazione Python (Solo per Test Locale)

**ATTENZIONE:**  Eseguire l'applicazione localmente è **solo per scopi di test e dimostrativi**. NON esporre questa applicazione vulnerabile su reti pubbliche o internet.

**Prerequisiti:**

  * **Python 3.9+ Installato:**  Assicurati di avere Python 3.9 o superiore installato sul tuo sistema.

  * **Pip Installato:**  Assicurati di avere `pip`, il gestore di pacchetti di Python, installato.

  * **Dipendenze Python:** Installa le dipendenze necessarie elencate nel file `requirements.txt`:

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

L'[articolo di integrazione](https://www.google.com/url?sa=E&source=gmail&q=./INTEGRAZIONE_CODEQL_CHECKOV.md) descrive in dettaglio come correggere le vulnerabilità presenti in questo progetto e come le scansioni di CodeQL e Checkov, dopo le correzioni, non dovrebbero più segnalare gli stessi problemi.

## Disclaimer Importante

**Questo progetto è a scopo puramente DIDATTICO.** Contiene **VULNERABILITÀ INTENZIONALI** e **NON DEVE ESSERE UTILIZZATO IN AMBIENTI DI PRODUZIONE.**

La sicurezza delle applicazioni e dell'infrastruttura è un aspetto critico. In applicazioni reali, è fondamentale seguire le *best practices* di sicurezza, eseguire test di sicurezza approfonditi e utilizzare strumenti di sicurezza automatizzati in modo continuo per ridurre i rischi e proteggere i dati e i sistemi.

## Licenza

[Inserisci qui la licenza del tuo progetto, ad esempio MIT License] (Opzionale)

