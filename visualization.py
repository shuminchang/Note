# https://www.kaggle.com/residentmario/univariate-plotting-with-pandas/
# pandas built-in plotting tools
# single-variable (univariate) visualization
# nominal categories, ordinal categories
# bar plot - for less categories, for ordering categories, a bar for a single value
# line plot - for more categories, not suitable for nominal categories, does not mean much for the order
# if the data can fit into a bar chart, use a bar chart.
# The interpretation of the data is more important than the tool that you use
# histogram - for interval data with skew, a bar for a range of values
# skewed data
# nominal or ordinal, large or small, interval or not, skewed or not - then decide which chart you use

# pandas built-in tools
# bar chart - order: high count to low count
reviews['province'].value_counts().head(10).plot.bar()
# bar chart -  ratio
(reviews['province'].value_counts().head(10) / len(reviews)).plot.bar()
# bar chart - sorted(ex. young age to old age)
reviews['points'].value_counts().sort_index().plot.bar()
# line chart
reviews['points'].value_counts().sort_index().plot.line()
# area chart
review['points'].value_counts().sort_index().plot.area()
# histogram - within a range(< 200)
reviews[reviews['price'] < 200]['price'].plot.hist()
reviews['price'].plot.hist()
reviews['points'].plot.hist()

# downsample, weakly correlated, overplotting
# scatter plot - weak to overplotting, work better with small datasets
reviews[reviews['price'] < 100].sample(100).plot.scatter(x='price', y='points')
# Hexplot
reviews[reviews['price'] < 100].plot.hexbin(x='price', y='points', gridsize=15)
# gidesize is for resolution of Hexplot, small number: blurry, large number: sharp
# missing x-axis is a bug
# Stacked plots
wine_counts.plot.bar(stacked=True)  
# Area plots
wine_counts.plot.area()
# Can't work with too many variable, five sets are interpretable
# Hard to distinguish concrete values
# Bivariate line chart
wine_counts.plot.line()
# more interpretable than stacked plots and area plots

# ordinal categorical data, interval data, nominal categorical data
# outlier, in-betweener

# However, it's a worse choice for ordinal categorical data.
# A KDE plot expects that if there are 200 wine rated 85 and 400 rated 86, then the values in between, like 85.5, should smooth out to somewhere in between (say, 300). 

# However, if the value in between can't occur (wine ratings of 85.5 are not allowed), then the KDE plot is fitting to something that doesn't exist. 
# In these cases, use a line chart instead.

# record-oriented format, tidy format
# pandas plotting tools - for initial explorations
# seaborn - for more sophisticated explorations

# seaborn
# Countplot - like bar plot
sns.countplot(reviews['points'])
# Kernel density estimate(KDE) plot - line plot with outlier
sns.kdeplot(reviews.query('price < 200').price)
# 2D KDE plot
sns.kdeplot(reviews[reviews['price'] < 200].loc[:, ['price', 'points']].dropna().sample(5000))
# Distplot - histogram with KDE closed
sns.distplot(reviews['points'], bins=10, kde=False)
# Scatterplot + hexplot
sns.jointplot(x='price', y='points', data=reviews[reviews['price'] < 100])
# Scatterplot + hexplot, Scatterplot as hex form
sns.jointplot(x='price', y='points', data=reviews[reviews['price'] < 100], kind='hex', 
              gridsize=20)
# Boxplot
df = reviews[reviews.variety.isin(reviews.variety.value_counts().head(5).index)]
sns.boxplot(x='variety', y='points', data=df)
# Violinplot
df = reviews[reviews.variety.isin(reviews.variety.value_counts().head(5).index)]
sns.violinplot(x='variety', y='points', data=reviews[reviews.variety.isin(reviews.variety.value_counts()[:5].index)])

# FacetGrid
df = footballers[footballers['Position'].isin(['RW', 'LW', 'GK'])]  # select 'RW', 'LW', 'GK' in 'Position' for the first row, each for a column
df = footballers[footballers['Club'].isin(['Real Madrid CF', 'FC Barcelona', 'Atlético Madrid'])] # select for the second row
g = sns.FacetGrid(df, col="Position")  # create FacetGrid
g.map(sns.kdeplot, "Overall")  # make a kdeplot on the FacetGrid, x axis = 'Overall'

g = sns.FacetGrid(df, col="Position", col_wrap=5)  # display 5 column per row

g = sns.FacetGrid(df, row="Position", col="Club", 
                  row_order=['GK', 'ST'],
                  col_order=['Atlético Madrid', 'FC Barcelona', 'Real Madrid CF'])  # ordering the row and column
g.map(sns.violinplot, "Overall")

# Pairplot
sns.pairplot(footballers[['Overall', 'Potential', 'Value']])

# Multivariate scatter plots, markers for shape, hue for color
sns.lmplot(x='Value', y='Overall', markers=['o', 'x', '*'], hue='Position',
           data=footballers.loc[footballers['Position'].isin(['ST', 'RW', 'LW'])],
           fit_reg=False
          )
# Grouped box plot
f = (footballers
         .loc[footballers['Position'].isin(['ST', 'GK'])]
         .loc[:, ['Value', 'Overall', 'Aggression', 'Position']]
    )
f = f[f["Overall"] >= 80]
f = f[f["Overall"] < 85]  # 80 <= f < 85
f['Aggression'] = f['Aggression'].astype(float)  # ？

sns.boxplot(x="Overall", y="Aggression", hue='Position', data=f)

# Heatmap
f = (
    footballers.loc[:, ['Acceleration', 'Aggression', 'Agility', 'Balance', 'Ball control']]
        .applymap(lambda v: int(v) if str.isdecimal(v) else np.nan)
        .dropna()
).corr()

sns.heatmap(f, annot=True) # 'annot' for showing numbers inside the squares

# Parallel Coordinates
from pandas.plotting import parallel_coordinates

f = (
    footballers.iloc[:, 12:17]
        .loc[footballers['Position'].isin(['ST', 'GK'])]
        .applymap(lambda v: int(v) if str.isdecimal(v) else np.nan)
        .dropna()
)
f['Position'] = footballers['Position']
f = f.sample(200)

parallel_coordinates(f, 'Position')

# Plotnine
from plotnine import *

df = top_wines.head(1000).dropna()

(ggplot(df) # passing the data as a parameter
 + aes(color='points')  # add colors
 + aes('points', 'price')  # add the variables of interest in aes(aesthetic)
 + geom_point()  # specify the plot type
 + stat_smooth()  # add a regression line
 + facet_wrap('~variety')  # facet with 'variety'. Why '~' ?
 )  
  
(ggplot(df)
 + geom_point(aes('points', 'price'))
)

(ggplot(df, aes('points', 'price'))
 + geom_point()
)

(ggplot(top_wines)
     + aes('points')
     + geom_bar()
)

(ggplot(top_wines)
     + aes('points', 'variety')
     + geom_bin2d(bins=20)
)

(ggplot(top_wines)
         + aes('points', 'variety')
         + geom_bin2d(bins=20)
         + coord_fixed(ratio=1)
         + ggtitle("Top Five Most Common Wine Variety Points Awarded")
)

# Time-series plotting
shelter_outcomes['date_of_birth'].value_counts().sort_values().plot.line() 
shelter_outcomes['date_of_birth'].value_counts().resample('Y').sum().plot.line() # resample as 'year'
stocks['volume'].resample('Y').mean().plot.bar()

# Lag plot
from pandas.plotting import lag_plot
lag_plot(stocks['volume'].tail(250))  # correlation with t and t+1

# Autocorrelation plot
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(stocks['volume'])



