# Strumenti di Test

## Criteri di Decisione

Per scegliere gli strumenti di test per il nostro progetto, abbiamo considerato i seguenti criteri:

1. **Facilità d'uso e manutenzione**: Lo strumento deve essere intuitivo da configurare e utilizzare, con una curva di apprendimento ridotta.
2. **Evitazione del debito tecnico**: Deve supportare buone pratiche di sviluppo e non introdurre complessità inutili.
3. **Raccomandazioni della comunità**: La popolarità e il supporto da parte della comunità sono stati valutati tramite [Snyk Advisor](https://snyk.io/advisor).

---

## Strumenti Analizzati

Abbiamo preso in considerazione diversi strumenti di test disponibili per Python, ognuno con vantaggi e svantaggi, come mostrato di seguito.

### **1. Pytest**
- **Descrizione**: Pytest è un framework versatile che combina funzionalità di libreria per asserzioni e test runner.
- **Valutazione su Snyk Advisor**: [Pytest](https://snyk.io/advisor/python/pytest) - 96.
- **Pro**:
  - Supporta fixture per la preparazione dei test.
  - Parametrizzazione avanzata per ridurre la duplicazione di codice.
  - Ampio supporto dalla community e ottima documentazione.
  - Integrazione con strumenti di copertura del codice (pytest-cov).
- **Contro**:
  - Può richiedere più configurazioni iniziali per progetti complessi.

#### **Adattamento degli Assert in Pytest**
Gli assert in Pytest verificano che una determinata condizione sia vera. Se la condizione risulta falsa, Pytest fornisce un messaggio di errore chiaro e leggibile, utile per diagnosticare rapidamente i problemi.

Nel nostro progetto, utilizziamo gli assert per:
1. **Verificare le funzionalità principali** delle classi e dei metodi, come il calcolo corretto delle quantità o dei prezzi.
2. **Validare errori e eccezioni**: Ad esempio, controlliamo che vengano generate eccezioni appropriate quando un valore non è valido.
3. **Collegare i test alle storie utente**: Ogni funzionalità testata corrisponde a un requisito del cliente o a una storia utente.

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

1. **Facilità d'uso**: Pytest semplifica l'esecuzione di test e la gestione degli errori, riducendo al minimo la complessità.
2. **Flessibilità**: Offre supporto avanzato per fixture, parametrizzazione e test delle eccezioni.
3. **Comunità e Valutazione**: Pytest è ampiamente supportato e raccomandato, con un'alta valutazione su Snyk Advisor.

---

## Conclusione

La scelta di **Pytest** come framework e test runner principale è stata fatta tenendo conto delle esigenze del progetto, dei requisiti di test e dei criteri di valutazione sopra descritti. La combinazione di facilità d'uso, ampia documentazione e integrazione nativa lo rende lo strumento ideale per garantire la qualità del codice.
