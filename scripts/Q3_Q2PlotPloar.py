#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:01:04 2024

@author: sijimathew
"""
import polars as pl
import altair as alt

alt.renderers.enable('png')


#1.	Read the data from the CSV file into a DataFrame and display the first five rows.
print("Read the data from the CSV file into a DataFrame.")
print()

#url = 'https://data.cdc.gov/api/views/v6ab-adf5/rows.csv?accessType=DOWNLOAD'
url = 'exams.csv'
exam_df = pl.scan_csv(url)
exam_df_collected = exam_df.collect()
print("• Display the first and last five rows")
print(exam_df_collected.head(5))  # First 5 rows
print(exam_df_collected.tail(5))  # Last 5 rows



#2.Use the plot() method to create a box plot.
exam_df_pandas = exam_df_collected.to_pandas()
# Create the box plot using Altair for math score by gender
chart1 = alt.Chart(exam_df_pandas).mark_boxplot().encode(
    x='gender:N',  # Gender on the x-axis (categorical data)
    y='math score:Q'     # Math scores on the y-axis (quantitative data)
).properties(
    title='Box Plot of Math Scores by Gender'
).properties(
    width=300
).configure_facet(
    spacing=60
)
# Display the plot
chart1.show()

#3.	Scattered Plot reading score Vs m,ath Score

chart2 = alt.Chart(exam_df_pandas).mark_point(shape='circle',color='blue', fill='true').encode(
    x='math score:Q',   
    y='reading score:Q',
).properties(
    title='Scatter Plot: Reading Score vs Math Score'
)

chart2.show()

# 4 Group the data by gender and calculate average scores for math and reading

mean_scores_by_gender = (
    exam_df.group_by(["gender"])
    .agg([
        pl.col("math score").sum().alias("math score"),
        pl.col("reading score").sum().alias("reading score"),
        pl.col("writing score").sum().alias("writing score"),
    ])
    .collect().to_pandas()
)

mean_scores_long = mean_scores_by_gender.melt(id_vars=["gender"],
                                              value_vars=["math score", "reading score", "writing score"],
                                              var_name="score_type", value_name="score")
Chart3 = alt.Chart(mean_scores_long).mark_bar().encode(
    x=alt.X("score_type:N", title="Gender"),
    y=alt.Y("count():Q", title="Count of Scores"),
    color="gender:N",
    tooltip=["gender", "score_type", "count():Q"]
).properties(
    title="Scores by Gender"
).properties(
    width=300
).configure_facet(
    spacing=200
).configure_view(
    stroke=None
)
Chart3.show()
