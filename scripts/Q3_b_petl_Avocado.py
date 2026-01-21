#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 01:18:11 2024

@author: sijimathew
"""


import sqlite3
import petl as etl
import altair as alt
import numpy as np
alt.renderers.enable('png') #The visualization is saved as a static PNG file (chart.png) instead of being rendered interactively in the notebook or browser.
# SQLite database file
db_file = 'avocado.db'
table_name = 'avocado_data'


url = 'avocado.csv'
# Create a SQLite database connection
conn = sqlite3.connect(db_file)

# Load data from CSV and write it to SQLite3 database

avocado_data = etl.fromcsv(url)
print("Original Headers:", etl.header(avocado_data))

new_headers = [(header if header != '' else 'Unnamed') for header in etl.header(avocado_data)]
# list called new_headers where any empty headers have been replaced by 'Unnamed'.
data_fixed = etl.rename(avocado_data, dict(zip(etl.header(avocado_data), new_headers)))
#Combines the original headers and the new headers into pairs using the zip function.
print("Fixed Headers:", etl.header(data_fixed))

#Write the fixed updated data to the sqlite3 database
etl.todb(data_fixed, conn, table_name, create=True, sample=1000)
print("Data written to SQLite3 database.")

#Write the code for Question 1(a) using pETL

#1.	.Read the data from the CSV file into a DataFrame.
print(etl.head(data_fixed))

#2.	Display type, memory consumption, and null count information
headers = etl.header(data_fixed)

print("------Column Types-----------")
for column in headers: #looping is happening
    column_data = etl.cut(data_fixed, column) #
    first_value = next(iter(column_data), None)
    print(f"Column: {column}")
    print(f"Type: {type(first_value)}")  # Check the type of the first element
    print("-" * 50)

print("------Null Values-----------")
for column in headers:
    column_data = etl.cut(data_fixed, column)
    null_count = sum(1 for value in column_data if value is None)
    print(f"Column: {column} - Null Count: {null_count}") #Prints the data type of the first value in the column.

print("------memory consumption-----------")
for column in headers:
    column_data = etl.cut(data_fixed, column)
    total_size = sum(len(str(value)) for value in column_data)
    print(f"Column: {column} - Estimated Memory Size (in characters): {total_size}")

#3.	Display the number of unique values in each column.
print("------Unique Values-----------")
for column in headers:
    column_data = etl.cut(data_fixed, column)
    unique_values = set(column_data)  # Convert the column data to a set to get unique values by removing duplicates
    print(f"Column: {column} - Unique Values Count: {len(unique_values)}")
    
#4.	Display the first and last five rows and the first and last four columns of data.
first_four_columns = etl.cutout(data_fixed, *etl.header(data_fixed)[4:])  # Get first 4 columns
last_four_columns = etl.cutout(data_fixed, *etl.header(data_fixed)[:-4])  # Get last 4 columns

print("First 4 columns:")
print(etl.head(first_four_columns, 5))

print("Last 4 columns:")
print(etl.head(last_four_columns, 5))

#5.	Choose any three columns, access them with bracket notation, and display the first five rows of this data.

columns_of_interest = etl.cut(data_fixed, 'type', 'year', 'region')
print("First 5 rows of chosen columns:")
print(etl.head(columns_of_interest, 5))

#6.	Select one column and access it with dot notation.

type_column = etl.cut(data_fixed, 'region')
print("First 5 rows of the 'type' column:")
print(etl.head(type_column, 5))

#7.	Multiply the Total Volume and AveragePrice columns, and store the result in a new column called EstimatedRevenue.  Then, display the first five rows of this data to confirm that the column was added and has the correct values.
print("Estimated Revenue =  Total Volume * AveragePrice")
data_with_revenue = etl.addfield(data_fixed, 'EstimatedRevenue', 
                                 lambda row: float(row['Total Volume']) * float(row['AveragePrice']) if row['Total Volume'] and row['AveragePrice'] else None)
#lambda row:: This defines an anonymous (inline) function that takes a row of the dataset as input. Each row represents a single record or entry in the dataset
print("First 5 rows with EstimatedRevenue:")
data_with_revenue_es = etl.cut(data_with_revenue, 'Total Volume', 'AveragePrice', 'EstimatedRevenue')
print(etl.head(data_with_revenue_es, 5))

#8.	Create a DataFrame that’s grouped by region and type and that includes the average price for the grouped columns.  Then, reset the index and display the first five rows.
def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return None 

data_fixed = etl.convert(data_fixed, 'AveragePrice', safe_float)
grouped_data = etl.aggregate(data_fixed, key=['region', 'type'], aggregation={'AveragePrice': lambda rows: sum(row['AveragePrice'] for row in rows if row['AveragePrice'] is not None) / len([row for row in rows if row['AveragePrice'] is not None])})
reset_data = etl.cutout(grouped_data, 'region', 'type')
print("First 5 rows of the grouped and reset data:")
print(etl.head(reset_data, 5))


#9.	Create a bar plot that shows the mean, median, and standard deviation of the Total Volume column by year.
data = etl.convert(avocado_data, 'Total Volume', float)

# Custom functions to calculate mean, median, and std
def calc_mean(rows):
    return np.mean([row['Total Volume'] for row in rows])

def calc_median(rows):
    return np.median([row['Total Volume'] for row in rows])

def calc_std(rows):
    return np.std([row['Total Volume'] for row in rows])

# Group by 'year' and aggregate: mean, median, and std for 'Total Volume'
grouped_data = etl.aggregate(data, key='year', aggregation={
    'Total Volume_mean': calc_mean,
    'Total Volume_median': calc_median,
    'Total Volume_std': calc_std
})

# Convert the PETL table to a Pandas DataFrame
df = etl.todataframe(grouped_data)

# Melt the DataFrame for use in Altair
melted_df = df.melt(id_vars='year', value_vars=['Total Volume_mean', 'Total Volume_median', 'Total Volume_std'],
                    var_name='Statistic', value_name='Total Volume')
#This function reshapes the DataFrame so that the statistical columns
#
# Create a bar plot with Altair
chart = alt.Chart(melted_df).mark_bar().encode(
    x='year:N',  # 'O' stands for ordinal (discrete data)
    y='Total Volume:Q',  # 'Q' stands for quantitative (continuous data)
    color='Statistic:N',  # 'N' for nominal (categorical data)
    column='Statistic:N'  # Create separate plots for mean, median, and std dev
).properties(
    title='Total Volume by Year (Mean, Median, and Std Dev)'
)
chart.show()



