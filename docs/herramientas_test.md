## Criteri di Selezione
Per scegliere gli strumenti di test per il nostro progetto, abbiamo preso in considerazione i seguenti criteri:

1. **Facilità di uso e manutenzione**: Gli strumenti devono essere facili da configurare e utilizzare, con una documentazione chiara e attiva supporto della community.
2. **Evitazione del debito tecnico**: È essenziale che gli strumenti permettano di scrivere test di alta qualità, evitando la duplicazione del codice e facilitando l'integrazione continua.
3. **Raccomandazioni della comunità**: Gli strumenti scelti devono essere ampiamente adottati nella comunità Python e avere una buona reputazione per stabilità e prestazioni.

---

## 1. **Scelta del Test Runner**

Un **Test Runner** è uno strumento che esegue i test e fornisce i risultati. Abbiamo considerato diverse opzioni per il nostro progetto.

### Alternative:

#### 1.1 **Pytest**
**Pytest** è uno degli strumenti più utilizzati per il testing in Python. È semplice da configurare e usare, e offre molte funzionalità avanzate come fixture, asserzioni dettagliate e supporto per i test paralleli.

**Vantaggi**:
  - Facile da usare.
  - Grande supporto della comunità.
  - Supporto per test di unità, integrazione e accettazione.

**Svantaggi**:
  - Alcune funzionalità avanzate richiedono una comprensione profonda della libreria
  - Alcuni errori possono risultare difficili da diagnosticare per i principianti

- **Valutazione su Snyk Advisor**: [Pytest](https://snyk.io/advisor/python/pytest) 

#### 1.2 **Pytest-BDD**
**Pytest-BDD** è un'estensione di Pytest che aggiunge supporto per il Behavior-Driven Development (BDD). Si basa sulla sintassi di Gherkin per scrivere scenari di test.

**Vantaggi**:
  - Adatto per il BDD e la scrittura di scenari di test in linguaggio naturale.
  - Integra perfettamente Pytest, quindi mantiene la compatibilità con altri strumenti e funzionalità di Pytest.

**Svantaggi**:
  - Richiede una conoscenza del BDD e del linguaggio Gherkin
  - Non necessario per progetti che non seguono la metodologia BDD

- **Valutazione su Snyk Advisor**: [Pytest-BDD](https://snyk.io/advisor/python/pytest-bdd)

### 1.3. **Unittest**
**Unittest** è il modulo di testing predefinito in Python. Fornisce un framework di test basato su classi e metodi, che lo rende utile per progetti più strutturati.

- **Vantaggi**:
  - Integrato direttamente in Python, senza bisogno di installare librerie esterne
  - Basato sul paradigma di testing xUnit, facilmente comprensibile per chi ha esperienza con altri linguaggi

- **Svantaggi**:
  - Meno flessibile e più verboso rispetto a Pytest
  - Funzionalità più limitate e meno estendibile
    
**Valutazione su Snyk Advisor**: [Unittest](https://snyk.io/advisor/python/unittest).

### Scelta Finale:
Dopo aver valutato le alternative, la scelta è ricaduta su **Pytest**. Sebbene **Pytest-BDD** sia utile per scenari BDD, il nostro progetto si concentra maggiormente su test unitari e di integrazione, quindi **Pytest** offre la soluzione più completa e versatile.

## 2. **Scelta della Biblioteca di Asserzioni**

La **Biblioteca di Asserzioni** è un componente fondamentale per i test, poiché permette di verificare che i risultati ottenuti siano quelli attesi.

### Alternative:

#### 2.1 **Pytest**
**Pytest** ha già integrato un sistema di asserzioni che consente di esprimere facilmente le condizioni di test. È molto semplice da usare e consente di scrivere test chiari e leggibili.

- **Vantaggi**:
  - Facile da usare
  - Ottima integrazione con il Test Runner **Pytest**
  - Supporta una vasta gamma di casi di test

- **Svantaggi**:
  - Limitato rispetto a librerie come **Hypothesis** per il testing basato su proprietà

#### 2.2 **Hypothesis**
**Hypothesis** è una libreria di testing che consente di scrivere test basati su **strategie**. Genera automaticamente dati di test per le funzioni, verificando un numero maggiore di casi e migliorando la copertura del codice.

**Vantaggi**:
  - Genera automaticamente casi di test per una copertura migliore.
  - Utile per il testing del comportamento e per test che richiedono vari input.
  - Eccellente per il testing basato su proprietà.

**Svantaggi**:
  - Richiede tempo per imparare a generare i test corretti
  - Può risultare eccessivo per test più semplici

**Valutazione su Snyk Advisor**: [Hypothesis](https://snyk.io/advisor/python/hypothesis#readme)

### Scelta Finale:
La scelta finale per la **Biblioteca di Aserzioni** è **Pytest** integrato. Sebbene **Hypothesis** offra funzionalità potenti per il **property-based testing**, non è necessaria per il nostro progetto in quanto i test non richiedono la generazione automatica di casi complessi. L'asserzione integrata di **Pytest** è sufficiente per soddisfare le esigenze del nostro progetto.

## Conclusioni
La combinazione di **Pytest** come Test Runner e la sua libreria di asserzioni integrata è la scelta migliore per il nostro progetto. Essa offre un'ottima usabilità, una comunità attiva e una documentazione completa, che ci permetterà di scrivere test efficaci e facilmente manutenibili.
