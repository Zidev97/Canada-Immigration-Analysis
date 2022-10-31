import numpy as np
import pandas as pd
import openpyxl
import matplotlib as mpl
import matplotlib.pyplot as plt


# Reading and Cleaning Data from Excel File
URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx'
df = pd.read_excel(
    URL,
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)
print('Data downloaded and read into a dataframe!')
pd.set_option('expand_frame_repr', None)
df.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
print(df.head())
df.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)
print(df.head())
df.set_index('Country',inplace=True)
print(df.head())
print(df.loc['Morocco',:])
# add total immigrants per country
df['Total'] = df.sum(axis=1)
print(df)
# Plotting the top 10 countries with immigrants to Canada using a stacked Area plot
Years=list(range(1980,2014))
print(Years)
df.sort_values(['Total'],ascending=False,inplace=True)
print(df.head(10))
df_sort=df.head(10)
df_sort=df_sort[Years].transpose()
print(df_sort)
#df_sort.index=df_sort.index.map(int)
print(df_sort)
df_sort.plot(kind='area',figsize=(20,10))
plt.title('Immigration Trend of Top 10 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()
# Plotting the least 10 countries with immigrants to Canada using a stacked Area plot
Years_least=list(range(1980,2014))
print(Years_least)
df.sort_values(['Total'],ascending=True,inplace=True)
print(df.head(10))
df_sort_least=df.head(10)
df_sort_least=df_sort_least[Years].transpose()
print(df_sort_least)
#df_sort.index=df_sort.index.map(int)
print(df_sort_least)
df_sort_least.plot(kind='area',figsize=(20,10))
plt.title('Immigration Trend of Least 10 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()