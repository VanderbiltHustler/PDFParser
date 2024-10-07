from flask import Flask, request, jsonify, send_file
import tabula # for extracting pdfs
import pandas as pd # for manipulating tabular data
import os # for file paths
import logging

app = Flask(__name__)

# path for temporary file storage
TEMP_DIR = os.path.join(os.getcwd(), 'temp')

# if path doesn't exist, make it
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

# the function pdf to excel
def pdf_to_excel(pdf_file_path, excel_file_path):
    logging.info(f"Reading PDF file: {pdf_file_path}") 
    try:
        tables = tabula.read_pdf(pdf_file_path, pages='all', multiple_tables=True, lattice=True)
        
        if not tables or len(tables) == 0:
            logging.info("No tables found with lattice mode, trying stream mode...")
            tables = tabula.read_pdf(pdf_file_path, pages='all', multiple_tables=True, stream=True)

        if tables and len(tables) > 0:
            logging.info("Tables found, converting to Excel...")
            with pd.ExcelWriter(excel_file_path) as writer:
                for i, table in enumerate(tables):
                    table.to_excel(writer, sheet_name=f'Sheet{i+1}')
        else:
            logging.error("No tables found in your PDF.")
            raise ValueError("No tables found in the provided PDF file.")
    except Exception as e:
        logging.error(f"Error during PDF processing: {e}")
        raise

# route for uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files: # check if a file was provided in the POST request
        return jsonify({'error': 'No file part in request'}), 400

    file = request.files['file'] # get the file from the request
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # save to temp directory
    pdf_file_path = os.path.join(TEMP_DIR, file.filename)
    file.save(pdf_file_path)

    # output path
    excel_file_path = os.path.join(TEMP_DIR, f"{os.path.splitext(file.filename)[0]}.xlsx")

    # convert from pdf to excel
    pdf_to_excel(pdf_file_path, excel_file_path)

    # check if the excel file was created
    if not os.path.exists(excel_file_path):
        return jsonify({'error': 'Error creating Excel file'}), 500

    # send the excel file to client
    return send_file(excel_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False) 

