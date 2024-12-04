## Criteri di Selezione

Per scegliere gli strumenti di test per il nostro progetto, abbiamo preso in considerazione i seguenti criteri:

1. **Compatibilità Nativa**
2. **Salute del Progetto**
3. **Comunità e Supporto**
4. **Maturità del Progetto**

---

## Alternative Analizzate

### 1. **pytest**

#### Descrizione
`pytest` è uno dei framework di test più utilizzati nel mondo Python. È molto apprezzato per la sua semplicità e potenza. Supporta un'ampia gamma di funzionalità, come l'esecuzione di test, asserzioni avanzate e l'integrazione con strumenti di continuous integration.

#### Pro
- **Facilità di uso**: Ha una sintassi semplice e permette di scrivere test concisi.
- **Comunità e Supporto**: È uno degli strumenti più popolari nel mondo Python, con una vasta comunità e frequenti aggiornamenti.
- **Maturità**: È stato ampiamente adottato in progetti di qualsiasi dimensione.
- **Valutazione su Snyk Advisor**: [Pytest](https://snyk.io/advisor/python/pytest) - 96.
- **Funzionalità avanzate**: Supporta fixture, parametrize, e vari metodi di reportistica.

#### Contro
- **Configurazione**: In alcuni casi, può richiedere una configurazione aggiuntiva per ottimizzare l'esperienza di utilizzo.

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

## Scelta Finale

Dopo aver valutato le diverse alternative, la nostra scelta finale è stata quella di utilizzare **pytest**. Ecco i motivi principali:

1. **Compatibilità e Supporto**: `pytest` è ampiamente supportato e continuamente aggiornato, con una comunità molto attiva. Inoltre, è compatibile con gli altri strumenti del nostro stack tecnologico.
2. **Semplicità d'uso**: La sua facilità di configurazione e la possibilità di scrivere test semplici lo rendono ideale per il nostro progetto.
3. **Flessibilità e Funzionalità avanzate**: La capacità di gestire test complessi e la possibilità di estendere facilmente il framework sono aspetti fondamentali che ci hanno spinto a preferirlo rispetto ad altre alternative.

Infine, consideriamo che il supporto attivo e la documentazione di `pytest` garantiscono una soluzione stabile e sicura a lungo termine, riducendo il debito tecnico e migliorando la qualità del codice.

---

## Conclusione

La scelta di **Pytest** come framework e test runner principale è stata fatta tenendo conto delle esigenze del progetto, dei requisiti di test e dei criteri di valutazione sopra descritti. La combinazione di facilità d'uso, ampia documentazione e integrazione nativa lo rende lo strumento ideale per garantire la qualità del codice.
