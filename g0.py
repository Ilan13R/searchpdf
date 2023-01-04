import argparse
import os
import PyPDF2
from tqdm import tqdm

def search_pdfs(directory, search_word):
  # Validate input
  if not os.path.isdir(directory):
    raise ValueError("Invalid directory")
  if not search_word or not isinstance(search_word, str):
    raise ValueError("Invalid search word")
  
  # Initialize variables
  found = []
  total_files = len(os.listdir(directory))
  
  # Iterate through all files in the directory
  for i, file in enumerate(os.listdir(directory)):
    # Check if file is a PDF
    if not file.endswith(".pdf"):
      continue
      
    # Open the PDF file
    with open(os.path.join(directory, file), "rb") as f:
      pdf = PyPDF2.PdfReader(f)
      
      # Search for the word in the PDF
      for page in range(len(pdf.pages)):
        if search_word in pdf.pages[page].extract_text():
          found.append(file)
          break
          
    # Update the progress bar
    tqdm.write(f"{i+1}/{total_files} files processed")
  
  # Print the results
  print(f"{len(found)} PDFs found containing the word '{search_word}':")
  for file in found:
    print(file)

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("directory", help="Directory containing PDF files")
parser.add_argument("word", help="Word to search for")
args = parser.parse_args()

# Search the PDF files
search_pdfs(args.directory, args.word)
      
