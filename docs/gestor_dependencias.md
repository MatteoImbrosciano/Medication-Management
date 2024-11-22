# Gestore di Dipendenze: Poetry

## Motivazioni della Scelta

Abbiamo scelto **Poetry** come gestore di dipendenze per il nostro progetto basandoci sui seguenti criteri:

1. **Aderenza agli standard del linguaggio:**
   - Poetry utilizza il formato `pyproject.toml`, standardizzato dal PEP 518. Questo garantisce la compatibilità con le migliori pratiche moderne di Python.
   - Strumenti come **PDM** e **Poethepoet** supportano anch'essi questo formato, ma Poetry offre una gestione delle dipendenze più completa.

2. **Funzionalità principali:**
   - Risoluzione automatica delle dipendenze e gestione avanzata dei conflitti.
   - Isolamento degli ambienti virtuali specifici per ogni progetto.
   - Capacità di creare pacchetti Python pronti per la distribuzione.

3. **Debito tecnico ridotto:**
   - Poetry è attivamente mantenuto dalla comunità Python, riducendo il rischio di dover migrare a strumenti alternativi in futuro.
   - Strumenti come **Pipenv** non ricevono aggiornamenti frequenti, aumentando il rischio di obsolescenza.

4. **Facilità d'uso:**
   - Comandi semplici e una documentazione chiara rendono Poetry facile da adottare sia per sviluppatori esperti che per principianti.

---

## Confronto con altri strumenti

| **Strumento**       | **Pro**                                                                                     | **Contro**                                                                                  |
|----------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Poetry**           | - Supporto completo a `pyproject.toml`<br>- Gestione avanzata delle dipendenze<br>- Attivamente mantenuto | - Leggermente più lento rispetto a strumenti minimalisti come **PDM**                      |
| **PDM**              | - Leggero e veloce<br>- Integrazione perfetta con `pyproject.toml`                          | - Meno documentato rispetto a **Poetry**<br>- Funzionalità limitate                        |
| **Pipenv**           | - Interfaccia user-friendly<br>- Supporta nativamente `Pipfile`                            | - Non compatibile con `pyproject.toml` direttamente<br>- Aggiornamenti poco frequenti      |
| **Poethepoet**       | - Integrazione nativa con `pyproject.toml`<br>- Ottimo per automazione avanzata             | - Configurazione più complessa per progetti semplici                                       |

---

## Utilizzo di Poetry nel Progetto

### Conclusione

Poetry è stato scelto per la sua robustezza, compatibilità con gli standard e facilità d'uso. È lo strumento ideale per la gestione delle dipendenze nel nostro progetto, garantendo affidabilità e scalabilità a lungo termine.
