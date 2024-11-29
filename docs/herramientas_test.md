# Strumenti di Test

## Criteri di Decisione

Per scegliere gli strumenti di test per il nostro progetto, abbiamo considerato i seguenti criteri:

1. **Compatibilità**: Lo strumento deve essere pienamente compatibile con il linguaggio di programmazione scelto (Python).
2. **Valutazione**: La qualità e la popolarità dello strumento sono state analizzate tramite la piattaforma [Snyk Advisor](https://snyk.io/advisor).
3. **Flessibilità**: Deve offrire sia una libreria per le asserzioni, sia funzionalità di test runner e supporto per test automatizzati, permettendo di coprire in modo efficace le storie utente.

---

## Strumenti Analizzati

Abbiamo preso in considerazione diversi strumenti di test disponibili per Python, ognuno con vantaggi e svantaggi, come mostrato di seguito.

### **1. Pytest**
- **Descrizione**: Pytest è un framework versatile che combina funzionalità di libreria per asserzioni e test runner.
- **Valutazione su Snyk Advisor**: [Pytest](https://snyk.io/advisor/python/pytest) - 96.
- **Pro**:
  - Facile da configurare e usare.
  - Supporta fixture per la preparazione dei test.
  - Parametrizzazione avanzata per ridurre la duplicazione di codice.
  - Ampio supporto dalla community e ottima documentazione.
  - Integrazione con strumenti di copertura del codice (pytest-cov).
- **Contro**:
  - Può richiedere più configurazioni iniziali per progetti complessi.

---

### **2. Pytest-BDD**
- **Descrizione**: Estensione di Pytest per implementare test basati sul comportamento (Behavior-Driven Development).
- **Valutazione su Snyk Advisor**: [Pytest-BDD](https://snyk.io/advisor/python/pytest-bdd) - 78.
- **Pro**:
  - Permette di scrivere scenari di test in linguaggio naturale (Gherkin).
  - Utilizza Pytest come base, quindi supporta fixture e altre funzionalità avanzate.
- **Contro**:
  - Non necessario per progetti senza requisiti complessi basati su scenari.
  - Può introdurre overhead e complicazioni se non si utilizza BDD come metodologia principale.

---

### **3. Behave**
- **Descrizione**: Framework standalone per Behavior-Driven Development in Python.
- **Valutazione su Snyk Advisor**: [Behave](https://snyk.io/advisor/python/behave) - 65.
- **Pro**:
  - Consente di scrivere test in formato Gherkin, utile per team che collaborano con non sviluppatori.
  - Integrazione con strumenti CI/CD.
- **Contro**:
  - Complesso da configurare rispetto a Pytest.
  - Maggiore curva di apprendimento per team non esperti di BDD.
  - Dipende da librerie aggiuntive per funzionalità che Pytest ha nativamente.

---

### **4. Unittest**
- **Descrizione**: Parte della libreria standard di Python, offre strumenti per scrivere test unitari.
- **Valutazione su Snyk Advisor**: [Unittest](https://snyk.io/advisor/python/unittest).
- **Pro**:
  - Inclusa nella libreria standard, quindi non richiede installazione.
  - Facile da usare per test di base.
  - Ampio supporto per test strutturati (suite di test).
- **Contro**:
  - Meno flessibile rispetto a Pytest.
  - Non supporta nativamente funzionalità avanzate come fixture o parametrizzazione.
  - Maggiore verbosità rispetto a Pytest.

---

## Scelta degli Strumenti di Test

Per il nostro progetto, abbiamo scelto **Pytest** come strumento principale di testing. La scelta è motivata dai seguenti fattori:

1. **Compatibilità**: Pytest è perfettamente integrato con Python e offre tutto il necessario per scrivere e gestire test unitari, coprendo i requisiti del progetto.
2. **Valutazione**: Pytest ha una valutazione eccellente su Snyk Advisor (96), il che garantisce affidabilità e sicurezza.
3. **Flessibilità**: Con Pytest possiamo facilmente implementare test unitari e funzionali, sfruttando funzionalità come fixture e parametrizzazione senza necessità di linguaggi aggiuntivi (es. Gherkin).

---

## Confronto con Pytest-BDD, Behave e Unittest

- **Pytest-BDD** e **Behave** sono strumenti validi per progetti che richiedono scenari complessi o un approccio BDD, ma non sono la scelta migliore per il nostro progetto, perché:
  - **Semplicità del progetto**: Il nostro progetto non richiede scenari complessi o linguaggio naturale per descrivere i test.
  - **Focus sui test unitari**: Pytest è sufficiente per coprire tutte le storie utente e verificare la logica di business del sistema.
  - **Overhead evitabile**: L'adozione di strumenti BDD introdurrebbe un overhead inutile e maggiore complessità nella configurazione.

- **Unittest**, pur essendo incluso nella libreria standard, non offre la flessibilità e le funzionalità avanzate di Pytest, risultando meno adatto per un progetto con esigenze di test più evolute.

---

## Conclusione

La scelta di **Pytest** come framework e test runner principale è stata fatta tenendo conto delle esigenze del progetto, dei requisiti di test e dei criteri di valutazione sopra descritti. La combinazione di facilità d'uso, ampia documentazione e integrazione nativa lo rende lo strumento ideale per garantire la qualità del codice.
