# Loading an excel to pandas
# 
# Step 1.) importing libraries to be able to open excel file with Python
import pandas as pd
import numpy as np

# Step 2.) setting the location of excel file.
# important: it is generally useful to write it like this r"C:\Users\...."
# otherwise the system might not locate the file
# Also, we set the name of the sheet we wish to import
excel_file_location=r"/home/mate/Asztal/Python things/Blog materials/sales_report.xlsx"
sheet_name="Sales Report"

# Step 3.) opening the excel to a dataframe (e.g.Python table)
dataframe = pd.read_excel(excel_file_location, sheet_name)

# Step 4.) showing the loaded excel
dataframe
