
# PDF Search

A Python script that searches for a specific word in all PDF files in a directory.

## Requirements

- Python 3
- PyPDF2 library
- tqdm library

## Usage

python search.py directory search_word

Replace `directory` with the path to the directory containing the PDF files, and `search_word` with the word you want to search for.

## Example

python search.py /home/user/pdfs search_word

This will search for the word "search_word" in all PDF files in the "/home/user/pdfs" directory.

## Output

The program will display a progress bar while it is searching, and it will print the number of PDFs found containing the specified word, as well as a list of the file names.

2 PDFs found containing the word 'search_word':
file1.pdf
file2.pdf
