"""This is a script used for data reading, basic exploration, cleaning and extracting new file.
Some code was left commented as it was used ald left for reference.
"""

# Importing modules.
import pandas as pd
import numpy as np


# Reading file and assigning it to pandas module.
df_can = pd.read_excel(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx",
    sheet_name = "Canada by Citizenship",
    skiprows = range(20),
    skipfooter = 2)


"""Basic data exploration for data cleaning."""
# Checking general data
# print(df_can.head())
# print(df_can.tail())
# print(df_can.info(verbose = False))
# print(df_can.columns) # 'Type','Coverage','OdName','AREA','AreaName','REG','RegName','DEV','DevName',Years from '1980'-'2013'.
# print(df_can.index) # 195 rows.
# print(type(df_can.columns)) # Index to be changed.
# print(type(df_can.index)) # Not lists.
# print(df_can.shape) # 195 rows, 43 columns.
# print(df_can.isnull().sum()) # No empty cells.
# print(df_can.dtypes)


"""Data cleaning, formatting, type changing, filling missing data."""
# Converting columns to list.
df_can.columns.tolist()
df_can.index.tolist()

# Dropping columns - they will not be used during analysis.
df_can.drop(["AREA", "REG", "DEV", "Type", "Coverage"], axis = 1, inplace = True)

# Renaming columns for easier reference.
df_can.rename(columns = {"OdName": "Country", "AreaName": "Continent", "RegName": "Region"}, inplace = True)

# Adding "Total" column that will sum all immigrants for each country.
df_can["Total"] = df_can[list(range(1980,2014))].sum(axis = 1)


"""Saving cleaned file"""
df_can.to_csv("../data/cleaned_data.csv", index = False) # Saving cleaned file in csv format for easier use.

