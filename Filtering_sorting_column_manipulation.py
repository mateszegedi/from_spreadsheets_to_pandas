# Filteing pandas table
#
# Step 1.) importing libraries and test table to a dataframe
import pandas as pd
import numpy as np
excel_file_location=r"/home/mate/Asztal/Python things/Blog materials/sales_report.xlsx"
sheet_name="Sales Report"
dataframe = pd.read_excel(excel_file_location, sheet_name)

# Step 2.) listing the table names
dataframe.columns

# Showing only one column from the table
dataframe["Name_of_the_column"]

# Showing multiple columns from the table
dataframe[["Name_of_the_column","Name_of_other_column"]]

# Saving a subset of the original table to a new table
dataframe_subset=dataframe["Name_of_the_column","Name_of_other_column"]

# Saving a subset of the original table to a new table,
# where the values in a column are higher than 0
# important: only works, if the column contains only numerical values!
dataframe_subset=dataframe[dataframe["Name_of_the_column"]>0]

# Saving a subset of the original table to a new table,
# where the values in a column contains the substring "ello"
dataframe_subset=dataframe[dataframe["Name_of_the_column"].str.contains("ello")]

# Saving a subset of the original table to a new table,
# where the values in a column are not "world"
dataframe_subset=dataframe[dataframe["Name_of_the_column"]!="world"]

# Saving a subset of the original table to a new table,
# where the values in a column are exactly "hello world"

dataframe_subset=dataframe[dataframe["Name_of_the_column"]=="hello world"]

# Saving a subset of the original table to a new table,
# where multiple conditions are true
dataframe_subset=dataframe[(dataframe["Name_of_the_column"].str.contains("ello")&(dataframe["Name_of_other_column"]>0))]

# Saving a subset of the original table to a new table,
# where one of the conditions is true

dataframe_subset=dataframe[(dataframe["Name_of_the_column"].str.contains("ello")|(dataframe["Name_of_other_column"]>0))]

# Saving the original table to a new table, where it is sorted by a column ascending
dataframe_subset=dataframe.sort_values(by="Name_of_the_column", ascending=True)

# Reordering columns
dataframe[["Name_of_the_column_in_the_new_order","Name_of_other_column_in_the_new_order"]]

# Renaming columns
dataframe=dataframe.rename(columns={"old_column_name":"new_column_name","other_old_column_name":"other_new_column_name"})
