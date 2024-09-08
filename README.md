# PDFParser
Vanderbilt Hustler internal tool to convert PDFs to spreadsheets!

This Python script uses the tabula library to read a PDF, build it into a dataframe, and export it as a csv. For pdfs with multiple tables, the script outputs each table as separate sheets.

# Usage
1. Add your PDF file to the repository. You can do this by dragging and dropping the file into the folder.

2. Add an empty Excel file to the repository. You can do this by right-clicking on the file explorer and selecting New File. Name the file with the .xlsx extension.

3. Run the Python script using the command
```bash
python pdf_to_excel.py
```
