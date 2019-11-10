{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dataset: Suicide Rates Overview 1985 to 2016\n",
    "# Reference: https://www.kaggle.com/lmorgan95/r-suicide-rates-in-depth-stats-insights\n",
    "\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# read csv file\n",
    "df = pd.read_csv('D:\\coding\\data\\master.csv')\n",
    "\n",
    "# rename the column with space and symbols\n",
    "df.rename(columns={' gdp_for_year ($) ': 'gdp_for_year'}, inplace=True)\n",
    "df.rename(columns={'gdp_per_capita ($)': 'gdp_per_capita'}, inplace=True)\n",
    "df.rename(columns={'suicides/100k pop': 'suicides100k'}, inplace=True)\n",
    "\n",
    "# remove ',' from gdp_for_year\n",
    "df['gdp_for_year'] = [ i.replace(\",\", \"\") for i in df['gdp_for_year'] ]\n",
    "\n",
    "# create lists of continents\n",
    "Asia = ['Armenia', 'Azerbaijan', 'Bahrain', 'Israel', 'Japan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Macau', 'Maldives',\n",
    "        'Mongolia', 'Oman', 'Philippines', 'Qatar', 'Republic of Korea', 'Singapore', 'Sri Lanka', 'Thailand', 'Turkey',\n",
    "        'Turkmenistan', 'United Arab Emirates', 'Uzbekistan']\n",
    "America = ['Antigua and Barbuda', 'Argentina', 'Aruba', 'Bahamas', 'Barbados', 'Belize', 'Brazil', 'Canada', 'Chile',\n",
    "           'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'Ecuador', 'El Salvador', 'Grenada', 'Guatemala', 'Guyana',\n",
    "           'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Puerto Rico', 'Saint Kitts and Nevis', 'Saint Lucia',\n",
    "           'Saint Vincent and Grenadines', 'Suriname', 'Trinidad and Tobago', 'United States', 'Uruguay']\n",
    "Europe = ['Albania', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus',\n",
    "          'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary',\n",
    "          'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Montenegro', 'Netherlands',\n",
    "          'Norway', 'Poland', 'Portugal', 'Romania', 'Russian Federation', 'San Marino', 'Serbia', 'Slovakia', 'Spain',\n",
    "          'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom']\n",
    "Africa = ['Cabo Verde', 'Mauritius', 'Seychelles', 'South Africa']\n",
    "Oceania = ['Australia', 'Fiji', 'Kiribati', 'New Zealand']\n",
    "\n",
    "# make a function to indicate country to continent\n",
    "def GetConti(country):\n",
    "    if country in Asia:\n",
    "        return \"Asia\"\n",
    "    elif country in America:\n",
    "        return \"America\"\n",
    "    elif country in Europe:\n",
    "        return \"Europe\"\n",
    "    elif country in Africa:\n",
    "        return \"Africa\"\n",
    "    else:\n",
    "        return \"Oceania\"\n",
    "\n",
    "df['continent'] = df['country'].apply(lambda x: GetConti(x))\n",
    "\n",
    "# rename the column with space and symbol in their name\n",
    "df.rename(columns={'suicides/100k pop': 'suicides100k'}, inplace=True)\n",
    "\n",
    "# make multiple lineplots with seaborn\n",
    "sns.relplot(x=\"year\", y=\"suicides100k\", hue=\"sex\", col=\"continent\", col_wrap=3, ci=None, kind=\"line\", data=df)\n",
    "\n",
    "# make a copy of df\n",
    "df1 = df.copy()\n",
    "# remove data at year 2016\n",
    "df1 = df[df.year != 2016]\n",
    "\n",
    "# Global suicides100k over time 1985 -2015\n",
    "a5 = df1.groupby(['year']).suicides_no.sum()\n",
    "b5 = df1.groupby(['year']).population.sum()\n",
    "c5 = ( a5 / b5 ) * 100000\n",
    "c5 = pd.DataFrame(c5)\n",
    "c5 = c5.reset_index()\n",
    "c5.rename(columns={0: 'suicides100k'}, inplace=True)\n",
    "f, ax = plt.subplots(figsize=(10, 7))\n",
    "year_suicides = sns.lineplot(x=\"year\", y='suicides100k', markers=True, data=c5).set_title(\n",
    "    'Global Suicides (per 100k) \\n Trend over time, 1985 - 2015.', x=0.2, fontsize=15)\n",
    "plt.ylim(11.3, 15.5)\n",
    "ax.set_xticks([1985, 1987, 1989, 1991, 1993, 1995, 1997, 1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015])\n",
    "\n",
    "# Want to make a stackplot to find out which continent affect the suicide rate?\n",
    "# stack? bar? area? seaborn? matplotlib? dataframe\n",
    "a6 = df1.groupby(['continent', 'year']).suicides_no.sum()\n",
    "b6 = df1.groupby(['continent', 'year']).population.sum()\n",
    "c6 = ( a6 / b6 ) * 100000\n",
    "c6 = pd.DataFrame(c6)\n",
    "c6 = c6.reset_index()\n",
    "c6.rename(columns={0: 'suicides100k'}, inplace=True)\n",
    "\n",
    "f, ax = plt.subplots(figsize=(10, 7))\n",
    "year_suicides = sns.lineplot(x=\"year\", y='suicides100k', hue='continent', markers=True, data=c6)\n",
    "ax.set_xticks([1985, 1987, 1989, 1991, 1993, 1995, 1997, 1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015])\n",
    "\n",
    "# suicides_no over continent, barplot\n",
    "import numpy as np\n",
    "a = df.groupby(['continent']).suicides_no.sum()\n",
    "b = df.groupby('continent').population.sum()\n",
    "c = ( a / b ) * 100000\n",
    "f, ax = plt.subplots(figsize=(7, 10))\n",
    "c.sort_values().plot.bar()\n",
    "\n",
    "# suicides100k over time by continent, lineplot\n",
    "'''\n",
    "Another approach by seaborn:\n",
    "a1 = df1.groupby(['continent', 'year']).suicides_no.sum()\n",
    "b1 = df1.groupby(['continent', 'year']).population.sum()\n",
    "c1 = ( a1 / b1 ) * 100000\n",
    "c1 = pd.DataFrame(c1)\n",
    "c1 = c1.reset_index()\n",
    "c1.rename(columns={0: 'suicides100k'}, inplace=True)\n",
    "plt.rcParams['figure.figsize']=(10,2)\n",
    "continent_suicide = sns.relplot(x='year', y='suicides100k', col='continent', kind='line', col_wrap=1, data=df1)\n",
    "ax.set_xticks([1985, 1990, 1995, 2000, 2005, 2010, 2015])\n",
    "'''\n",
    "from ggplot import *\n",
    "\n",
    "a1 = df1.groupby(['continent', 'year']).suicides_no.sum()\n",
    "b1 = df1.groupby(['continent', 'year']).population.sum()\n",
    "c1 = ( a1 / b1 ) * 100000\n",
    "c1 = pd.DataFrame(c1)\n",
    "c1 = c1.reset_index()\n",
    "c1.rename(columns={0: 'suicides100k'}, inplace=True)\n",
    "p = ggplot(aes(x='year', y='suicides100k', color='continent'), data=c1)\n",
    "p + facet_grid('continent') + geom_line() + geom_point() + labs(title = \"Trends Over Time, by Continent\", \n",
    "                                      x = \"Year\",\n",
    "                                      y = \"Suicides per 100k\")\n",
    "                                      \n",
    "a2 = df.groupby(['sex']).suicides_no.sum()\n",
    "b2 = df.groupby(['sex']).population.sum()\n",
    "c2 = ( a2 / b2 ) * 100000\n",
    "c2.plot.bar()\n",
    "plt.xticks(rotation=360)\n",
    "plt.title('Global suicides (per 100k), by Sex')\n",
    "\n",
    "a3 = df1.groupby(['sex', 'year']).suicides_no.sum()\n",
    "b3 = df1.groupby(['sex', 'year']).population.sum()\n",
    "c3 = ( a3 / b3 ) * 100000\n",
    "c3 = pd.DataFrame(c3)\n",
    "c3 = c3.reset_index()\n",
    "c3.rename(columns={0: 'suicides100k'}, inplace=True)\n",
    "'''\n",
    "sns.relplot(x='year', y='suicides100k', col='sex', col_wrap=3, kind='line', data=df1)\n",
    "'''\n",
    "\n",
    "p2 = ggplot(aes(x='year', y='suicides100k', color='sex'), data=c3) + \\\n",
    "geom_line() + \\\n",
    "geom_point() + \\\n",
    "ggtitle('Trends Over Time, by Sex') + \\\n",
    "xlab(\"Year\") + \\\n",
    "ylab(\"Suicides per 100k\")\n",
    "\n",
    "p2 + facet_grid('sex', scales='free')\n",
    "# How to adjust the position of the title?\n",
    "\n",
    "a7 = df.groupby(['age']).suicides_no.sum()\n",
    "b7 = df.groupby(['age']).population.sum()\n",
    "c7 = ( a7 / b7 ) * 100000\n",
    "f, ax = plt.subplots(figsize=(7, 10))\n",
    "c7.sort_values().plot.bar()\n",
    "plt.xticks(rotation=360)\n",
    "plt.title('Global suicides (per 100k), by Age')\n",
    "\n",
    "a8 = df1.groupby(['age', 'year']).suicides_no.sum()\n",
    "b8 = df1.groupby(['age', 'year']).population.sum()\n",
    "c8 = ( a8 / b8 ) * 100000\n",
    "c8 = pd.DataFrame(c8)\n",
    "c8 = c8.reset_index()\n",
    "c8.rename(columns={0: 'suicides100k'}, inplace=True)\n",
    "'''\n",
    "sns.relplot(x='year', y='suicides100k', col='sex', col_wrap=3, kind='line', data=df1)\n",
    "'''\n",
    "\n",
    "p2 = ggplot(aes(x='year', y='suicides100k', color='age'), data=c8) + \\\n",
    "geom_line() + \\\n",
    "geom_point() + \\\n",
    "ggtitle('Trends Over Time, by Age') + \\\n",
    "xlab(\"Year\") + \\\n",
    "ylab(\"Suicides per 100k\")\n",
    "\n",
    "p2 + facet_grid('age', scales='free')\n",
    "# How to adjust the position of the title?\n",
    "\n",
    "c4 = c3[c3.sex == 'female']\n",
    "sns.lineplot(x='year', y='suicides100k', data=c4)\n",
    "\n",
    "'''\n",
    "ggplot(aes(x = 'country', y = 'suicides100k', fill = 'continent'), data = c4) + \\\n",
    "geom_bar(stat = 'identity')\n",
    "'''\n",
    "f, ax = plt.subplots(figsize=(6, 15))\n",
    "a4 = df.groupby(['country', 'continent']).suicides_no.sum()\n",
    "b4 = df.groupby(['country', 'continent']).population.sum()\n",
    "c4 = ( a4 / b4 ) * 100000\n",
    "c4 = pd.DataFrame(c4)\n",
    "c4 = c4.reset_index()\n",
    "c4.rename(columns={0: 'suicides100k'}, inplace=True)\n",
    "c4 = c4.sort_values(by=['suicides100k'], ascending=False)\n",
    "\n",
    "ax = sns.barplot(x='suicides100k', y='country', color='b', data=c4)\n",
    "ax.set_xlabel('suicides100k')\n",
    "\n",
    "ggplot(aes(x = 'country', y = 'suicides100k', fill = 'continent'), data = c4) + \\\n",
    "geom_bar() + \\\n",
    "coord_flip() + \\\n",
    "labs(title = \"Global suicides per 100k, by Country\",\n",
    "     x = \"Suicides per 100k\",\n",
    "     y = \"Country\")\n",
    "     \n",
    "q = ggplot(c4, aes('suicides100k', 'country', fill = 'continent')) + geom_point()\n",
    "q"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
