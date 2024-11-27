# Gestore di Dipendenze

## Criteri di selezione
Per scegliere il gestore di dipendenze, abbiamo considerato i seguenti criteri:
1. **Compatibilità con lo standard del linguaggio:** Deve supportare il formato `pyproject.toml` o gestire dipendenze in modo conforme agli standard Python.
2. **Facilità di utilizzo:** Deve semplificare l’installazione e la gestione delle dipendenze.
3. **Manutenzione attiva:** Deve essere regolarmente aggiornato per evitare debiti tecnici.
4. **Funzionalità avanzate:** Deve offrire funzionalità extra come la gestione degli ambienti virtuali o il blocco delle versioni.

### 3. **`Pipenv`**
- **Descrizione:** Gestore di dipendenze che combina l'installazione delle dipendenze e la gestione degli ambienti virtuali.
- **Pro:**
  - Integra `virtualenv` per creare ambienti virtuali facilmente.
  - Utilizza **`Pipfile`** e **`Pipfile.lock`** per gestire le dipendenze in modo simile a `poetry.lock` di Poetry.
  - Compatibile con **`pyproject.toml`** per la configurazione, anche se non è la sua configurazione primaria.
- **Contro:** 
  - **Meno popolare di Poetry** e ha una manutenzione ridotta, con supporto parziale per `pyproject.toml`.

### 2. **`Poetry`**
- **Descrizione:** Gestore moderno che usa `pyproject.toml`.
- **Pro:** 
  - Compatibilità con gli standard Python.
  - Funzionalità avanzate come il blocco delle versioni.
- **Contro:** Richiede installazione iniziale.

### 3. **`PDM`**
- **Descrizione:** Uno strumento moderno, simile a Poetry, con maggiore flessibilità.
- **Pro:** 
  - Supporta `pyproject.toml` e PEP 582 (ambienti locali senza virtualenv).
  - Molto leggero.
- **Contro:** Ancora meno utilizzato rispetto a Poetry.

## Scelta del migliore
Abbiamo scelto **Poetry** per la gestione delle dipendenze, grazie alla sua compatibilità con `pyproject.toml`, facilità d’uso e manutenzione attiva.

## Istruzioni per l'uso
1. **Installazione di Poetry:**
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
