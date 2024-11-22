# Gestore di Tereas: 

## Criteri
1. **Compatibilità con il Gestore di Dipendenze:**
   - Il gestore di task deve integrarsi direttamente con il gestore di dipendenze scelto, evitando la necessità di strumenti aggiuntivi.
2. **Automazione delle Attività Comuni:**
   - Deve permettere di automatizzare task come installazione delle dipendenze, esecuzione di test e controllo della sintassi.
3. **Leggibilità e Manutenibilità:**
   - La configurazione deve essere chiara, leggibile e facilmente modificabile.
4. **Flessibilità:**
   - Deve consentire di aggiungere nuovi task o aggiornare quelli esistenti senza complicazioni.
5. **Debito Tecnico Ridotto:**
   - Lo strumento deve essere attivamente mantenuto e ben documentato per garantire stabilità e affidabilità nel tempo.

---

## Strumenti
| **Strumento**        | **Pro**                                                                                     | **Contro**                                                                                  |
|-----------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Poetry Tasks**      | - Integrato con il gestore di dipendenze<br>- Semplice da configurare                       | - Meno flessibile rispetto a strumenti dedicati                                             |
| **Poe**              | - Supporto avanzato per task complessi<br>- Integrazione nativa con `pyproject.toml`        | - Documentazione limitata rispetto a Poetry                                                |
| **Poethepoet**        | - Ottimo per automazione complessa<br>- Integrazione nativa con YAML                        | - Complesso da configurare per progetti semplici                                           |
| **Makefile**          | - Standard de facto per task automation<br>- Supporto universale                           | - Richiede una configurazione più manuale                                                  |
| **UV**                | - Minimalista e flessibile<br>- Ottimo per piccoli progetti                                | - Richiede configurazioni manuali per task e dipendenze                                     |

---

## Scelta
Abbiamo scelto di utilizzare **Poetry Tasks** combinato con un file YAML per i seguenti motivi:
1. **Compatibilità:** Si integra perfettamente con il gestore di dipendenze scelto (Poetry), evitando configurazioni aggiuntive.
2. **Automazione Semplice:** Supporta le attività essenziali (installazione, test, controllo della sintassi) senza richiedere strumenti esterni.
3. **Leggibilità:** La struttura YAML garantisce una configurazione chiara e facilmente manutenibile.
4. **Debito Tecnico Ridotto:** Poetry Tasks è parte di un ecosistema attivamente mantenuto e moderno, riducendo il rischio di obsolescenza.

---

## Conclusione

La scelta di utilizzare Poetry Tasks e YAML è una decisione strategica che bilancia semplicità, efficienza e conformità agli standard moderni, garantendo che il progetto sia ben strutturato, facile da mantenere e pronto per future integrazioni.
