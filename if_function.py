# Reproducing IF function in pandas
#
# Step 1.) importing libraries and test table to a dataframe

import pandas as pd
import numpy as np
excel_file_location=r"/home/mate/Asztal/Python things/Blog materials/sales_report.xlsx"
sheet_name="Sales Report"
dataframe = pd.read_excel(excel_file_location, sheet_name)

# 2.) setting up a single condition
conditions= [
    (dataframe["Name_of_the_column"]>0)
]

# setting up multiple condition, where all are true
conditions= [
    ((dataframe["Name_of_the_column"]>0)&(dataframe["Name_of_the_column"]<10))
]
# setting up multiple condition, where at least one is true
conditions= [
    ((dataframe["Name_of_the_column"]==0)|(dataframe["Name_of_the_column"]==1))
]
# setting up multiple scenarios - eg, if not true,else if ...
conditions= [
    (dataframe["Name_of_the_column"]>0),
    (dataframe["Name_of_the_column"]<10)
]
# choices - if the condition is true, which value should be here
#
#   !important!
# Within the brackets, always exactly as many elements
# must be listed, as was the number of commas + 1 in the conditions
# e.g. if you had only one condition, then choices need 1 item,
# if you had 2, choices need 2 items, etc

choices=["column has values between 1 and 10","column has 0s or 1s"]

# store the result of the "IF" function as a new column in the dataframe
# the "default" is the "else", if none of the above set conditions are True
dataframe["Result_of_the_if_function"]=np.select(conditions,choices,default="columns have values outside of  range [1,10]")
