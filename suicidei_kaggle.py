# Dataset: Suicide Rates Overview 1985 to 2016
# Reference: https://www.kaggle.com/lmorgan95/r-suicide-rates-in-depth-stats-insights

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read csv file
df = pd.read_csv('D:\coding\data\master.csv')

# rename the column with space and symbols
df.rename(columns={' gdp_for_year ($) ': 'gdp_for_year'}, inplace=True)
df.rename(columns={'gdp_per_capita ($)': 'gdp_per_capita'}, inplace=True)
df.rename(columns={'suicides/100k pop': 'suicides100k'}, inplace=True)

# remove ',' from gdp_for_year
df['gdp_for_year'] = [ i.replace(",", "") for i in df['gdp_for_year'] ]

# create lists of continents
Asia = ['Armenia', 'Azerbaijan', 'Bahrain', 'Israel', 'Japan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Macau', 'Maldives',
        'Mongolia', 'Oman', 'Philippines', 'Qatar', 'Republic of Korea', 'Singapore', 'Sri Lanka', 'Thailand', 'Turkey',
        'Turkmenistan', 'United Arab Emirates', 'Uzbekistan']
America = ['Antigua and Barbuda', 'Argentina', 'Aruba', 'Bahamas', 'Barbados', 'Belize', 'Brazil', 'Canada', 'Chile',
           'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'Ecuador', 'El Salvador', 'Grenada', 'Guatemala', 'Guyana',
           'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Puerto Rico', 'Saint Kitts and Nevis', 'Saint Lucia',
           'Saint Vincent and Grenadines', 'Suriname', 'Trinidad and Tobago', 'United States', 'Uruguay']
Europe = ['Albania', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus',
          'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary',
          'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Montenegro', 'Netherlands',
          'Norway', 'Poland', 'Portugal', 'Romania', 'Russian Federation', 'San Marino', 'Serbia', 'Slovakia', 'Spain',
          'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom']
Africa = ['Cabo Verde', 'Mauritius', 'Seychelles', 'South Africa']
Oceania = ['Australia', 'Fiji', 'Kiribati', 'New Zealand']

# make a function to indicate country to continent
def GetConti(country):
    if country in Asia:
        return "Asia"
    elif country in America:
        return "America"
    elif country in Europe:
        return "Europe"
    elif country in Africa:
        return "Africa"
    else:
        return "Oceania"

df['continent'] = df['country'].apply(lambda x: GetConti(x))

# rename the column with space and symbol in their name
df.rename(columns={'suicides/100k pop': 'suicides100k'}, inplace=True)

# make multiple lineplots with seaborn
sns.relplot(x="year", y="suicides100k", hue="sex", col="continent", col_wrap=3, ci=None, kind="line", data=df)

# make a copy of df
df1 = df.copy()
# remove data at year 2016
df1 = df[df.year != 2016]

# Global suicides100k over time 1985 -2015
a5 = df1.groupby(['year']).suicides_no.sum()
b5 = df1.groupby(['year']).population.sum()
c5 = ( a5 / b5 ) * 100000
c5 = pd.DataFrame(c5)
c5 = c5.reset_index()
c5.rename(columns={0: 'suicides100k'}, inplace=True)
f, ax = plt.subplots(figsize=(10, 7))
year_suicides = sns.lineplot(x="year", y='suicides100k', markers=True, data=c5).set_title(
    'Global Suicides (per 100k) \n Trend over time, 1985 - 2015.', x=0.2, fontsize=15)
plt.ylim(11.3, 15.5)
ax.set_xticks([1985, 1987, 1989, 1991, 1993, 1995, 1997, 1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015])

# Want to make a stackplot to find out which continent affect the suicide rate?
# stack? bar? area? seaborn? matplotlib? dataframe
a6 = df1.groupby(['continent', 'year']).suicides_no.sum()
b6 = df1.groupby(['continent', 'year']).population.sum()
c6 = ( a6 / b6 ) * 100000
c6 = pd.DataFrame(c6)
c6 = c6.reset_index()
c6.rename(columns={0: 'suicides100k'}, inplace=True)

f, ax = plt.subplots(figsize=(10, 7))
year_suicides = sns.lineplot(x="year", y='suicides100k', hue='continent', markers=True, data=c6)
ax.set_xticks([1985, 1987, 1989, 1991, 1993, 1995, 1997, 1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015])

# suicides_no over continent, barplot
import numpy as np
a = df.groupby(['continent']).suicides_no.sum()
b = df.groupby('continent').population.sum()
c = ( a / b ) * 100000
f, ax = plt.subplots(figsize=(7, 10))
c.sort_values().plot.bar()

