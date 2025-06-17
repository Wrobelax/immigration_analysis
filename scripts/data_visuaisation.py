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

df_sorted = df_can.sort_values(by = "Total", ascending = False, axis = 0)
df_top5 = df_sorted.head(5)
df_top5 = df_top5[years].transpose()
df_top5.index = df_top5.index.map(int)

df_dns = df_can.loc[["Denmark", "Norway", "Sweden"], years].transpose()



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


# Visualisation of immigration from top 5 contributing countries - line plot.
# df_top5.plot(kind = "line", figsize = (14,8))
#
# plt.title("Immigration trend of top 5 countries")
# plt.xlabel("Years")
# plt.ylabel("Number of immigrants")
#
# plt.savefig("../outputs/top5_immigration_line.png") # Saving results to file
# plt.show()


# Visualisation of immigration from top 5 contributing countries - area plot.
# df_top5.plot(kind = "area", stacked = True, alpha = 0.35, figsize = (14,8))
#
# plt.title("Immigration trend of top 5 countries")
# plt.xlabel("Years")
# plt.ylabel("Number of immigrants")
#
# plt.savefig("../outputs/top5_immigration_area.png") # Saving results to file
# plt.show()


# Visualisation of immigration in 2013 (last) year between countries.
count, bin_edges = np.histogram(df_can["2013"])
# print(count)
# print(bin_edges)

# df_can["2013"].plot(kind = "hist", figsize = (12,6), xticks = bin_edges, color = "skyblue")
#
# plt.title("Histogram of immigration from all countries in 2013")
# plt.xlabel("Number of immigrants")
# plt.ylabel("Number of countries")
#
# plt.savefig("../outputs/2013_immigration.png") # Saving results to file
# plt.show()


# Visualisation of total immigration from Denmark, Norway and Sweden.
count2, bin_edges2 = np.histogram(df_dns, 15)
xmin = bin_edges2[0] - 10
xmax = bin_edges2[-1] + 10

df_dns.plot(kind = "hist",
            figsize = (12,8),
            bins = 15,
            xticks = bin_edges2,
            color = ["coral", "darkslateblue", "mediumseagreen"],
            stacked = True,
            xlim = (xmin, xmax)
            )

plt.title("Histogram of total immigration form Denmark, Norway and Sweden")
plt.xlabel("Number of immigrants")
plt.ylabel("Years")

plt.savefig("../outputs/den_nor_swed_immigration.png") # Saving results to file
plt.show()


# Visualisation of total immigration from Albania, Greece and Bulgaria.
