''' Test 3 - 817 - https://chat.openai.com/share/d8e1b2a0-8413-4635-83e3-8ef3f7b65432'''

import pandas as pd
import os
import openpyxl

# Change to the directory containing your excel files
os.chdir('/path/to/excel/files')

# Create an empty DataFrame to hold all the data
dataframe = pd.DataFrame()

# Loop over every file in the directory
for file in os.listdir():
    # Check if the file is an excel file
    if file.endswith('.xlsx') or file.endswith('.xls'):
        # Load the workbook
        workbook = openpyxl.load_workbook(file)

        # Check each sheet
        for sheet in workbook.sheetnames:
            # If the sheet name contains 'dashboard' (case-insensitive)
            if 'dashboard' in sheet.lower():
                # Load the data into a DataFrame
                df = pd.read_excel(file, sheet_name=sheet)

                # Check if 'C7:C37' are in the DataFrame
                if all(elem in df.columns.tolist() for elem in ['C7', 'C37']):
                    # Add the data to the final DataFrame
                    dataframe[file] = df.loc['C7':'C37']

# Write the final DataFrame to a new excel file
dataframe.to_excel('new_dashboard_data.xlsx')
