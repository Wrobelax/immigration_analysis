"""This is a script for data modeling and visualisation used for generating outputs.
Some lines with code are commented as they were used solely for analysis and left for reference.
"""


# Modules importing.
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import ListedColormap
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



"""Creating variables for easier reference"""
# Variable for years.
years = list(map(str, range(1980, 2014)))

# Variable for total data for Haiti.
haiti = df_can.loc["Haiti", years]

# Variable for China and India total.
df_ci = df_can.loc[["India", "China"], years].transpose()
df_ci.index = df_ci.index.map(int)

# Variable for top 5 countries.
df_sorted = df_can.sort_values(by = "Total", ascending = False)
df_top5 = df_sorted.head(5)
df_top5 = df_top5[years].transpose()
df_top5.index = df_top5.index.map(int)

# Variable for Denmark, Norway and Sweden.
df_dns = df_can.loc[["Denmark", "Norway", "Sweden"], years].transpose()

# Variable for Greece, Bulgaria and Albania.
df_gba = df_can.loc[["Greece", "Bulgaria", "Albania"], years].transpose()

# Variable for Iceland.
df_ice = df_can.loc["Iceland", years]

# Variable for top 15 countries.
df_top15 = df_sorted["Total"].head(15).transpose()

# Variable for continents.
df_continents = df_can.groupby("Continent").sum()
df_cont_tot = df_can.groupby("Continent")["Total"].sum()

# Variable for Japan.
df_jap = df_can.loc[["Japan"],years].transpose()

# Variable for total data lock.
df_tot = pd.DataFrame(df_can[years].sum(axis = 0))
df_tot.index = map(int, df_tot.index)
df_tot.reset_index(inplace = True)
df_tot.columns = ["year", "total"]

# Variable for total data lock with transpose.
df_can_tot = df_can[years].transpose()
df_can_tot.index = map(int, df_can_tot.index)
df_can_tot.index.name = "Year"
df_can_tot.reset_index(inplace = True)

# Variable for normalized Brazil data.
norm_br = (df_can_tot["Brazil"] - df_can_tot["Brazil"].min() / (df_can_tot["Brazil"].max() - df_can_tot["Brazil"].min()))

# Variable for normalized Argentina data.
norm_arg = (df_can_tot["Argentina"] - df_can_tot["Argentina"].min() / (df_can_tot["Argentina"].max() - df_can_tot["Argentina"].min()))



"""Data visualisation"""
# Visualisation of Haiti immigration.
haiti.index = haiti.index.map(int)
haiti.plot(kind = "line")

plt.title("Immigration from Haiti")
plt.xlabel("Years")
plt.ylabel("Number of immigrants")
plt.text(2000, 6000, "2010 Earthquake")

# plt.savefig("../outputs/haiti_immigration.png") # Saving results to file


# Visualisation of immigration from India and China.
df_ci.plot(kind = "line")

plt.title("Immigration from China and India")
plt.xlabel("Years")
plt.ylabel("Number of immigrants")

# plt.savefig("../outputs/china_india_immigration.png") # Saving results to file


# Visualisation of immigration from top 5 contributing countries - line plot.
df_top5.plot(kind = "line", figsize = (14,8))

plt.title("Immigration trend of top 5 countries")
plt.xlabel("Years")
plt.ylabel("Number of immigrants")

# plt.savefig("../outputs/top5_immigration_line.png") # Saving results to file


# Visualisation of immigration from top 5 contributing countries - area plot.
df_top5.plot(kind = "area", stacked = True, alpha = 0.35, figsize = (14,8))

plt.title("Immigration trend of top 5 countries")
plt.xlabel("Years")
plt.ylabel("Number of immigrants")

# plt.savefig("../outputs/top5_immigration_area.png") # Saving results to file


# Visualisation of immigration in 2013 (last) year between countries.
count, bin_edges = np.histogram(df_can["2013"])
print(count)
print(bin_edges)

df_can["2013"].plot(kind = "hist", figsize = (12,6), xticks = bin_edges, color = "skyblue")

plt.title("Histogram of immigration from all countries in 2013")
plt.xlabel("Number of immigrants")
plt.ylabel("Number of countries")

# plt.savefig("../outputs/2013_immigration.png") # Saving results to file


