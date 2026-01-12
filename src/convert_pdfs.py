import shutil
import os
import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\sgriswold\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


cwd = os.getcwd()
raw_pdf_path = os.path.join(cwd, "raw_pdfs")
scanned_pdf_path = os.path.join(cwd, "scanned_pdfs")
txt_pdf_path = os.path.join(cwd, "txt_pdfs")


def scrap_pdf_text(pdf_filename:str):
    """
    Docstring for scrap_pdf_text
    
    :param pdf_filename: Description
    :type pdf_filename: str
    :ret: extracted_text
    :r-type: str
    """
    pdf_key = os.path.join(raw_pdf_path, pdf_filename)
    pages = convert_from_path(pdf_key, 300, poppler_path="C:\\poppler-25.12.0\\Library\\bin")

    full_text = []
    for page in pages:
        txt = pytesseract.image_to_string(page)
        full_text.append(txt)

    return "\n\n".join(full_text)

def save_extracted_text(extracted_text:str, pdf_filename:str):
    p = pdf_filename
    txt_filename = p[:-4]+'.txt' if p[-4:]=='.pdf' else p + '.txt'
    txt_key = os.path.join(txt_pdf_path, txt_filename)
    with open(txt_key, 'w') as f:
        f.writelines(extracted_text)

def move_raw_pdf(pdf_filename:str):
    src_pdf_path = os.path.join(raw_pdf_path, pdf_filename)
    dest_pdf_path = os.path.join(scanned_pdf_path, pdf_filename)
    shutil.move(src_pdf_path, dest_pdf_path)

def main():
    """Get the file names from the raw pdf folder.  
    Convert the pdf to text and move the file to scanned folder.
    """

    pdf_files = os.listdir(raw_pdf_path)
    for pdf_filename in pdf_files:
        pdf_key = os.path.join(raw_pdf_path, pdf_filename)
        if os.path.exists(pdf_key):
            extracted_text = scrap_pdf_text(pdf_filename)
            save_extracted_text(extracted_text, pdf_filename)
            move_raw_pdf(pdf_filename)
        else:
            print(f"File {pdf_key} not found.")

# Example Usage:
if __name__ == "__main__":
    main()
    