# Gestore di Dipendenze: Poetry

## Criteri
1. **Aderenza agli Standard del Linguaggio:**
   - Il gestore deve supportare il formato `pyproject.toml` (PEP 518) per garantire compatibilità e interoperabilità con altri strumenti.
2. **Funzionalità Principali:**
   - Risoluzione automatica dei conflitti, isolamento degli ambienti virtuali e gestione separata delle dipendenze di sviluppo e produzione.
3. **Facilità d'Uso e Documentazione:**
   - Deve avere comandi intuitivi e una documentazione chiara per facilitare l'apprendimento e l'adozione.
4. **Riduzione del Debito Tecnico:**
   - Deve essere attivamente sviluppato e mantenuto, per evitare problemi di obsolescenza.
5. **Adattabilità al Progetto:**
   - Deve adattarsi alle esigenze specifiche del progetto, considerando il numero di dipendenze e la complessità generale.

---

## Strumenti
| **Strumento**       | **Pro**                                                                                     | **Contro**                                                                                  |
|----------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Poetry**           | - Supporto completo a `pyproject.toml`<br>- Gestione avanzata delle dipendenze<br>- Attivamente mantenuto | - Leggermente più lento rispetto a strumenti minimalisti come **PDM**                      |
| **PDM**              | - Leggero e veloce<br>- Integrazione perfetta con `pyproject.toml`                          | - Meno documentato rispetto a **Poetry**<br>- Funzionalità limitate                        |
| **Pipenv**           | - Interfaccia user-friendly<br>- Supporta nativamente `Pipfile`                            | - Non compatibile con `pyproject.toml` direttamente<br>- Aggiornamenti poco frequenti      |
| **Poethepoet**       | - Integrazione nativa con `pyproject.toml`<br>- Ottimo per automazione avanzata             | - Configurazione più complessa per progetti semplici                                       |

---

## Scelta
Abbiamo scelto **Poetry** come gestore di dipendenze per i seguenti motivi:
1. **Standard Moderni:** Aderisce al formato `pyproject.toml` (PEP 518), garantendo compatibilità con altri strumenti.
2. **Gestione Completa:** Offre una gestione avanzata delle dipendenze, inclusi ambienti virtuali e risoluzione automatica dei conflitti.
3. **Facilità d'Uso:** Comandi semplici e una documentazione chiara lo rendono ideale sia per sviluppatori esperti che per principianti.
4. **Manutenzione Attiva:** È attivamente sviluppato e mantenuto dalla comunità Python.
5. **Supporto per Dipendenze Separate:** Permette di gestire separatamente dipendenze di sviluppo e produzione, essenziale per il nostro progetto.

---

## Conclusione
Poetry è stato scelto per la sua robustezza, compatibilità con gli standard moderni e facilità d'uso. È lo strumento ideale per la gestione delle dipendenze nel nostro progetto, garantendo affidabilità e scalabilità a lungo termine.
