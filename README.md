


# PDFParser
Status: [In-Progress] <br>
Published: [date here] <br>
Updated: [9/22] <br>
### Vanderbilt Hustler internal tool to convert PDFs to spreadsheets!

## How this tool works
This Python script uses the tabula library to read a PDF, build it into a dataframe, and export it as a csv. For pdfs with multiple tables, the script outputs each table as separate sheets. 

## How to use this tool
1. Add your PDF file to the repository. You can do this by dragging and dropping the file into the folder.

2. Add an empty Excel file to the repository. You can do this by right-clicking on the file explorer and selecting New File. Name the file with the .xlsx extension.

3. Run the Python script using the command

```bash
python pdf_to_excel.py
```

## Directory 
install tree (mac example shown)
```bash
brew install tree
```
use tree command in terminal to generate
```bash
tree -I 'node_modules|.git' --dirsfirst | pbcopy
```
 
## Deployment History
- 9/12: Deploy PDF Script

## Credits
- Front-end Design | [Name], [Name]
- Back-end Design | [Name], [Name]

Thank you to [credit any inspiration, open source code, or advisors] for [X].

## Powered by The Vanderbilt Hustler Data Team
For questions, comments or curiosities: 
- Hustler staff: Slack the #data team. 
- The rest of the 🌎: [email](mailto:katherine.oung@vanderbilt.edu) Data Editor Katherine Oung

