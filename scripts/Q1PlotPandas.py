#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 20:13:12 2024

@author: sijimathew
"""

import pandas as pd

#Read the data from the CSV file into a DataFrame and display the first five rows.

print("Read the data from the CSV file into a DataFrame and sisplay the first five rows")
print()
avocado_data = pd.read_csv('avocado.csv')
print(avocado_data.head())

# Save the DataFrame to a pickle file named avocado_data.pkl
avocado_data.to_pickle('avacado_data.pkl')
avocado_data = pd.read_pickle('avocado_data.pkl')

#Create a new DataFrame that contains the total of the Small Bags, Large Bags, and XLarge Bags columns grouped by type
bags_sum_by_type = avocado_data.groupby('type')[['Small Bags', 'Large Bags', 'XLarge Bags']].sum()
# then display the DataFrame.
print("Display the new DataFrame")
print()
print(bags_sum_by_type)


#Use the grouped data to create a bar plot that shows the number of small, large, and extra-large bags for both types of avocado.
bags_sum_by_type.groupby('type')[['Small Bags', 'Large Bags', 'XLarge Bags']].sum().plot(kind='bar')


#Use the original data to create a scatter plot for the Total Volume and AveragePrice columns.
avocado_data.plot.scatter(x='Total Volume', y='AveragePrice', title='Total Volume vs Average Price')