# suicides100k over time by continent, lineplot
'''
Another approach by seaborn:
a1 = df1.groupby(['continent', 'year']).suicides_no.sum()
b1 = df1.groupby(['continent', 'year']).population.sum()
c1 = ( a1 / b1 ) * 100000
c1 = pd.DataFrame(c1)
c1 = c1.reset_index()
c1.rename(columns={0: 'suicides100k'}, inplace=True)
plt.rcParams['figure.figsize']=(10,2)
continent_suicide = sns.relplot(x='year', y='suicides100k', col='continent', kind='line', col_wrap=1, data=df1)
ax.set_xticks([1985, 1990, 1995, 2000, 2005, 2010, 2015])
'''
from ggplot import *

a1 = df1.groupby(['continent', 'year']).suicides_no.sum()
b1 = df1.groupby(['continent', 'year']).population.sum()
c1 = ( a1 / b1 ) * 100000
c1 = pd.DataFrame(c1)
c1 = c1.reset_index()
c1.rename(columns={0: 'suicides100k'}, inplace=True)
p = ggplot(aes(x='year', y='suicides100k', color='continent'), data=c1)
p + facet_grid('continent') + geom_line() + geom_point() + labs(title = "Trends Over Time, by Continent", 
                                      x = "Year",
                                      y = "Suicides per 100k")
                                      
a2 = df.groupby(['sex']).suicides_no.sum()
b2 = df.groupby(['sex']).population.sum()
c2 = ( a2 / b2 ) * 100000
c2.plot.bar()
plt.xticks(rotation=360)
plt.title('Global suicides (per 100k), by Sex')

a3 = df1.groupby(['sex', 'year']).suicides_no.sum()
b3 = df1.groupby(['sex', 'year']).population.sum()
c3 = ( a3 / b3 ) * 100000
c3 = pd.DataFrame(c3)
c3 = c3.reset_index()
c3.rename(columns={0: 'suicides100k'}, inplace=True)
'''
sns.relplot(x='year', y='suicides100k', col='sex', col_wrap=3, kind='line', data=df1)
'''

p2 = ggplot(aes(x='year', y='suicides100k', color='sex'), data=c3) + \
geom_line() + \
geom_point() + \
ggtitle('Trends Over Time, by Sex') + \
xlab("Year") + \
ylab("Suicides per 100k")

p2 + facet_grid('sex', scales='free')
# How to adjust the position of the title?

a7 = df.groupby(['age']).suicides_no.sum()
b7 = df.groupby(['age']).population.sum()
c7 = ( a7 / b7 ) * 100000
f, ax = plt.subplots(figsize=(7, 10))
c7.sort_values().plot.bar()
plt.xticks(rotation=360)
plt.title('Global suicides (per 100k), by Age')

a8 = df1.groupby(['age', 'year']).suicides_no.sum()
b8 = df1.groupby(['age', 'year']).population.sum()
c8 = ( a8 / b8 ) * 100000
c8 = pd.DataFrame(c8)
c8 = c8.reset_index()
c8.rename(columns={0: 'suicides100k'}, inplace=True)
'''
sns.relplot(x='year', y='suicides100k', col='sex', col_wrap=3, kind='line', data=df1)
'''

p2 = ggplot(aes(x='year', y='suicides100k', color='age'), data=c8) + \
geom_line() + \
geom_point() + \
ggtitle('Trends Over Time, by Age') + \
xlab("Year") + \
ylab("Suicides per 100k")

p2 + facet_grid('age', scales='free')
# How to adjust the position of the title?

c4 = c3[c3.sex == 'female']
sns.lineplot(x='year', y='suicides100k', data=c4)

'''
ggplot(aes(x = 'country', y = 'suicides100k', fill = 'continent'), data = c4) + \
geom_bar(stat = 'identity')
'''
f, ax = plt.subplots(figsize=(6, 15))
a4 = df.groupby(['country', 'continent']).suicides_no.sum()
b4 = df.groupby(['country', 'continent']).population.sum()
c4 = ( a4 / b4 ) * 100000
c4 = pd.DataFrame(c4)
c4 = c4.reset_index()
c4.rename(columns={0: 'suicides100k'}, inplace=True)
c4 = c4.sort_values(by=['suicides100k'], ascending=False)

ax = sns.barplot(x='suicides100k', y='country', color='b', data=c4)
ax.set_xlabel('suicides100k')

ggplot(aes(x = 'country', y = 'suicides100k', fill = 'continent'), data = c4) + \
geom_bar() + \
coord_flip() + \
labs(title = "Global suicides per 100k, by Country",
     x = "Suicides per 100k",
     y = "Country")
     
q = ggplot(c4, aes('suicides100k', 'country', fill = 'continent')) + geom_point()
q
