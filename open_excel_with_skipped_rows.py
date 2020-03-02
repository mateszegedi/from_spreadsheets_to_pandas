# Loading an excel to pandas, where
# only a section of a table has to be loaded 
# Step 1.) importing libraries to be able to open excel file with Python
import pandas as pd
import numpy as np

# Step 2.) setting the location of excel file.
# important: it is generally useful to write it like this r"C:\Users\...."
# otherwise the system might not locate the file
# Also, we set the name of the sheet we wish to import
excel_file_location=r"/home/mate/Asztal/Python things/Blog materials/sales_report.xlsx"
sheet_name="Sales Report skiprow"

#Opening excel from a specific row/column
#Additional parameters:
# "usecols": pandas reads only data within these columns. You have to write the start and the end columns
#  within brackets and divided with a ":", just as you set a range of columns in Excel
# "skiprows": it skips the first x rows, and reads the x+1-st row as table name
# "nrows": maximum number of rows to be loaded. If the "skiprows" has been set,
# nrows counts the number of rows from the value set in skiprows + 1
second_sheet_name="Sales Report skiprow"
dataframe_from_specific_segment=pd.read_excel(excel_file_location, second_sheet_name, usecols="A:B",skiprows=4,nrows=3)
# Step 4.) showing the loaded excel
dataframe_from_specific_segment
