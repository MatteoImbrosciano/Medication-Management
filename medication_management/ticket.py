from fpdf import FPDF
from datetime import date

class Ticket:
    
    def __init__(self):
        self.medicamentos = []
        self.fecha = date.today()

    def aggiungi_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def genera_pdf(self, nome_cliente, nome_file_pdf):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Titolo
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, txt="Pharmacy Receipt - Farmacia Italia", ln=True, align='C')
        pdf.ln(10)

        # Dettagli Cliente e Data
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Cliente: {nome_cliente}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Data: {self.fecha.strftime('%d %B %Y')}", ln=True, align='L')
        pdf.ln(10)

        # Tabella dei Farmaci
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(80, 10, txt="Articolo", border=1)
        pdf.cell(40, 10, txt="Quantità (mg/ml)", border=1)
        pdf.cell(40, 10, txt="Unità", border=1)
        pdf.cell(30, 10, txt="Importo (Euro)", border=1, ln=True)

        pdf.set_font("Arial", size=12)
        totale = 0
        for medicamento in self.medicamentos:
            prezzo_totale = medicamento.cantidad * medicamento.precio
            totale += prezzo_totale
            pdf.cell(80, 10, txt=medicamento.nombre, border=1)
            pdf.cell(40, 10, txt=str(medicamento.cantidad), border=1)
            pdf.cell(40, 10, txt=medicamento.unidad, border=1)
            pdf.cell(30, 10, txt=f"{prezzo_totale:.2f}", border=1, ln=True)

        # Totale
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Totale: {totale:.2f} Euro", ln=True, align='L')
        pdf.ln(10)
        pdf.cell(200, 10, txt="Grazie per il suo acquisto!", ln=True, align='C')

        # Salva il PDF
        pdf.output(nome_file_pdf)
        print(f"Ricevuta salvata come {nome_file_pdf}")
