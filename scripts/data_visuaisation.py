"""This is a script for data modeling and visualisation used for generating outputs.
Some lines with code are commented as they were used solely for analysis and left for reference.
"""


# Modules importing.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Importing file with cleaned data into dataframe.
url = "../data/cleaned_data.csv"
df_can = pd.read_csv(url)