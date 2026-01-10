from fpdf import FPDF
from docx import Document
import pandas as pd
import pypandoc
import os

# ------------------------------
# Convertir DOCX → PDF (texto plano)
# ------------------------------
def convertir_docx_a_pdf(docx_path, pdf_path):
    doc = Document(docx_path)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, para.text)

    pdf.output(pdf_path)


# ------------------------------
# Convertir TXT → PDF
# ------------------------------
def convertir_txt_a_pdf(txt_path, pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(txt_path, "r", encoding="utf-8") as f:
        for line in f:
            pdf.multi_cell(0, 10, line)

    pdf.output(pdf_path)


# ------------------------------
# Convertir ODT → DOCX
# (usando pypandoc)
# ------------------------------
def convertir_odt_a_docx(odt_path, docx_path):
    pypandoc.convert_text(
        "", to="docx", format="odt",
        outputfile=docx_path,
        extra_args=["--standalone"],
        source_file=odt_path  # para versiones recientes de pypandoc
    )


# ------------------------------
# Convertir XLSX ↔ ODS
# (mediante pandas)
# ------------------------------
def convertir_excel(origen, destino):
    df = pd.read_excel(origen)
    df.to_excel(destino, index=False)


# ------------------------------
# Ejemplo de uso
# ------------------------------
if __name__ == "__main__":
    convertir_docx_a_pdf("archivo.docx", "salida.pdf")
    convertir_txt_a_pdf("notas.txt", "notas.pdf")
    convertir_odt_a_docx("documento.odt", "documento.docx")
    convertir_excel("datos.xlsx", "datos.ods")
