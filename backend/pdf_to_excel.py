import tabula
import pandas as pd
# note -- this isn't being used at the moment, as the logic is in app.py

def pdf_to_excel(pdf_file_path, excel_file_path):
    # Read PDF file
    tables = tabula.read_pdf(pdf_file_path, pages='all')
    if tables:
        print("Tables located, printing...")

        # Write each table to a separate sheet in the Excel file
        with pd.ExcelWriter(excel_file_path) as writer:
            for i, table in enumerate(tables):
                table.to_excel(writer, sheet_name=f'Sheet{i+1}')
    else:
        print("No tables found in your pdf")


# pdf_to_excel('annual-security-report.pdf', 'vscpolicy.xlsx')

# import tabula
# import pandas as pd
# import logging

# # Set up basic logging
# logging.basicConfig(level=logging.INFO)

# def pdf_to_excel(pdf_file_path, excel_file_path):
#     logging.info(f"Reading PDF file: {pdf_file_path}")
    
#     try:
#         tables = tabula.read_pdf(pdf_file_path, pages='all', multiple_tables=True, lattice=True)
        
#         if not tables or len(tables) == 0:
#             logging.info("No tables found with lattice mode, trying stream mode...")
#             tables = tabula.read_pdf(pdf_file_path, pages='all', multiple_tables=True, stream=True)

#         if tables and len(tables) > 0:
#             logging.info("Tables found, converting to Excel...")
#             with pd.ExcelWriter(excel_file_path) as writer:
#                 for i, table in enumerate(tables):
#                     table.to_excel(writer, sheet_name=f'Sheet{i+1}')
#         else:
#             logging.error("No tables found in your PDF.")
#             raise ValueError("No tables found in the provided PDF file.")
#     except Exception as e:
#         logging.error(f"Error during PDF processing: {e}")
#         raise



# pdf_to_excel('annual-security-report.pdf', 'vscpolicy.xlsx')

