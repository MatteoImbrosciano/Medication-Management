import pytest
from medication_management.inventario import Inventario
from medication_management.medicamento import Medicamento
from pathlib import Path

@pytest.fixture
def inventario_vuoto():
    return Inventario()

@pytest.fixture
def inventario_con_medicamentos():
    inventario = Inventario()
    inventario.agregar_medicamento(Medicamento(nombre="Paracetamolo", cantidad="50 mg", precio=0.50, unitad=2))
    inventario.agregar_medicamento(Medicamento(nombre="Ibuprofeno", cantidad="30 mg", precio=0.30, unitad=1))
    return inventario

def test_inventario_iniziale_vuoto(inventario_vuoto):
    assert inventario_vuoto.medicamentos == []

def test_agregar_medicamento(inventario_vuoto):
    medicamento = Medicamento(nombre="Paracetamolo", cantidad="50 mg", precio=0.50, unitad=2)
    inventario_vuoto.agregar_medicamento(medicamento)
    assert len(inventario_vuoto.medicamentos) == 1
    assert inventario_vuoto.medicamentos[0] == medicamento

def test_visualizzare_inventario(inventario_con_medicamentos):
    inventario_visualizzato = inventario_con_medicamentos.visualizar_inventario()
    contenuto_atteso = "Paracetamolo: Cantidad=50 mg, Precio=0.5€, Unitad=2\nIbuprofeno: Cantidad=30 mg, Precio=0.3€, Unitad=1"
    assert inventario_visualizzato == contenuto_atteso

def test_agregar_medicamento_tipo_errato(inventario_vuoto):
    with pytest.raises(TypeError, match="Solo se pueden agregar instancias de Medicamento"):
        inventario_vuoto.agregar_medicamento("No es un Medicamento")

def test_leggi_file_esistente(tmp_path):

    # Percorso reale del file
    percorso_file = Path("C:/Users/matte/OneDrive/Desktop/Medication-Management/docs/pharmacy_receipt_1.txt")
    contenuto_atteso = (
        "Pharmacy Receipt - Farmacia Italia  \n"
        "Cliente: Matteo Imbrosciano  \n"
        "Data: 15 Febbraio 2024\n\n"
        "Articolo              | Quantità (mg/ml) | Unità | Importo (Euro)\n"
        "----------------------------------------------------------------\n"
        "Sintrom               | 1 mg            |   1   |    €7.50\n"
        "Elidel                | 10 mg/g         |   1   |   €12.30\n"
        "Protopic              | 0.3 mg          |   1   |    €9.80\n"
        "Decloban              | 500 mic         |   1   |    €7.10\n"
        "Dolquine              | 200 mg          |   1   |   €10.60\n"
        "Hemovas               | 400 mg          |   1   |    €8.40\n\n"
        "----------------------------------------------------------------\n"
        "Totale: €55.70"
    )
    percorso_file.write_text(contenuto_atteso, encoding='utf-8')

    # Leggere il contenuto del file
    contenuto = percorso_file.read_text(encoding='utf-8')
    assert contenuto == contenuto_atteso, "Il contenuto del file letto non corrisponde a quello atteso."

def test_leggi_file_non_esistente(tmp_path):
    percorso_file = tmp_path / "file_inesistente.txt"
    with pytest.raises(FileNotFoundError):
        percorso_file.read_text(encoding='utf-8')

def test_leggi_file_vuoto(tmp_path):
    percorso_file = tmp_path / "empty_file.txt"
    percorso_file.write_text("", encoding='utf-8')
    contenuto = percorso_file.read_text(encoding='utf-8')
    assert contenuto == "", "Il file dovrebbe essere vuoto."

def test_leggi_file_permessi_negati(tmp_path, monkeypatch):
    percorso_file = tmp_path / "restricted_file.txt"
    percorso_file.write_text("Contenuto", encoding='utf-8')

    # Simula PermissionError
    def mock_read_text(*args, **kwargs):
        raise PermissionError("Permiso denegado")

    monkeypatch.setattr(Path, "read_text", mock_read_text)
    
    with pytest.raises(PermissionError, match="Permiso denegado"):
        percorso_file.read_text(encoding='utf-8')
