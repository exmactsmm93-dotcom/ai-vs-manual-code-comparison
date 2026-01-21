#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:59:54 2024

@author: sijimathew
"""
import pandas as pd
#Read the data from the CSV file into a DataFrame and display the first five rows.
print()
print("Read the data from the CSV file into a DataFrame and display the first five rows")
print()
exam_data = pd.read_csv('exams.csv')
print(exam_data.head())

  # Save the DataFrame to a pickle file named exams_data.pkl
exam_data.to_pickle('exams_data.pkl')
exam_data= pd.read_pickle('exams_data.pkl')

#Display the basic information for the DataFrame and its columns using the info() method.
print("Get more information about a DataFrame")
print()
print(exam_data.info())  # information about DataFrame
print()

#Display statistical information for the math score, reading score, and writing score columns using the describe() method.
print("Display statistical information for the math score, reading score, and writing score columns using the describe() method")
# Display statistical information for math score, reading score, and writing score
scores_description = exam_data[['math score', 'reading score', 'writing score']].describe()
print()
# Display the result
print(scores_description)
print()


#Group the data by the race/ethnicity column and display the mean scores.
print("Group the data by the race/ethnicity column and display the mean scores.")
print()
# Group the data by race/ethnicity and calculate the mean scores
mean_scores_by_race = exam_data.groupby('race/ethnicity')[['math score', 'reading score', 'writing score']].mean()
# Display the result
print(mean_scores_by_race)
print()


#Display a single column as a DataFrame with bracket notation.
print("Displaying column 'parental level of education' as a DataFrame with bracket notation")
print()
ple_column = exam_data[['parental level of education']] #When you want to display the column as a DataFrame, you use double brackets 
print(ple_column)
print()

#Display a single column as a Series with bracket notation.
print("Displaying column 'parental level of education' as a Series with bracket notation")
print()
ple_column_series = exam_data['parental level of education']  # Using single bracket for Series
print(ple_column_series)
print()


#Display a single column as a Series with dot notation.
print("Displaying column 'lunch' as a Series with dot notation")
print()
lunch_column_dot = exam_data.lunch
print(lunch_column_dot)
print()

#Display only rows for females with a math score greater than or equal to 80.
print("Displaying rows for females with a math score greater than or equal to 80.")
print()
female_math_scores_80 = exam_data[(exam_data['gender'] == 'female') & (exam_data['math score'] >= 80)] #Filter the data

# Display the filtered DataFrame
print(female_math_scores_80)