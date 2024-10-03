import PyPDF2
import re

#Valido para version 3.0 en adelante
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        num_pages = len(reader.pages)        
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

pdf_path = "D:/Python/file.pdf"
text = extract_text_from_pdf(pdf_path)

_listaDnis = re.findall(r"DNI (\d{8}[A-Z])",text)
print(len(_listaDnis))
if _listaDnis:
    for dni in _listaDnis:
        print("DNI:", dni)