# Visualisation of total immigration from Denmark, Norway and Sweden.
count2, bin_edges2 = np.histogram(df_dns, 15)
xmin = bin_edges2[0] - 10
xmax = bin_edges2[-1] + 10

df_dns.plot(kind = "hist",
            figsize = (12,8),
            bins = 15,
            xticks = bin_edges2,
            color = ["coral", "darkslateblue", "mediumseagreen"],
            alpha = 0.6,
            stacked = True,
            xlim = (xmin, xmax)
            )

plt.title("Histogram of total immigration form Denmark, Norway and Sweden")
plt.xlabel("Number of immigrants")
plt.ylabel("Number of years")

# plt.savefig("../outputs/den_nor_swed_immigration.png") # Saving results to file


# Visualisation of total immigration from Albania, Greece and Bulgaria.
count3, bin_edges3 = np.histogram(df_gba, 15)
xmin = bin_edges3[0] - 10
xmax = bin_edges3[-1] + 10

df_gba.plot(kind = "hist",
            figsize = (12,8),
            bins = 15,
            xticks = bin_edges3,
            color = ["purple", "skyblue", "lightgreen"],
            alpha = 0.35,
            stacked = True,
            xlim = (xmin, xmax)
            )

plt.title("Histogram of total immigration form Greece, Bulgaria and Albania")
plt.xlabel("Number of immigrants")
plt.ylabel("Number of years")

# plt.savefig("../outputs/gr_bul_alb_immigration.png") # Saving results to file


# Visualisation of immigration from Iceland - checking if 2008 crisis had an impact.
df_ice.plot(kind = "bar", figsize = (12,8), rot = 90)

plt.title("Icelandic immigration to Canada between years 1980 - 2013")
plt.xlabel("Year")
plt.ylabel("Number of immigrants")

plt.annotate("",
             xy = (32, 70),
             xytext = (28, 20),
             xycoords = "data",
             arrowprops = dict(arrowstyle = "->",
                               connectionstyle = "arc3",
                               color = "red",
                               lw = 2)
             )

plt.annotate("2008 - 2011 financial crisis",
             xy = (28, 30),
             rotation = 75,
             va = "bottom",
             ha = "left",
             )

# plt.savefig("../outputs/iceland_immigration.png") # Saving results to file


# Visualisation of immigration from top 15 contributing countries.
df_top15.plot(kind = "barh", figsize = (11, 11), color = "steelblue")

plt.title("Top 15 countries contributing to immigration in Canada between 1980 - 2013")
plt.xlabel("Number of immigrants")

for index, value in enumerate(df_top15):
    label = format(int(value), ",")
    plt.annotate(label, xy = (value - 47000, index - 0.1), color = "white")


# plt.savefig("../outputs/top15_immigration.png") # Saving results to file


# Visualisation of a total immigration contribution per continent.
df_continents["Total"].plot(kind = "pie",
                                 figsize = (10, 6),
                                 autopct = "%1.1f%%",
                                 startangle = 90,
                                 shadow = False,
                                 labels = None,
                                 pctdistance = 1.12,
                                 colors = ["gold",
                                           "lightcoral",
                                           "yellowgreen",
                                           "lightskyblue",
                                           "lightgreen",
                                           "pink"],
                                 explode = [0.1, 0, 0, 0, 0.1, 0.1]
                                 )

plt.title("Immigration to Canada per Continent in 1980 - 2013", y = 1.08, fontsize = 15)
plt.axis("equal")
plt.legend(labels = df_continents.index, loc = "upper left", fontsize = 8)

# # plt.savefig("../outputs/continents_immigration.png") # Saving results to file


# Visualisation of immigration to Canada from Japan.
df_jap.plot(kind = "box", figsize = (8, 6))

plt.title("Box plot of immigration to Canada from Japan")
plt.ylabel("Number of immigrants")

# plt.savefig("../outputs/japan_immigration.png") # Saving results to file


# Visualisation of immigration to Canada from India and China on a box plot.
df_ci.plot(kind = "box", figsize = (10, 7), vert = False)

plt.title("Box plot of immigration to Canada from India and China")
plt.xlabel("Number of immigrants")

# plt.savefig("../outputs/china_india_box_immigration.png") # Saving results to file


