# Gestore di Tareas

## Criteri di Selezione
Per scegliere il gestore di tareas per il nostro progetto, abbiamo considerato i seguenti criteri:

1. **Semplicità**: La soluzione deve essere facile da configurare e utilizzare, con comandi intuitivi e una curva di apprendimento ridotta.
2. **Rendimento**: Il gestore deve essere rapido ed efficiente nell'esecuzione delle tareas, anche in progetti di grandi dimensioni.
3. **Comunità**: Deve avere una community attiva per fornire supporto in caso di problemi.

---

## Strumenti Analizzati

### 1. **Make**
- **Descrizione**: Uno strumento generico per la gestione di tareas, ampiamente utilizzato in diversi ecosistemi di sviluppo.
- **Pro:**
  - Altamente performante e affidabile.
  - Definizione chiara delle tareas tramite un file `Makefile`.
- **Contro:**
  - Richiede l'installazione di `make` su sistemi Windows, riducendo la portabilità.
  - Non specifico per Python, il che lo rende meno intuitivo in questo contesto.
- **Documentazione Ufficiale:** [GNU Make Manual](https://www.gnu.org/software/make/manual/make.html)

---

### 2. **Invoke**
- **Descrizione**: Un task runner specifico per Python, che utilizza script Python per definire tareas personalizzate.
- **Pro:**
  - Semplice da configurare grazie all'uso di Python.
  - Flessibilità nella definizione di tareas complesse.
- **Contro:**
  - Dipende dal runtime Python, rendendolo meno portabile rispetto a strumenti generici.
- **Comunità:** La community di Invoke è più piccola rispetto ad altri strumenti come `Make`.
- **Documentazione Ufficiale:** [Invoke Documentation](https://www.pyinvoke.org/)

---

### 3. **Poethepoet**
- **Descrizione**: Un task runner moderno progettato per integrarsi con `pyproject.toml`, ideale per progetti Python.
- **Pro:**
  - Integrazione perfetta con il gestore di dipendenze **Poetry**.
  - Centralizzazione della configurazione delle tareas e delle dipendenze in un unico file.
  - Semplice da configurare e utilizzare.
- **Contro:**
  - Community più piccola rispetto a strumenti come `Make`.
- **Rendimento:** Ottimo per progetti Python-specific.
- **Snyk - Analisi delle Vulnerabilità:** [Snyk su Poethepoet](https://snyk.io/advisor/python/poethepoet)

---

### 4. **Taskipy**
- **Descrizione:** Un task runner minimalista che utilizza anche `pyproject.toml` per configurare le tareas.
- **Pro:**
  - Leggero e facile da configurare.
  - Supporto diretto per `pyproject.toml`.
- **Contro:**
  - Funzionalità limitate rispetto a strumenti come Poethepoet.
  - Documentazione meno approfondita.
- **Snyk - Analisi delle Vulnerabilità:** [Snyk su Taskipy](https://snyk.io/advisor/python/taskipy)

---

## Scelta del Gestore di Tareas
Per il nostro progetto, abbiamo scelto **Poethepoet** come gestore di tareas. La decisione si basa sui seguenti motivi:

1. **Semplicità**: Poethepoet è facile da configurare e integra le tareas direttamente in `pyproject.toml`.
2. **Rendimento**: È ottimizzato per progetti Python-specific, garantendo rapidità nell'esecuzione delle tareas.
3. **Comunità**: Sebbene più piccola rispetto a strumenti generici, offre documentazione chiara e supporto per progetti Python.
