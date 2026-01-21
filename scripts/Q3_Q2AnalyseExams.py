#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:30:49 2024

@author: sijimathew
"""
import polars as pl

#1.Read the data from the CSV file into a DataFrame.
print("Read the data from the CSV file into a DataFrame.")
print()

#url = 'https://data.cdc.gov/api/views/v6ab-adf5/rows.csv?accessType=DOWNLOAD'
url = 'exams.csv'
exam_df = pl.scan_csv(url)
exam_df_collected = exam_df.collect()
print("• Display the first and last five rows")
print(exam_df_collected.head(5))  # First 5 rows
print(exam_df_collected.tail(5))  # Last 5 rows

#2.	Display the basic information for the DataFrame and its columns using the info() method.
print("Basic Information about the DataFrame:\n")
print(exam_df_collected.schema)
# 3.	Display statistical information for the math score, reading score, and writing score columns using the describe() method.
print("Display statistical information")
print(exam_df.describe())

#4.	Group the data by the race/ethnicity column and display the mean scores.
grouped_means = (
    exam_df_collected
    .group_by("race/ethnicity")
    .agg([
        pl.col("math score").mean().alias("Mean Math Score"),
        pl.col("reading score").mean().alias("Mean Reading Score"),
        pl.col("writing score").mean().alias("Mean Writing Score")
    ])
)
print(grouped_means)

#5.	Display a single column as a DataFrame with bracket notation.
math_scores_df = exam_df_collected[["math score"]]
print("Math Scores as a DataFrame:")
print(math_scores_df)

#6.	Display a single column as a Series with bracket notation.
math_scores_series = exam_df_collected["math score"]
print("Math Scores as a Series:")
print(math_scores_series)

#7.	Display a single column as a Series with dot notation.
lunch_dot = exam_df_collected.select('lunch')
print("Lunch as series accessed by dot")
print(lunch_dot)

#8.Display only rows for females with a math score greater than or equal to 80.

filtered_df = exam_df_collected.filter(
    (pl.col('gender') == 'female') & (pl.col('math score') >= 80)
)

print(filtered_df)




