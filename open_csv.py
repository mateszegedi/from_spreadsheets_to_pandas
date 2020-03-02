# Loading a .csv to pandas
# 
# Step 1.) importing libraries to be able to open excel file with Python
import pandas as pd
import numpy as np
# Step 2.) setting the location of csv file.
# important: it is generally useful to write it like this r"C:\Users\...."
csv_file_location=r"/home/mate/Asztal/Python things/Blog materials/sales_report_csv.csv"
# Step 3.) opening the excel to a dataframe (e.g.Python table)
# It is generally a good idea to set with "sep", by which character the columns should be splitted
csv_dataframe = pd.read_csv(csv_file_location, sep=",")
# Step 4.) showing the loaded csv
csv_dataframe
