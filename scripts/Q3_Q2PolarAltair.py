#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 00:52:18 2024

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

#3. Bar Chart count vs parental level of education

# Create a bar chart using Altair
chart1 = alt.Chart(exam_df_collected).mark_bar().encode(
    x=alt.X('parental level of education:N', 
            sort='-y', 
            title='Parental Level of Education', 
            axis=alt.Axis(labelAngle=360)),  # Tilt labels at -45 degrees
    y=alt.Y('count():Q', title='Count'),  # Y-axis with count of occurrences
    tooltip=['parental level of education:N', 'count():Q'],  # Tooltip showing counts
    color='parental level of education:N'  # Different colors for categories
).properties(
    title='Count of Parental Level of Education',
    width=300,
    height=400
)

chart1.show()
#4.	Rotate the x labels for the above plot to make them readable.
chart2 = alt.Chart(exam_df_collected).mark_bar().encode(
    x=alt.X('parental level of education:N', 
            sort='-y', 
            title='Parental Level of Education', 
            axis=alt.Axis(labelAngle=45)),  # Tilt labels at -45 degrees
    y=alt.Y('count():Q', title='Count'),  # Y-axis with count of occurrences
    tooltip=['parental level of education:N', 'count():Q'],  # Tooltip showing counts
    color='parental level of education:N'  # Different colors for categories
).properties(
    title='Count of Parental Level of Education',
    width=300,
    height=400
)

chart2.show()

#5.	Create a Seaborn scatter plot that compares the writing scores with the reading score.  Use a different colour to show which students took a test prep course.
scatter_plot = alt.Chart(exam_df_collected).mark_circle(size=100).encode(
    x=alt.X('reading score:Q', title='Reading Score'),
    y=alt.Y('writing score:Q', title='Writing Score'),
    color=alt.Color('test preparation course:N', legend=alt.Legend(title='Test Prep Course')),
    tooltip=['reading score', 'writing score', 'test preparation course']  # Add tooltips for details
).properties(
    title='Comparison of Writing and Reading Scores by Test Prep Course',
    width=600,
    height=400
    )
scatter_plot.show()