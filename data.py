

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# %matplotlib inline

flights = pd.read_csv(r"C:\Users\dell\Documents\flight.CSV")
print(flights.shape)
flights.head()

sb.countplot(data=flights, x='Source')
# plt.xticks(rotation = 30)
plt.ylabel('Number of Flights', fontsize=12)
plt.xlabel('Source', fontsize=12)

base_color = sb.color_palette()[0]
sb.countplot(data=flights, x='Source', color=base_color)
plt.xticks(rotation=30)

base_color = sb.color_palette()[1]
gen_order = flights['Source'].value_counts().index
sb.countplot(data=flights, x='Source', color=base_color, order=gen_order)

base_color = sb.color_palette()[2]
sb.countplot(data=flights, x='Airline', color=base_color)

base_color = sb.color_palette()[2]
sb.countplot(data=flights, x='Airline', color=base_color)
plt.xticks(rotation=90);

base_color = sb.color_palette()[2]
sb.countplot(data=flights, y='Airline', color=base_color)
plt.xticks(rotation=90);

flights.isna().sum()

na_counts = flights.isna().sum()
base_color = sb.color_palette()[0]
sb.barplot(na_counts.index.values, na_counts, color=base_color)
plt.xticks(rotation=90)
plt.ylabel('Number of missing values', fontsize=1299)

sorted_counts = flights['Destination'].value_counts()
plt.pie(sorted_counts, labels=sorted_counts.index, startangle=90, counterclock=False);
plt.axis('square')
plt.title('Flight Destination\'s')

sorted_counts = flights['Destination'].value_counts()
plt.pie(sorted_counts, labels=sorted_counts.index, startangle=90, counterclock=False, wedgeprops={'width': 0.4});
plt.axis('square');

plt.hist(data=flights, x='Duration(minutes)')

plt.hist(data=flights, x='Price', bins=20)

bins = np.arange(0, flights['Price'].max() + 1, 1200)
plt.hist(data=flights, x='Price', bins=bins)
plt.show()

sb.displot(flights['Price']);

sb.displot(flights['Price'], kde=False);

bin_edges = np.arange(0, flights['Price'].max() + 1, 1200)
sb.distplot(flights['Price'], bins=bin_edges, kde=False, hist_kws={'alpha': 1});