# Visualisation of a total contribution to immigration to Canada per continent in comparison to 1980 and 2013.
fig = plt.figure()
ax0 = fig.add_subplot(1, 2, 1)
ax1 = fig.add_subplot(1, 2, 2)

df_continents["1980"].plot(kind = "pie",
                           figsize = (13, 9),
                           autopct = "%1.1f%%",
                           startangle = 90,
                           shadow = False,
                           labels = None,
                           pctdistance = 1.12,
                           colors = ["gold",
                                     "lightcoral",
                                     "yellowgreen",
                                     "lightskyblue",
                                     "lightgreen",
                                     "pink"],
                           explode = [0.1, 0, 0, 0, 0.1, 0.15],
                           ax = ax0,
                           )
ax0.set_title("Immigration to Canada per Continent in 1980")
ax0.axis("equal")
ax0.set_ylabel("")
ax0.legend(labels = df_continents.index, loc = "upper left", fontsize = 7)

df_continents["2013"].plot(kind = "pie",
                           figsize = (13, 9),
                           autopct = "%1.1f%%",
                           startangle = 90,
                           shadow = False,
                           labels = None,
                           pctdistance = 1.12,
                           colors = ["gold",
                                     "lightcoral",
                                     "yellowgreen",
                                     "lightskyblue",
                                     "lightgreen",
                                     "pink"],
                           explode = [0.1, 0, 0, 0, 0.1, 0.15],
                           ax = ax1,
                           )
ax1.set_title("Immigration to Canada per Continent in 2013")
ax1.set_ylabel("")
ax1.axis("equal")

# plt.savefig("../outputs/continents_pie_immigration.png") # Saving results to file


# Visualisation of total immigration to Canada between years.
df_tot.plot(kind = "scatter",
            x = "year",
            y = "total",
            figsize = (10, 6),
            color = "darkblue",
            )

plt.title("Total immigration to Canada from 1980 - 2013")
plt.xlabel("Year")
plt.ylabel("Number of immigrants")

# plt.savefig("../outputs/total_immigration.png")  # Saving results to file


# Visualisation of a linear regression on a total immigration to Canada between years.
x = df_tot["year"]
y = df_tot["total"]
fit = np.polyfit(x, y, deg = 1)

df_tot.plot(kind = "scatter", x = "year", y = "total", figsize = (10,6), color = "darkblue")

plt.title("Total immigration to Canada from 1980 - 2013")
plt.xlabel("Year")
plt.ylabel("Number of immigrants")

plt.plot(x, fit[0] * x + fit[1], color = "darkred")

# plt.savefig("../outputs/total_immigration_reg.png")  # Saving results to file


# Visualisation of a polynomial regression on a total immigration to Canada between years.
x1 = df_tot["year"]
y1 = df_tot["total"]
fit1 = np.polyfit(x1, y1, deg = 10)
poly_func = np.poly1d(fit1)

df_tot.plot(kind = "scatter", x = "year", y = "total", figsize = (10,6), color = "darkblue")

plt.title("Total immigration to Canada from 1980 - 2013")
plt.xlabel("Year")
plt.ylabel("Number of immigrants")

x_vals = np.linspace(x1.min(), x1.max(), 200)
y_vals = poly_func(x_vals)
plt.plot(x_vals,y_vals, color = "darkred")

# plt.savefig("../outputs/total_immigration_poly_reg.png")  # Saving results to file


# Visualisation of an immigration to Canada from Argentina and Brazil.
ax2 = df_can_tot.plot(kind = "scatter",
                      x = "Year",
                      y = "Brazil",
                      figsize = (14, 8),
                      alpha = 0.5,
                      color = "green",
                      s = norm_br * 0.2,
                      xlim = (1975, 2015)
                      )

ax3 = df_can_tot.plot(kind = "scatter",
                      x = "Year",
                      y = "Argentina",
                      figsize = (14, 8),
                      alpha = 0.5,
                      color = "red",
                      s = norm_arg * 0.2,
                      ax = ax2
                      )

ax2.set_title("Immigration from Brazil and Argentina from 1980 - 2013")
ax2.set_ylabel("Number of immigrants")
ax2.legend(["Brazil", "Argentina"], loc = "upper left", fontsize = "x-large")
# plt.savefig("../outputs/brazil_argentina_immigration.png")  # Saving results to file

# plt.show() # Uncomment to generate all outputs