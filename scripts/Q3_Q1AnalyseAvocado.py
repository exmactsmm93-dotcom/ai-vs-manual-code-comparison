#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 18:12:17 2024

@author: sijimathew
"""

import polars as pl
import altair as alt
# Enable Altair's default renderer to display plots
alt.renderers.enable('png')

#1.Read the data from the CSV file into a DataFrame.
print("Read the data from the CSV file into a DataFrame.")
print()

#url = 'https://data.cdc.gov/api/views/v6ab-adf5/rows.csv?accessType=DOWNLOAD'
url = 'avocado.csv'

avocado_data = pl.scan_csv(url)
"""
# Save the DataFrame to a parquet file named avocado_data.parquet
avocado_data.write_parquet('avocado_data.parquet')
avocado_data = pl.read_parquet('avocado_data.parquet')
"""
# 2.Display type, memory consumption, and null count information
print("• Display type, memory consumption, and null count information.")
print("Get more information about a DataFrame")
print()
print(avocado_data.describe()) 

#3.Display the number of unique values in each column
print("Display the number of unique values in each column")

unique_counts = avocado_data.lazy().select(
    [pl.col(col_name).n_unique().alias(f"{col_name}_unique_count") for col_name in avocado_data.collect_schema().names()]
).collect()

print("Unique Counts")
print(unique_counts) 
#4. Display the first and last five rows and the first and last four columns of data

avocado_data_collected = avocado_data.collect()

print("• Display the first and last five rows")
print(avocado_data_collected.head(5))  # First 5 rows
print(avocado_data_collected.tail(5))  # Last 5 rows


print("• Display the first four columns of data.")
print(avocado_data_collected.select(avocado_data_collected.columns[:4]))  # First 4 columns

# Display the last four columns
print("• Display the last four columns of data.")
print(avocado_data_collected.select(avocado_data_collected.columns[-4:]))  # Last 4 columns

#5.	Choose any three columns, access them with bracket notation, and display the first five rows of this data.
print("Select three columns (e.g., 'Date', 'AveragePrice', and 'Total Volume') using select() and display the first five rows of this data")
selected_columns = avocado_data.select(["Date", "AveragePrice", "Total Volume"])
selected_columns_collected = selected_columns.collect()
print(selected_columns_collected.head(5))


#6. Select one column and access it with dot notation.
print("Select one column(AveragePrice) and access it with dot notation.")
average_price_column = avocado_data.select("AveragePrice")
result = average_price_column.collect()
print(result.head(5))

#7.	Multiply the Total Volume and AveragePrice columns, and store the result in a new column called EstimatedRevenue.  Then, display the first five rows of this data to confirm that the column was added and has the correct values.
avocado_data_with_revenue = avocado_data.with_columns(
    (pl.col("Total Volume") * pl.col("AveragePrice")).alias("EstimatedRevenue")
)
selected_columns = avocado_data_with_revenue.select(["Total Volume", "AveragePrice", "EstimatedRevenue"])
result = selected_columns.collect()
print(result.head(5))

#8.	Create a DataFrame that’s grouped by region and type and that includes the average price for the grouped columns.  Then, reset the index and display the first five rows.

print("DataFrame that’s grouped by region and type and that includes the average price for the grouped columns.  Then, reset the index and display the first five rows.")
windowed_data = avocado_data.with_columns(
    pl.col("AveragePrice")
    .mean()
    .over(["region", "type"])  # Window function over 'region' and 'type'
    .alias("AveragePrice_mean")  # Alias for the new column
)

result = windowed_data.collect()
result_dedup = result.unique(subset=["region", "type"])
avocado_data_reset= result_dedup.with_row_index("index")

print(" Display the first 5 rows")
print(avocado_data_reset.head(5))

#9.	Create a bar plot that shows the mean, median, and standard deviation of the Total Volume column by year.

wd_2 = avocado_data.group_by('year').agg([
    pl.col('Total Volume').mean().alias('mean'),
    pl.col('Total Volume').median().alias('median'),
    pl.col('Total Volume').std().alias('std')
])

melted_df = wd_2.melt(id_vars=["year"], variable_name="Statistic", value_name="Value")

stats =melted_df.collect().to_pandas()
print(stats)
chart = alt.Chart(stats).mark_bar().encode(
    x='year:O',
    y='Value:Q',
    color='Statistic:N',
    column='Statistic:N',  
    tooltip=['year', 'Statistic', 'Value']
).properties(
    title='Total Volume Statistics by Year'
).interactive() 

alt.data_transformers.enable("vegafusion")
#a high-performance renderer in Altair that speeds up the transformation and rendering of large datasets.
alt.renderers.enable('png')
chart.show()