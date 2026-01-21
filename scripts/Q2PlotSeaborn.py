#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:58:24 2024

@author: sijimathew
"""

import pandas as pd
import seaborn as sns

#Read the data from the CSV file into a DataFrame and display the first five rows.
print()
print("Read the data from the CSV file into a DataFrame and sisplay the first five rows")
print()
exam_data = pd.read_csv('exams.csv')

  # Save the DataFrame to a pickle file named exams_data.pkl
exam_data.to_pickle('exams_data.pkl')
exam_data2 = pd.read_pickle('exams_data.pkl')

print(exam_data.head())
print()

#Seaborn catplot() method to create a plot
#Count the occurrences
parental_counts = exam_data2['parental level of education'].value_counts().reset_index()
parental_counts.columns = ['parental level of education', 'Count']
#plot the counts
sns.catplot(data=parental_counts, kind='bar', 
            x='parental level of education',
            y='Count',
            palette='Set1'
           )

#Rotate the x labels for the above plot to make them readable

bar_plot = sns.catplot(data=parental_counts, kind='bar', 
            x='parental level of education',
            y='Count',
            palette='Set1'
           )
bar_plot.set_xticklabels(bar_plot.ax.get_xticklabels(), rotation=45, ha='right')
"""
bar_plot.set_xticklabels(...): This is modifying the x-axis labels (i.e., the labels for the different parental education levels).
bar_plot.ax.get_xticklabels(): This retrieves the current list of x-axis tick labels, which represent the different levels of parental education.
ha horizontal aignment
"""

#Create a Seaborn scatter plot that compares the writing scores with the reading score.  
#Use a different colour to show which students took a test prep course

sns.relplot(data= exam_data2, kind='scatter',x='reading score', y='writing score',hue='test preparation course', sizes=(10, 100))