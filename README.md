


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

## Things being worked through/considered
- Example PDFs
  - https://police.vanderbilt.edu/pdfs/Daily_Crime_Log.pdf
  - https://police.vanderbilt.edu/crimeinfo/annual-security-report.pdf
- React-Typescript, perhaps with Flask for the Python backend
  - [https://stackoverflow.com/questions/60528792/how-to-combine-javascript-react-frontend-and-python-backend](url)
- Will assign components; however, frontend is focus for now
```
/pdf-parser-tool
├── /backend
│   ├── app.py                   # python script
│   ├── requirements.txt         # dependencies for python (e.g. tabula-py, pandas, etc.)
│   └── ...                      # other backend files
├── /frontend
│   ├── /public                  # public assets (index.html, favicon, etc.)
│   ├── /src
│   │   ├── /components          # react components (e.g., UploadForm, TableView)
│   │   ├── /hooks               # custom hooks (for API calls, etc.)
│   │   ├── /styles              # CSS
│   │   ├── App.tsx              # main react component
│   │   ├── index.tsx            # entry point for react
│   │   └── api.ts               # API functions to interact w/ backend
│   ├── package.json             # dependencies for frontend (react, typescript, etc.)
│   └── tsconfig.json            # typescript config
└── README.md                    # project docs
```
- Doesn't need to store PDFs, but may need to turn Excel sheets into Google Sheets
  - Google Sheets API [https://developers.google.com/sheets/api/guides/concepts](url) 

## Possible Requirements
(Will be workshopped -- consider a requirements.txt)

- pip install tabula-py
- pip install JPype1
- Install Java 64-Bit @ [https://www.java.com/en/download/manual.jsp](url)
- Add it to your environment variabls
- Add it to your path (%JAVA_HOME%\bin)
- e.g. "(C:\Program Files (x86)\Java\jre1.8.0_421)"
- pip install openpyxl

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

