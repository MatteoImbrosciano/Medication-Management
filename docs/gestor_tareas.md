## Motivazioni della Scelta

Per l'automazione delle attività nel progetto, abbiamo scelto di utilizzare i **task integrati di Poetry** combinati con un file YAML per definire e organizzare i task principali. La scelta è basata sui seguenti criteri:

1. **Compatibilità con il Gestore di Dipendenze:**
   - Poetry offre supporto nativo per task comuni come installazione delle dipendenze e esecuzione di test, riducendo la necessità di strumenti aggiuntivi.

2. **Automazione semplice:**
   - YAML è leggibile e facilmente modificabile, permettendo di definire attività come il controllo della sintassi e l'esecuzione dei test in modo chiaro.

3. **Leggibilità e manutenibilità:**
   - La struttura YAML è più leggibile rispetto a configurazioni più complesse, come quelle necessarie con strumenti come **UV** o **Makefile**.

4. **Debito tecnico ridotto:**
   - Utilizzando un unico strumento per la gestione delle dipendenze e delle attività, semplifichiamo il flusso di lavoro del progetto, riducendo il rischio di configurazioni incoerenti.

---

## Confronto con altri Task Runner

| **Strumento**        | **Pro**                                                                                     | **Contro**                                                                                  |
|-----------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Poetry Tasks**      | - Integrato con il gestore di dipendenze<br>- Semplice da configurare                       | - Meno flessibile rispetto a strumenti dedicati                                             |
| **Poe**              | - Supporto avanzato per task complessi<br>- Integrazione nativa con `pyproject.toml`        | - Documentazione limitata rispetto a Poetry                                                |
| **Poethepoet**        | - Ottimo per automazione complessa<br>- Integrazione nativa con YAML                        | - Complesso da configurare per progetti semplici                                           |
| **Makefile**          | - Standard de facto per task automation<br>- Supporto universale                           | - Richiede una configurazione più manuale                                                  |
| **UV**                | - Minimalista e flessibile<br>- Ottimo per piccoli progetti                                | - Richiede configurazioni manuali per task e dipendenze                                     |

---

## Conclusione

La scelta di utilizzare Poetry Tasks e YAML è una decisione strategica che bilancia semplicità, efficienza e conformità agli standard moderni, garantendo che il progetto sia ben strutturato, facile da mantenere e pronto per future integrazioni.
