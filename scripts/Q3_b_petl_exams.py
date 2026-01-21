#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 01:04:32 2024

@author: sijimathew
"""

import sqlite3
import petl as etl

# SQLite database file
db_file = 'exams.db'
table_name = 'exam_data'

# 1. Write the CSV file data to SQLite3 database
url = 'exams.csv'
# Create a SQLite database connection
conn = sqlite3.connect(db_file)

# Load data from CSV and write it to SQLite3 database
exam_data = etl.fromcsv(url)
etl.todb(exam_data, conn, table_name, create=True, sample=1000)
print("Data written to SQLite3 database.")

#1.	Read the data from the CSV file into a DataFrame and display the first five rows

exam_data = etl.fromcsv(url)
print("First five rows of the data:")
print(etl.head(exam_data, 5))

#2.	Display the basic information for the DataFrame and its columns using the info() method.

print("\nColumn Names:")
print(exam_data.columns)

#3.	Display statistical information for the math score, reading score, and writing score columns using the describe() method.

columns = ['math score', 'reading score', 'writing score']
for column in columns:
    column_data = etl.values(exam_data, column)
    column_data = [int(value) for value in column_data if value.isdigit()]  # Convert to integers, ignoring non-numeric values

    print(f"\nStatistics for '{column}':")
    print(f"  Count: {len(column_data)}")
    print(f"  Mean: {sum(column_data) / len(column_data):.2f}")
    print(f"  Min: {min(column_data)}")
    print(f"  Max: {max(column_data)}")
    print(f"  Median: {sorted(column_data)[len(column_data) // 2]}")

#4.	Group the data by the race/ethnicity column and display the mean scores
def mean(values):
    return sum(values) / len(values) if values else None
mean_scores = (
    etl.aggregate(
        exam_data,
        key='race/ethnicity',
        aggregation={
            'math_mean': ('math score', lambda scores: mean(list(map(float, scores)))),
            'reading_mean': ('reading score', lambda scores: mean(list(map(float, scores)))),
            'writing_mean': ('writing score', lambda scores: mean(list(map(float, scores))))
        }
    )
)
print("\nMean Scores Grouped by Race/Ethnicity:")
print(etl.look(mean_scores))

#5.	Display a single column as a DataFrame with bracket notation.
math_scores = etl.cut(exam_data, 'math score')
print("\nSingle Column: 'math score'")
print(etl.look(math_scores))

#6.	Display a single column as a Series with bracket notation.
#7.	Display a single column as a Series with dot notation.
math_scores_series = etl.values(exam_data, 'math score')
print("\nSingle Column as Series: 'math score'")
print(math_scores_series)

#8.	Display only rows for females with a math score greater than or equal to 80.
filtered_data = etl.select(exam_data, lambda row: row['gender'] == 'female' and int(row['math score']) >= 80)
print("\nRows for females with a math score >= 80:")
print(etl.look(filtered_data))

# Write the updated data to the sqlite3 database
table_name_updated = 'exam_data_updated'
updated_data = etl.addfield(exam_data, 'total score', lambda row: int(row['math score']) + int(row['reading score']) + int(row['writing score']))
print("Updated data written back to SQLite3 database.")
etl.todb(updated_data, conn, table_name_updated, create=True, sample=1000)
# Close the database connection
conn.close()
