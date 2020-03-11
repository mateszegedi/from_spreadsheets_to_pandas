# Exporting pandas to csv, excel file
#
# Step 1.) importing libraries and test table to a dataframe

import pandas as pd
import numpy as np
excel_file_location=r"/home/mate/Asztal/Python things/Blog materials/sales_report.xlsx"
sheet_name="Sales Report"
dataframe = pd.read_excel(excel_file_location, sheet_name)

# Step 2.) do any kind of transformation

# Save the dataframe as a new .csv file
# Important: if you have a file with the same name, this will overwrite it!
# Index - if you do not wish to export the index (number of rows) as a separate column, set it to False
# sep = separator
#
# If you have multiple dataframes, you have to save these to different files
dataframe.to_csv("location/name_of_new_csv_file.csv", Index=False, sep=";")

# append dataframe to an existing files
# Important: only then works properly, if the .csv has the same number of columns as the dataframe
dataframe.to_csv("location/name_of_new_csv_file.csv", Index=False, sep=";";  mode='a', header=False)

# Save the dataframe as a new excel file
dataframe.to_excel("location/name_of_new_excel_file.xlsx", sheet_name='Sheet_name', Index=False)

# Append the dataframe to an existing table
with pd.ExcelWriter("location/name_of_new_excel_file.xlsx",mode='a') as writer:
    dataframe.to_excel(writer, sheet_name='Sheet_name')
