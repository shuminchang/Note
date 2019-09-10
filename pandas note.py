#To import pandas module
import pandas as pd

#To create DataFrame and Series by hand
pd.DataFrame()
pd.DataFrame({'': [], '': []}, index=['', ''])
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})  # keys for index of column, values for values, start from the first row
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})  # can also input string
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])  # 'index': index for rows

pd.Series([int, 'object'], index=['', ''], name='')  # index for index, name for Series's name, name can be num or string
pd.Series([1, 2, 3, 4, 5])  # create series
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

#To read csv file
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")  # read csv file with default index of row
wine_reviews.shape  # show (rows, columns) of dataframe
wine_review = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)  # read csv file with the first column as the index of row
wine_reviews.head()

#To read excel file
wic = pd.read_excel("../input/publicassistance/xls_files_all/WICAgencies2013ytd.xls", sheet_name='Total Women')

#To read SQL file
# import sqlite3 library
import sqlite3
# create a connector between sqlite database and python
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

'''
Indexing and Selecting
'''
# Index-based selection(iloc)
df['A']
df.A
df['A'][0]  # select column 'A', select first row
df.iloc[0]  # select first row
df.iloc[:, 0]  # select first column, select first value of rows
df.iloc[:3, 0] = df.iloc[[0, 1, 2], 0]  # select first three row, select first column
df.iloc[1:3, 0]  # select second and third row, select first column
df.iloc[-5:0]  # select last five row

# Label-based selection
df.loc[0, 'country']  # select first row, select column 'country'
df.loc[:, ['A', 'B', 'C']]  # select every row, selection column A, B, C

# Manipulating the index
df.set_index("title")  # set column 'title' as index

# Conditional selection
df.country == 'Italy'  # the value is 'Italy' will be True, else will be False
df.loc[df.country == 'Italy']  # select every value in dataframe df which value of column 'country' is 'Italy'
df.loc[(df.country == 'Italy') & (df.points >= 90)]  #  column 'country' = 'Italy' and column 'point' >= 90
df.loc[(df.country == 'Italy') | (df.points >= 90)]  # '|' = 'or'
df.loc[df.country.isin(['Italy', 'France'])]  # select multiple conditions
df.loc[df.price.notnull()]  # select not null value in column 'price'

# Assigning data
df['new column'] = 'everyone'  # input 'everyone' in every row of column 'new column'
df['index_backwards'] = range(len(columnA), 0, -1)  # input number from the number of the length of columnA to the first number, step = -1

# Summary functions
df.points.describe()
df.points.mean()
df.taster_name.unique()
df.taster_name.value_counts()

# Maps
# Series.map
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

# DataFrame.apply
def remean_points(row):
  row.points = row.points - review_points_mean
  return row
reviews.apply(remean_points, axis='columns')

# faster way
review_points_mean = reviews.points.mean()
review.points - review_points_mean

# an easy way of combining country and region
reviews.country + " - " + reviews.region_1

# >, <, ==,  faster, but not flexible
# map, apply     slower, but flexible

'''
Grouping and sorting
'''
# https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html - Groupby: split-apply-combine
# https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html - Multiindex/Advanced indexing
# https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html - Advanced basic functionality
# Grouping
reviews.groupby('points').points.count()  # group by count of 'points' column, and show 'points' column
reviews.groupby('points').price.min()  # group 'points' column, by min price, show price
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])  # group 'winery' column, show first title 
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.argmax()])  # get best wine in every province
reviews.groupby(['country']).price.agg([len, min, max])
# Multi-indexes
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed.reset_index()
# Sorting
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len', ascending=False)  # follow the order by 'len'
countries_reviewed.sort_index()
countries_reviewed.sort_values(by=['country', 'len'])
-----------------------------------------------------------------------------------------------------------------

df.points.median()  # show median of column 'points'
df.country.unique()  # show unique value in column 'country'
df.country.value_counts()  # show the number of every row of every unique value in column 'country', desc
df.price - df.price.mean()  # calculate every value in the column 'price' - mean of column 'price'

bargain_idx = (df.points / df.price).idxmax()
bargain_wine = df.loc[bargain_idx, 'title']  # Return index of first occurrence of maximum over requested axis. NA/null values are excluded.

df.A.iloc[0]
review[:1]
df.A.iloc[:10]
df.A.head(10)
df.loc[:9, 'A']
df.iloc[[1, 2, 3, 5, 8]]  # select row 1, 2, 3, 5, 8 (start from 0)
df.iloc[[0, 1, 10, 100], [0, 5, 6, 7]]  # select row 0, 1, 10, 100 and column 0, 5, 6, 7
df.iloc[0:100, [0, 11]]
df.query("country == 'Italy'")
df.query("country == ['Australia', 'New Zealand'] and points > 94")

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
