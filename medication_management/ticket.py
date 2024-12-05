from datetime import date

class Ticket:
    
    def __init__(self):
        self.medicamentos = []
        self.fecha = date.today()

    def aggiungi_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def genera_txt(self, nome_cliente, nome_file_txt):

        try:
            # Apri o crea il file di testo
            with open(nome_file_txt, "w", encoding="utf-8") as file:
                # Titolo e intestazione
                file.write("Pharmacy Receipt - Farmacia Italia\n")
                file.write(f"Cliente: {nome_cliente}\n")
                file.write(f"Data: {self.fecha.strftime('%d %B %Y')}\n\n")
                file.write("Articolo | Quantità | Unità | Importo (Euro):\n")

                # Dati sui farmaci
                totale = 0
                for medicamento in self.medicamentos:
                    prezzo_totale = medicamento.cantidad * medicamento.precio
                    totale += prezzo_totale
                    file.write(f"- {medicamento.nombre} | {medicamento.cantidad} | {medicamento.unidad} | €{prezzo_totale:.2f}\n")

                # Totale
                file.write(f"\nTotale: €{totale:.2f}\n")
                file.write("Grazie per il suo acquisto!\n")

            print(f"Ricevuta salvata in {nome_file_txt}")
        except Exception as e:
            print(f"Errore durante la creazione del file di testo: {e}")