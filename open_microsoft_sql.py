# Loading microsoft sql to pandas
#
# Step 1.) importing libraries to be able marke
# a query to a relational database (like MySQL) with Python
# and to load the result directly into a pandas table
import pandas as pd
import numpy as np
# pyodbc is library to connect to databases
import pyodbc

# Step 2.) setting up a connection with the database
# For the following variables, you might need to ask your admins
conn = pyodbc.connect("Driver={SQL Server};""Server=Servername;""Database=Database_name;""Trusted_Connection=yes;")

# Step 3.) making a query to a database and load the result directly to a dataframe
dataframe = pd.read_sql_query("SELECT * FROM Test_Table_name",conn)

# Step 4.) showing the results in a table format
dataframe
