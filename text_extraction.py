import os
from PyPDF2 import PdfReader


def extract_text(pdf_path):
  """
  Extracts text from a single PDF file.

  Args:
      pdf_path (str): Path to the PDF file.

  Returns:
      str: Extracted text from the PDF.
  """
  with open(pdf_path, 'rb') as pdf_file:
    reader = PdfReader(pdf_file)
    text = ""
    for page_num in range(len(reader.pages)):
      page = reader.pages[page_num]
      text += page.extract_text()
  return text.strip()

def extract_from_directory(directory):
  """
  Extracts text from all PDF files in a given directory.

  Args:
      directory (str): Path to the directory containing PDFs.
  """
  for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
      pdf_path = os.path.join(directory, filename)
      extracted_text = extract_text(pdf_path)
      print(f"Extracted from '{filename}':\n{extracted_text}\n")

if __name__ == "__main__":
  projection_dir = "my_pdf" 
  extract_from_directory(projection_dir)
