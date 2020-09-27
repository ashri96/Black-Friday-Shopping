"""BlackFriday.ipynb"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerBase
from matplotlib.text import Text
import seaborn as sns
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from google.colab import files
uploaded = files.upload()

df = pd.read_excel('BlackFriday.xlsx')

df.head()

df.shape

df.describe()

df.info()

sns.heatmap(df.corr(), annot = True, fmt = '.2f', cmap = 'vlag_r', center = 0)

df.isnull().sum()

df["Product_Category_1"].value_counts()

df["Product_Category_2"].value_counts()

df["Product_Category_3"].value_counts()

df_copy = df.copy()

print("Shape of orginial df: {}".format(df.shape))
print("Shape of copy df_copy: {}".format(df_copy.shape))

df_copy.dropna(inplace = True)

print("Shape of orginial df: {}".format(df.shape))
print("Shape of copy df_copy: {}".format(df_copy.shape))

df_copy[["Product_ID","Product_Category_1","Product_Category_2","Product_Category_3"]].head()

#df_copy.dropna().shape[0]/df_copy.shape[0]
print ("Propotion of missing values in df :{0:.2f}".format((df.shape[0] - df_copy.shape[0])/df.shape[0]))

#Removing NaN values is resulting in loss of 70% of the data. Since that is a lot of data, we will replace NaN with zeros

df.fillna(0, inplace= True)

df.isnull().sum()

def count_plot(dataframe, column_name, title = None, hue = None):
  base_color = sns.color_palette()[0]
  sns.countplot(data = dataframe, x= column_name, hue= hue)
  plt.title(title)
  pass

def simple_bar_plot(data, title = None):
  data.plot("bar", title = title)
  pass

#legend displayed
class TextHandler(HandlerBase):
  def create_artists(self, legend, tup, xdescent, ydescent, width, height, fontsize, trans):
    tx = Text(width/2.,height/2,tup[0], fontsize=fontsize,
                  ha="center", va="center", color=tup[1], fontweight="bold")
    return [tx]

#top 10 poducts sold
df["Product_ID"].value_counts(sort=True)[:10]

#plotting the top 10 products sold
simple_bar_plot(df["Product_ID"].value_counts(sort=True)[:10], title = "Top 10 products sold")

#plotting the product category
simple_bar_plot(df["Product_Category_1"].value_counts(sort=True)[:10], 
                title = "Top 10 Product Category of people interested")

count_plot(df,"Marital_Status","Marital Status of Buyers")

#Check who purchase more
count_plot(df,"Gender","Men or Women spent more ?","Gender")
