#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 18:12:17 2024

@author: sijimathew
"""


import pandas as pd

#Read the data from the CSV file into a DataFrame.
print("Read the data from the CSV file into a DataFrame.")
print()
avocado_data = pd.read_csv('avocado.csv')

# Save the DataFrame to a pickle file named avocado_data.pkl
avocado_data.to_pickle('avocado_data.pkl')
avocado_data = pd.read_pickle('avocado_data.pkl')

#Display type, memory consumption, and null count information using the info() method.
print("•Display type, memory consumption, and null count information using the info() method.")
print("Get more information about a DataFrame")
print()
print(avocado_data.info())  # information about DataFrame

#Display the number of unique values in each column.
print("Display the number of unique values in each column.")
print()
print(avocado_data.nunique())

#Display the first and last five rows and the first and last four columns of data.
print("•Display the first and last five rows ")
print(avocado_data.head() ) # displays the first 5 rows
print(avocado_data.tail())  # displays the last 5 rows
print("•Display the first and last four columns of data.")
print(avocado_data.iloc[:, :4]) # displays the first four columns
print(avocado_data.iloc[:, -4:]) # displays the last four columns

#Choose any three columns, access them with bracket notation, and display the first five rows of this data.
print("Use brackets to access a column")
print()
print(avocado_data[['Date','year','region']].head(5))
print()

#Select one column and access it with dot notation.
print("Accessing one column with dot notation:")
print()
print(avocado_data.AveragePrice.head(5))
print()

#Multiply the Total Volume and AveragePrice columns, and store the result in a new column called EstimatedRevenue.  
avocado_data['EstimatedRevenue'] = avocado_data['Total Volume'] * avocado_data['AveragePrice']
#Then, display the first five rows of this data to confirm that the column was added and has the correct values.
print("First five rows with EstimatedRevenue column:")
print()
print(avocado_data[['Total Volume', 'AveragePrice', 'EstimatedRevenue']].head(5))
print()

#Group by region and type, then calculate the mean of the AveragePrice column
grouped_data = avocado_data.groupby(['region', 'type']).agg({'AveragePrice': 'mean'})

#Reset the index to convert grouped columns back into regular columns
grouped_data = grouped_data.reset_index()

#Display the first five rows
print("Data grouped by region and type with average price:")
print()
print(grouped_data.head(5))
print()

#•	Create a bar plot that shows the mean, median, and standard deviation of the Total Volume column by year.
 
avocado_data.groupby('year')['Total Volume'].agg(['mean', 'median', 'std']).plot(kind= 'bar',
  title='Total Volume Statistics by Year',
  ylabel='Total Volume',
  xlabel='year',
  )


