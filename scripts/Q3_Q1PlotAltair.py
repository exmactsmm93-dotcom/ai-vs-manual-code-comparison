#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 00:13:18 2024

@author: sijimathew
"""

#1.Read the data from the CSV file into a DataFrame and display the first five rows.

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

# Display the first and last five rows
print("• Display the first and last five rows")
print(avocado_data_collected.head(5))  # First 5 rows
print(avocado_data_collected.tail(5))  # Last 5 rows
# 2.	Create the following plot with a Altair specific method.
df_pd2 = avocado_data.collect().to_pandas()
alt.data_transformers.enable("vegafusion")

chart = (
    alt.Chart(df_pd2)
    .mark_circle()
    .encode(
        x=alt.X('AveragePrice:Q', title='Average Price'),
        y=alt.Y(
            'Total Volume:Q',
            title='Total Volume (1e7)',
            axis=alt.Axis(
                format='.1s',  # Short format for large numbers
                labelExpr="datum.value / 1e7 "  # Scale by 1e7
            )
        )
    )
    .properties(title='Average Price vs Total Volume')
)
alt.renderers.enable('png')  # Save as PNG image

chart.show()

#3.	Create the same plot but with the hue parameter set to year and the dots for the total volume ranging in size from 10 to 100.

chart2 = (
    alt.Chart(df_pd2)
    .mark_circle()
    .encode(
        x=alt.X('AveragePrice:Q', title='Average Price'),
        y=alt.Y(
            'Total Volume:Q',
            title='Total Volume (1e7)',
            axis=alt.Axis(
                format='.1s',  # Short format for large numbers
                labelExpr="datum.value / 1e7"  # Scale by 1e7
            )
        ),
        color=alt.Color('year:O', title='Year', scale=alt.Scale(range=['#f4a300', '#ff6347', '#4682b4', '#32cd32', '#8a2be2'])),  # Custom shades for each year
        size=alt.Size(
            'Total Volume:Q',
            scale=alt.Scale(domain=[df_pd2['Total Volume'].min(), df_pd2['Total Volume'].max()], range=[10, 100]),
            title='Volume Size'
        )
    )
    .properties(
        title='Average Price vs Total Volume (Scaled by 1e7) with Year Hue and Volume Size'
    )
)

chart2.show()

#4. Create box plot
# Filter data for year and region
filtered_data = avocado_data.filter(
    (pl.col('year').is_between(2015, 2018)) &
    (pl.col('region').is_in(["TotalUS", "West", "WestTexNewMexico"]))
)

# Convert the filtered data to a Pandas DataFrame (since Altair works with Pandas)
df = filtered_data.collect().to_pandas()
print("data----------",df)
chart3 = alt.Chart(df).mark_boxplot(ticks=True).encode(
    x=alt.X("region:O", title=None, axis=alt.Axis(labels=False, ticks=False), scale=alt.Scale(padding=1)), 
    y=alt.Y("Total Volume:Q"), 
    color="region:N",
    column=alt.Column('year:N', header=alt.Header(orient='bottom'))
).properties(
    width=60
).configure_facet(
    spacing=0
).configure_view(
    stroke=None
)
chart3.show()  