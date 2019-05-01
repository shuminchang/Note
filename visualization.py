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
