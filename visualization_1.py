import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

path = "../jwo/wejfoe.csv"
data = pd.read_csv(data, index_col="Date", parse_dates=True)
data.head()
data.tail()

sns.lineplot(data=data)
plt.figure(figsize=(14,6)
plt.title("Daily Global Steams of Popular Songs in 2017-2018")
sns.lineplot(data=data)
sns.lineplot(data=data['xxx'], label='xxx')
plt.xlabel("Date")
list(data.columns)
sns.barplot(x=data.index, y=data['column']) # exchange x and y if the label is too crowd
plt.ylabel("Arrival delay (in minutes)")
sns.heatmap(data=flight_data, annot=True) # annot=True, ensures the values for each cell appear on the chart
# scatter plot without regression line, hue=color
sns.scatterplot(x=insurance_date['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
# scatter plot with regression line
sns.regplot(x=insurance_date['bmi'], y=insurance_data['charges'])
# catter plot with multi-regression line, based on 'hue'
sns.lmplot(x='bmi', y='charges', hue='smoker', data=insurance_data)
# categorical scatter plot
sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])
# Histogram
sns.distplot(a=iris_data['Petal Length (cm)'], kde=False)
# KDE plot
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)
# 2D KDE plot
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")
# Histograms for each species
sns.distplot(a=iris_set_data['Petal Length (cm)'], label="Iris-setosa", kde=False)
sns.distplot(a=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", kde=False)
sns.distplot(a=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", kde=False)
# Force legend to appear
plt.legend()
# KDE plots for each species
sns.kdeplot(data=iris_set_data['Petal Length (cm)'], label="Iris-setosa", shade=True)
sns.kdeplot(data=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", shade=True)
sns.kdeplot(data=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", shade=True)
