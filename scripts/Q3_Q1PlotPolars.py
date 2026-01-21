#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 00:00:23 2024

@author: sijimathew
"""
import polars as pl
import altair as alt
alt.renderers.enable('png')

#1.Read the data from the CSV file into a DataFrame.
print("Read the data from the CSV file into a DataFrame.")
print()

#url = 'https://data.cdc.gov/api/views/v6ab-adf5/rows.csv?accessType=DOWNLOAD'
url = 'avocado.csv'

avocado_data = pl.scan_csv(url)

avocado_data_collected = avocado_data.collect()

print("• Display the first and last five rows")
print(avocado_data_collected.head(5))  # First 5 rows
print(avocado_data_collected.tail(5))  # Last 5 rows


#2.	Create a new DataFrame that contains the total of the Small Bags, Large Bags, and XLarge Bags columns grouped by type, then display the DataFrame.

print("New dataframe that contains details of Bags")
Bags_df = avocado_data.collect().group_by('type').agg([pl.col('Small Bags').sum().alias("Small Bags"),
                                   pl.col('Large Bags').sum().alias("Large Bags"),
                                   pl.col('XLarge Bags').sum().alias(("XLarge Bags"))])
print(Bags_df)

#3.	Use the grouped data to create a bar plot that shows the number of small, large, and extra-large bags for both types of avocado.

Bags_pd = Bags_df.to_pandas()
#print(Bags_pd)

melted_data = Bags_pd.melt(id_vars=['type'], value_vars=['Small Bags', 'Large Bags', 'XLarge Bags'],
                        var_name='Bag_Size', value_name='Value')
#print(melted_data)
chart1 = alt.Chart(melted_data).mark_bar().encode(
    x='type:O',
    y='Value:Q',
    color=alt.Color('Bag_Size:N', title='Bag_Size'),
    xOffset=alt.XOffset('Bag_Size:N') 
).properties(title='Mean of Total Volume by Year')

alt.renderers.enable('png')  # Save as PNG image

chart1.show()

#4.	Use the original data to create a scatter plot for the Total Volume and AveragePrice columns.
df_pd2 = avocado_data.collect().to_pandas()
# Enable VegaFusion data transformer
alt.data_transformers.enable("vegafusion")
chart2 = alt.Chart(df_pd2).mark_circle().encode(
    x='Total Volume',
    y='AveragePrice',
).properties(title='Total Volume VS Avearage Price')

chart2.show()


