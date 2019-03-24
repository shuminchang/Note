#To import pandas module
import pandas as pd

#To create DataFrame and Series by hand
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])
pd.Series([1, 2, 3, 4, 5])
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

#To read csv file
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")
wine_reviews.shape
wine_review = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
wine_reviews.head()

#To read excel file
wic = pd.read_excel("../input/publicassistance/xls_files_all/WICAgencies2013ytd.xls", sheet_name='Total Women')

#To read SQL file
import sqlite3
conn = sqlite3.connect("../input/188-million-us-wildfires/FPA_FOD_20170508.sqlite")
fires = pd.read_sql_query("SELECT * FROM fires", conn)
fires.head()

#Write things to csv file
wine_reviews.head().to_csv("wine_reviews.csv")

#Write things to excel file
wic.to_excel('wic.xlsx', sheet_name='Total Women')

#Write things to SQL file
conn = sqlite3.connect("fires.sqlite")
fires.head(10).to_sql("fires", conn)

#Indexing and Selecting
x = df['A']
x = df.A
x = df.A.iloc[0]
x = review[:1]
x = df.A.iloc[:10]
x = df.A.head(10)
x = df.loc[:9, 'A']
x = df.iloc[[1, 2, 3, 5, 8]]  # select row 1, 2, 3, 5, 8 (start from 0)
x = df.iloc[[0, 1, 10, 100], [0, 5, 6, 7]]  # select row 0, 1, 10, 100 and column 0, 5, 6, 7
x = df.iloc[0:100, [0, 11]]
x = df.query("country == 'Italy'")
x = df.query("country == ['Australia', 'New Zealand'] and points > 94")
