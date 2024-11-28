# Gestore di Dipendenze

## Criteri di Selezione
Per scegliere il gestore di dipendenze per il nostro progetto, abbiamo considerato i seguenti criteri:

1. **Supporto**: Il gestore di dipendenze deve essere compatibile con il runtime scelto (in questo caso Python) e supportare gli standard moderni come `pyproject.toml`.
2. **Semplicità**: Deve essere facile da usare, con comandi intuitivi e una configurazione minima.
3. **Comunità**: Deve avere una community attiva, in grado di fornire supporto in caso di problemi.

---

## Gestori di Dipendenze
Esistono diversi gestori di dipendenze per Python. Tra i principali, abbiamo considerato **Poetry**, **PDM** e **Hatch**.

### 1. **Poetry**
- **Descrizione**: Poetry è un gestore moderno che utilizza `pyproject.toml` come file di configurazione principale.
- **Pro**:
  - Compatibile con gli standard Python, inclusa la PEP 518.
  - Blocca le versioni delle dipendenze tramite un file `poetry.lock`.
  - Ampia community e aggiornamenti regolari.
- **Contro**:
  - Richiede l’installazione iniziale, ma è ben documentata.
- **Snyk - Analisi delle Vulnerabilità**: [Snyk su Poetry](https://snyk.io/advisor/python/poetry)

---

### 2. **PDM**
- **Descrizione**: PDM è uno strumento minimalista per la gestione delle dipendenze, che utilizza anche `pyproject.toml`.
- **Pro**:
  - Leggero e rapido.
  - Supporta la PEP 582, permettendo l’uso senza ambienti virtuali.
- **Contro**:
  - Meno popolare rispetto a Poetry, con una community più piccola.
- **Snyk - Analisi delle Vulnerabilità**: [Snyk su PDM](https://snyk.io/advisor/python/pdm)

---

### 3. **Hatch**
- **Descrizione**: Hatch è un gestore di dipendenze con un focus sulla gestione degli ambienti virtuali e configurazioni avanzate.
- **Pro**:
  - Supporto per configurazioni multi-ambiente, ideale per progetti complessi.
  - Integrazione con strumenti di sviluppo, come la gestione di versioni multiple.
- **Contro**:
  - Community più piccola rispetto a Poetry.
  - Può risultare complesso per progetti semplici.
- **Snyk - Analisi delle Vulnerabilità**: [Snyk su Hatch](https://snyk.io/advisor/python/hatch)

---

## Scelta del Gestore di Dipendenze
Per il nostro progetto, abbiamo scelto **Poetry** come gestore di dipendenze. Questo perché:
1. È compatibile con `pyproject.toml`, che è lo standard moderno per la configurazione di progetti Python.
2. Offre una gestione avanzata delle dipendenze con il blocco delle versioni.
3. Ha una community attiva e regolarmente aggiornata, facilitando il supporto e l'evoluzione del progetto.
