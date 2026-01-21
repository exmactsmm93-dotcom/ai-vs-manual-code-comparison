#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:48:31 2024

@author: sijimathew
"""

import pandas as pd
import seaborn as sns

#Read the data from the CSV file into a DataFrame and display the first five rows.
print()
print("Read the data from the CSV file into a DataFrame.")
print()
avocado_data = pd.read_csv('avocado.csv')

# Save the DataFrame to a pickle file named avocado_data.pkl
avocado_data.to_pickle('avacado_data.pkl')
avocado_data = pd.read_pickle('avocado_data.pkl')

print("Display the first five rows of the DataFrame")
print()
print(avocado_data.head())
print()

#Scattered  plot with a Seaborn specific method.
sns.scatterplot(data=avocado_data, x='AveragePrice', y='Total Volume')

#Create the same plot but with the hue parameter set to year and the dots for the total volume ranging in size from 10 to 100.

sns.relplot(data= avocado_data, kind='scatter',x='AveragePrice', y='Total Volume',hue='year', sizes=(10, 100))

#Create a plot that looks like box plot

sns.catplot(data=avocado_data.query('year >= 2015 and year <= 2018 and region in ["TotalUS", "West", "WestTexNewMexico"]'), kind='box', 
            x='year',y='Total Volume',hue='region',
            aspect=1.5,
            native_scale= True,
            palette={
                'TotalUS': 'red',       # Blue for 'Total US'
                'West': 'orange',         # Green for 'West'
                'WestTexNewMexico': 'blue'  # Orange for 'WestTexNewMexico'
                
})

"""
catplot:A Seaborn function used for categorical plots, which can generate different kinds of plots based on the kind parameter.
.query filtering is happening here
aspect=1.5:

This adjusts the aspect ratio of the plot (width to height). A value of 1.5 makes the plot wider than it is tall.
native_scale=True:

This argument controls the scaling of the axes. When set to True, the axes will follow the scale of the data, potentially improving readability if the values are widely spread out.


"""