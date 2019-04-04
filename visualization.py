# https://www.kaggle.com/residentmario/univariate-plotting-with-pandas/
# single-variable (univariate) visualization
# nominal categories, ordinal categories
# bar plot - for less categories, for ordering categories, a bar for a single value
# line plot - for more categories, not suitable for nominal categories, does not mean much for the order
# if the data can fit into a bar chart, use a bar chart.
# The interpretation of the data is more important than the tool that you use
# histogram - for interval data with skew, a bar for a range of values
# skewed data
# nominal or ordinal, large or small, interval or not, skewed or not - then decide which chart you use

reviews['province'].value_counts().head(10).plot.bar()
(reviews['province'].value_counts().head(10) / len(reviews)).plot.bar()
reviews['points'].value_counts().sort_index().plot.bar()
reviews['points'].value_counts().sort_index().plot.line()
review['points'].value_counts().sort_index().plot.area()
reviews[reviews['price'] < 200]['price'].plot.hist()
reviews['price'].plot.hist()
reviews['points'].plot.hist()

# downsample, weakly correlated
# scatter plot - weak to overplotting, work better with small datasets
