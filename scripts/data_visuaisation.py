"""This is a script for data modeling and visualisation used for generating outputs.
Some lines with code are commented as they were used solely for analysis and left for reference.
"""


# Modules importing.
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Importing file with cleaned data into dataframe.
url = "../data/cleaned_data.csv"
df_can = pd.read_csv(url)



"""Preparing dataset for visualisation"""
# Setting "Country" as index and removing the name of index.
df_can.set_index("Country", inplace = True)
df_can.index.name = None

# Sorting values by 'Total'.
df_can.sort_values(by = "Total", ascending = False, axis = 0, inplace = True)

# Creating variables for easier reference.
years = list(map(str, range(1980, 2014)))
haiti = df_can.loc["Haiti", years]
df_ci = df_can.loc[["India", "China"], years].transpose()
df_ci.index = df_ci.index.map(int)
df_top5 = df_can.


"""Data visualisation"""
# Visualisation of Haiti immigration.
# haiti.index = haiti.index.map(int)
# haiti.plot(kind = "line")
#
# plt.title("Immigration from Haiti")
# plt.xlabel("Years")
# plt.ylabel("Number of immigrants")
# plt.text(2000, 6000, "2010 Earthquake")
#
# plt.savefig("../outputs/haiti_immigration.png") # Saving results to file
# plt.show()


# Visualisation of immigration from India and China.
# df_ci.plot(kind = "line")
#
# plt.title("Immigration from China and India")
# plt.xlabel("Years")
# plt.ylabel("Number of immigrants")
#
# plt.savefig("../outputs/china_india_immigration.png") # Saving results to file
# plt.show()


