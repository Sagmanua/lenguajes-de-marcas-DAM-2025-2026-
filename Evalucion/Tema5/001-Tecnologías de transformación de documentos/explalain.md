# Indroduccion brece y contexalizacion
En este ejercicio, tu objetivo es convertir y adaptar documentos de diferentes formatos para su intercambio de información.

Primero, es importante identificar los formatos de archivo con los que trabajarás. Algunos ejemplos son:

* PDF: Formato portátil de documentos.

* Word (docx): Documentos de Microsoft Word.

* Texto plano (txt): Archivos de texto simples.

* OpenOffice Document (odt): Documentos de OpenOffice o LibreOffice



# Desarrollo técnico correcto y preciso
## app.py
### import `fpdf`  `docx ` `pandas` `pypandoc` `oc`
```
from fpdf import FPDF
from docx import Document
import pandas as pd
import pypandoc
import os
```
### crear funcion que conventir DOCX a PDF
```
def convertir_docx_a_pdf(docx_path, pdf_path):
```

#### declara rutas de doc y pdf 
```
doc = Document(docx_path)
pdf = FPDF()
```
#### anadir primero pagina de pdf
```
    pdf.add_page()
``` 
#### set font de pdf y size de texto
```
    pdf.set_font("Arial", size=12)

```
#### uso bucle `for` que cada paragrahs gurda en formato pdf
```
for para in doc.paragraphs:
pdf.multi_cell(0, 10, para.text)
``` 
### y guarda pdf en la `pdf_patht`
```
pdf.output(pdf_path)
```
Siguiendo tu estilo de explicación paso a paso, aquí tienes el desglose de tu función para convertir archivos de texto plano (TXT) a PDF:

### Crear función que convierte TXT a PDF
``` 

def convertir_txt_a_pdf(txt_path, pdf_path):
```
### Inicializar el objeto PDF y añadir página Se crea la instancia de FPDF y se prepara la primera hoja en blanco.

``` 
pdf = FPDF()
pdf.add_page()
``` 
### Configurar la fuente y el tamaño Se define el tipo de letra (Arial) y el tamaño (12 puntos) que tendrá el texto dentro del PDF.

``` 
pdf.set_font("Arial", size=12)
``` 
###  Abrir el archivo TXT y leer línea por línea Se abre el archivo de texto con codificación utf-8 para asegurar que se lean correctamente tildes y caracteres especiales.

``` 
with open(txt_path, "r", encoding="utf-8") as f:
        for line in f:
```
### Escribir cada línea en el PDF El método multi_cell permite que el texto cambie de línea automáticamente si es muy largo.

```
pdf.multi_cell(0, 10, line)
```
### Guardar el archivo final Se genera y guarda el documento en la ruta especificada en pdf_path.

``` 
pdf.output(pdf_path)
```





### crear funcion que convertir excel
``` 
def convertir_excel(origen, destino):
```
leer el archivo de excel (origen)
``` 
df = pd.read_excel(origen)
```
### guardar el archivo en la ruta de destino (sin el indice)
``` 
df.to_excel(destino, index=False)
```

### Crear función para convertir ODT a DOCX
``` 
def convertir_odt_a_docx(odt_path, docx_path):
```
### Llamar al motor de conversión de Pandoc Se utiliza pypandoc como puente para transformar el formato del documento sin perder la estructura.

``` 
pypandoc.convert_text(
    "", to="docx", format="odt",
```
### Definir la ruta de salida El parámetro outputfile indica dónde se creará el nuevo archivo .docx.

```
outputfile=docx_path,
```
### Configurar argumentos adicionales El argumento --standalone asegura que el archivo resultante sea un documento completo con todos sus metadatos y encabezados, no solo un fragmento.

``` 
extra_args=["--standalone"],
```
### Especificar el archivo de origen Se indica la ruta del archivo original que se desea transformar.
``` 
source_file=odt_path )
```

# Codigo completa
```
from fpdf import FPDF
from docx import Document
import pandas as pd
import pypandoc
import os

# ------------------------------
# Convertir DOCX → PDF 
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

```

# 4.-Cierre/Conclusión enlazando con la unidad

Este ejemplo muestra un proceso básico de conversión, que puedes ampliar según el formato de origen y destino. La clave es investigar la biblioteca correcta para cada tipo de archivo y utilizarla según las necesidades del ejercicio.