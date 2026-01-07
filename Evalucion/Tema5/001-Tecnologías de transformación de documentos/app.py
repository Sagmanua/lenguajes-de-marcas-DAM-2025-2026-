from fpdf import FPDF

def convertir_docx_a_pdf(docx, pdf):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    # código para leer el archivo y extraer el contenido...
    pdf.output(pdf)

# llamada al método
convertir_docx_a_pdf('archivo.docx', 'salida.pdf')