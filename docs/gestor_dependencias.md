# Gestore di Dipendenze

## Criteri di selezione
Per scegliere il gestore di dipendenze, abbiamo considerato i seguenti criteri:
1. **Compatibilità con lo standard del linguaggio:** Deve supportare il formato `pyproject.toml` o gestire dipendenze in modo conforme agli standard Python.
2. **Facilità di utilizzo:** Deve semplificare l’installazione e la gestione delle dipendenze.
3. **Manutenzione attiva:** Deve essere regolarmente aggiornato per evitare debiti tecnici.
4. **Funzionalità avanzate:** Deve offrire funzionalità extra come la gestione degli ambienti virtuali o il blocco delle versioni.

## Strumenti analizzati
### 1. **`pip`**
- **Descrizione:** Lo strumento predefinito per la gestione delle dipendenze in Python.
- **Pro:** Disponibile di default in Python.
- **Contro:** Non utilizza `pyproject.toml` e ha funzionalità limitate.

### 2. **`Pipenv`**
- **Descrizione:** Un gestore che combina dipendenze e ambienti virtuali.
- **Pro:** 
  - Integrazione diretta di virtualenv.
  - Genera file di blocco per le versioni.
- **Contro:** Manutenzione ridotta e non segue `pyproject.toml`.

### 3. **`Poetry`**
- **Descrizione:** Gestore moderno che usa `pyproject.toml`.
- **Pro:** 
  - Compatibilità con gli standard Python.
  - Funzionalità avanzate come il blocco delle versioni.
- **Contro:** Richiede installazione iniziale.

### 4. **`PDM`**
- **Descrizione:** Uno strumento moderno, simile a Poetry, con maggiore flessibilità.
- **Pro:** 
  - Supporta `pyproject.toml` e PEP 582 (ambienti locali senza virtualenv).
  - Molto leggero.
- **Contro:** Ancora meno utilizzato rispetto a Poetry.

### 5. **`Poethepoet`**
- **Descrizione:** Gestore combinato di dipendenze e tareas basato su `pyproject.toml`.
- **Pro:** 
  - Si integra perfettamente con `pyproject.toml`.
  - Consente di definire tareas personalizzate.
- **Contro:** È meno focalizzato sulla gestione delle dipendenze rispetto a Poetry.

## Scelta del migliore
Abbiamo scelto **Poetry** per la gestione delle dipendenze, grazie alla sua compatibilità con `pyproject.toml`, facilità d’uso e manutenzione attiva.

## Istruzioni per l'uso
1. **Installazione di Poetry:**
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
