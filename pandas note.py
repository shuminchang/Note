#To import pandas module
import pandas as pd

#To create DataFrame and Series by hand
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})  # keys for index of column, values for values, start from the first row
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})  # can also input string
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])  # 'index': index for rows
pd.Series([1, 2, 3, 4, 5])  # create series
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

#To read csv file
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")  # read csv file with default index of row
wine_reviews.shape
wine_review = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)  # read csv file with the first column as the index of row
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
wic.to_excel('wic.xlsx', sheet_name='Total Women')  # problem encountered!

#Write things to SQL file
conn = sqlite3.connect("fires.sqlite")  # create a connector
fires = pd.read_sql_query("SELECT * FROM fires", conn)  # write a SQL statement

# Writing common file formats
wine_reviews.head().to_csv("wine_reviews.csv")  # output dataframe as csv file
wic.to_excel('wic.xlsx', sheet_name='Total Women') # write a excel file
conn = sqlite3.connect("fires.sqlite")
fires.head(10).to_sql("fires", conn)  # output to a SQL database  

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

# Count unique value
df.nunique()

# Grouping
reviews.groupby('points').points.count()
reviews.groupby('points').price.min()
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.argmax()])
reviews.groupby(['country']).price.agg([len, min, max])
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed.reset_index()

# Sorting
countries_reviewed.sort_values(by='len')
countries_reviewed.sort_values(by='len', ascending=False)
countries_reviewed.sort_index()
countries_reviewed.sort_values(by=['country', 'len'])

# type
reviews.price.dtype  # column 'price' type
reviews.dtypes # each column type
reviews.points.astype('float64')  # transform to float data type
reviews.index.dtype  # index's type

# change type
df.column.astype('int64') # object, int64, float64
pd.to_numeric(df.column)

# drop
df = df.drop('HDI for year', 1)  # drop column 'HDI for year'

# replace
df[' gdp_for_year ($) '] = [ i.replace(",","") for i in df[' gdp_for_year ($) '] ]  # remove ',' - thousand separator

# Missing values
reviews.country.isnull()  # check null in column country
reviews.region_2.fillna("Unknown")  # replace NaN with 'Unknown'
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")  # replace non-missing values, replace '@kerinokeefe' to '@kerino'

# count missing values
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)

n_missing_prices = reviews.price.isnull().sum()

n_missing_prices = pd.isnull(reviews.price).sum()

# Renaming
reviews.rename(columns={'points': 'score'}) # rename column name 
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'}) # rename index 0 and index 1
reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns') # give name to column and index
df.rename(str.lower, axis='columns') # lowercase the columns
df.rename({1: 2, 2: 4}, axis='index') # rename index

# Combining
pd.concat([canadian_youtube, british_youtube]) # combine along axis = 0
left.join(right, lsuffix='_CAN', rsuffix='_UK') # combine along axis = 1, and modify column name

# show full dataframe
pd.set_option('display.max_columns', number_you_need)
pd.set_option('display.max_rows', number_you_need)
