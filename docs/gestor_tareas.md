# Gestore di Tareas

## Criteri di selezione
Per scegliere il gestore di tareas, abbiamo considerato i seguenti criteri:
1. **Flessibilità:** Deve consentire la definizione di tareas personalizzate.
2. **Portabilità:** Deve funzionare su tutti i principali sistemi operativi (Windows, macOS, Linux).
3. **Semplicità:** Deve essere facile da configurare e utilizzare.
4. **Integrazione:** Deve funzionare bene con il gestore di dipendenze scelto.

## Strumenti analizzati
### 1. **`Make`**
- **Descrizione:** Strumento generico per la gestione di tareas.
- **Pro:** 
  - Ampia compatibilità.
  - Consente la definizione di tareas in un file `Makefile`.
- **Contro:** Richiede ambienti compatibili con `make` (es. installazione su Windows).

### 2. **`Invoke` (UV)**
- **Descrizione:** Task runner Python-specific che utilizza file Python per definire tareas.
- **Pro:** 
  - Semplice da configurare.
  - Consente script Python personalizzati.
- **Contro:** Meno portabile rispetto a `Make`.

### 3. **`Poethepoet`**
- **Descrizione:** Task runner basato su `pyproject.toml`.
- **Pro:** 
  - Integrazione diretta con `pyproject.toml`.
  - Definizione di tareas direttamente in un unico file di configurazione.
- **Contro:** Non ampiamente diffuso.

## Scelta del migliore
Abbiamo scelto **Make** per la gestione delle tareas, grazie alla sua flessibilità e ampia portabilità.
