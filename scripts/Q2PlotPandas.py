#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:25:15 2024

@author: sijimathew
"""
import pandas as pd
#Read the data from the CSV file into a DataFrame and display the first five rows.
print()
print("Read the data from the CSV file into a DataFrame and sisplay the first five rows")
print()
exam_data = pd.read_csv('exams.csv')

  # Save the DataFrame to a pickle file named exams_data.pkl
exam_data.to_pickle('exams_data.pkl')
exam_data= pd.read_pickle('exams_data.pkl')

print(exam_data.head())
print()

#Use the pandas plot() method to create a box plot.
print("pandas plot() method to create a box plot")
print()
exam_data['writing score'].plot(kind='box')

#Use the pandas plot() method to create a plot like the one that follows:
print("Ploting Reading score V/S Math score")
exm_plt=exam_data.plot(kind='scatter', x='math score', y='reading score', color='blue')
# Set x-axis and y-axis ticks
exm_plt.set_xticks([0, 20, 40, 60, 80, 100])  # x-axis ticks
exm_plt.set_yticks([20, 40, 60, 80, 100])    # y-axis ticks

#Group the data by the gender column and calculate the average scores.  Then create a bar plot.
avg_scores = exam_data.groupby('gender')[['math score', 'reading score']].mean().plot(kind='bar')

