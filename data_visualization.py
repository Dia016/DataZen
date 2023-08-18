# -*- coding: utf-8 -*-
"""Data Visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ss4YFcTUTvvB_QzHhC3MucL_Cg5hMkCX
"""

### Quick Start
""" Matplotlib: It is the core module providing the fundamental
                building blocks for creating plots """
""" Matplotlib.pyplot: It provides a MATLAB like interface. Provides
                       functions that interact with the figure i.e.
                       creates a figure, decorates plot with labels and
                       creates a plotting area in a figure """

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

### To use different styles for our plot
print(plt.style.available)

plt.style.use('fivethirtyeight')

# Developer ages
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# Median All Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

### To plot the variates (For Python Devs)
plt.plot(ages_x, py_dev_y, color='b', marker='o', linewidth=3, label='Python')

### To plot the variates (For Java Devs)
plt.plot(ages_x, js_dev_y, color='#adad3b', marker='o', linewidth=3, label='JavaScript')

### To plot the variates (For All Devs)
plt.plot(ages_x, dev_y, color='k', linestyle='--', marker='.', linewidth=3, label='All Devs')

### Adding Labels to the Axes
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

### Adding Title to the Plot
plt.title('Median Salary (USD) by Age')

### Adding a legend to distinguish
plt.legend()

### To add a grid
plt.grid('True')

### To ensure some padding is given (Might vary from display to display)
plt.tight_layout()

### To save the plot as a PNG (in current working directory)
"""
plt.savefig('plot.png')
"""

### This aids in displaying the plot (Colab notebook works different)
plt.show()

### To do so we shall be using the bar method instead of the plot method

### Median All Developers salary (in USD) in bar chart format
plt.bar(ages_x, dev_y, color="#444444", label ="All Devs")

### Adding Labels to the Axes
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

### Adding Title to the Plot
plt.title('Median Salary (USD) by Age (Bar Chart)')

### Adding a legend to distinguish
plt.legend()
plt.tight_layout()

### This aids in displaying the plot (Colab notebook works different)
plt.show()

### To plot the variates (For All Devs)
plt.bar(ages_x, dev_y, color='#444444', label='All Devs')

### To plot the variates (For Python Devs)
plt.bar(ages_x, py_dev_y, color='#008fd5', label='Python')

### To plot the variates (For Java Devs)
plt.bar(ages_x, js_dev_y, color='#e5ae38', label='JavaScript')

### Adding Labels to the Axes
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

### Adding Title to the Plot
plt.title('Median Salary (USD) by Age')

### Adding a legend to distinguish
plt.legend()

### To add a grid
plt.grid('True')

### To ensure some padding is given (Might vary from display to display)
plt.tight_layout()

### This aids in displaying the plot (Colab notebook works different)
plt.show()

### To do this we shall be using Numpy

### Generating X coordinates for bars
x_indexes = np.arange(len(ages_x))

### This is like having a list within a list but like a Numpy Array
width = 0.25

### To offset these bars on the X-Axis, we shall +- the width

### To plot the variates (For All Devs)
plt.bar(x_indexes - width, dev_y, width=width, color='#444444', label='All Devs')

### To plot the variates (For Python Devs)
plt.bar(x_indexes, py_dev_y, width=width, color='#008fd5', label='Python')

### To plot the variates (For Java Devs)
plt.bar(x_indexes + width, js_dev_y, width=width, color='#e5ae38', label='JavaScript')

### Adding Labels to the Axes
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

### Adding Title to the Plot
plt.title('Median Salary (USD) by Age')

### Adding a legend to distinguish
plt.legend()

### To add a grid
plt.grid('True')

### To ensure some padding is given (Might vary from display to display)
plt.tight_layout()

### To fix the X-Axis Values (They aren't displaying the range we intend to have)
plt.xticks(ticks = x_indexes, labels=ages_x)

### This aids in displaying the plot (Colab notebook works different)
plt.show()

#Now we shall be using a CSV file and using it's Data

### Specifying the path and loading the CSV into a DataFrame

path = "https://raw.githubusercontent.com/HarshNagrani9/DataZen-7-Days-Data-Science-/main/matplotlib/data.csv"
data = pd.read_csv(path)

### Specifying some Columns (Setting the column to all of the Responser ID's in our CSV)
ids = data['Responder_id']

### Doing the same for the Languages Column
lang_responses = data['LanguagesWorkedWith']

### Displaying the first five contents to ensure
### we have successfully imported the CSV as a DataFrame

data.head()

### Declaring a Counter
language_counter = Counter()

### For iterating through our DataFrame
for response in lang_responses:
  language_counter.update(response.split(';'))

### Lists to Store our language lists and popularity lists for each row
languages = []
popularity = []

### To add the most popular language and its respective popularity to our lists
for item in language_counter.most_common(15):
  languages.append(item[0])
  popularity.append(item[1])

### To reverse the list
languages.reverse()
popularity.reverse()

### To make the plots
plt.bar(languages, popularity)

### Plot decorations
plt.title("Most Popular Languages")
plt.xlabel("Number of People Using")
plt.ylabel("Languages")
plt.tight_layout()

### To show the plot
plt.show()

### To do so we need to change the "bar" command
plt.barh(languages, popularity)

### Plot decorations
plt.title("Most Popular Languages")
plt.xlabel("Number of People Using")
plt.ylabel("Languages")

### To show the plot
plt.show()

### Beginning with a basic starting code for our plots
slices = [60, 40]

### Using the plot command
plt.pie(slices)

### Plot decoration
plt.title("My First Pie Chart")
plt.tight_layout()
plt.show()

### General way to add labels
labels = ['Sixty', 'Forty']

### Using the plot command
plt.pie(slices, labels=labels)

### Plot decoration
plt.title("My First Pie Chart")
plt.tight_layout()
plt.show()

### For indicating better separation between the different slices
### , we can use a few properties

### General way to add labels
labels = ['Sixty', 'Forty']

### Using the plot command
plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'})

### The "wedgeprops" is a dictionary of values where we can set
### the desired values for our properties

### Plot decoration
plt.title("My First Pie Chart")
plt.tight_layout()
plt.show()

### For indicating better separation between the different slices
### , we can use a few properties

### General way to add labels
labels = [60 , 40]
colors=["purple","pink"]

### Using the plot command
plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})

### The "wedgeprops" is a dictionary of values where we can set
### the desired values for our properties

### Plot decoration
plt.title("My First Pie Chart")
plt.tight_layout()
plt.show()

### Let's specify a few colors and use them for our plot

### Defining the lists
slices = [120, 80, 30, 20]
labels = ['120', '80', '30', '20']

### Creating a colors list
colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

### Using the plot command
plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})

### Plot decoration
plt.title("My First Pie Chart")
plt.tight_layout()
plt.show()

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

### Using the plot command
plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'})

### Plot decoration
plt.title("My First Pie Chart")
plt.tight_layout()
plt.show()

### Reducing the number of items and checking the plot again

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

### Using the plot command
plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'})

### Plot decoration
plt.title("My First Pie Chart")
plt.tight_layout()
plt.show()

### We shall be making "Python" stand out amongst all the items

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

### Using the explode list to specify our aim
explode = [0, 0, 0, 0.1, 0]

### Using the plot command (passing the "explode" argument)
plt.pie(slices, labels=labels, explode=explode, wedgeprops={'edgecolor': 'black'})

### Plot decoration
plt.title("My First Pie Chart")
plt.tight_layout()
plt.show()

## We shall be passing the "autopct" as an argument to the plt.pie method

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

### Using the explode list to specify our aim
explode = [0, 0, 0, 0.1, 0]

### Using the plot command (passing the "autopct" argument)
plt.pie(slices, labels=labels, explode=explode, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

### Plot decoration
plt.title("My First Pie Chart")
plt.tight_layout()
plt.show()

#With just the right amount of adjustments to out plots, we can enhance the readibility of the graphs. This aids in better understanding of our data as well as enables us to derive deeper insights which might be difficult to observe from just the surface of our Raw data

#Implementing Stack Plots using Matplotlib
#We usually use this type of plot when we intend on storing the individual as well as collective data for some parameter.

#Eg: We intend on storing the points of the team as well as the individual players for a given match

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

### Adding labels for our players
labels = ['player1', 'player2', 'player3']

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
### Implementing a Stack plot
plt.stackplot(minutes, player1, player2, player3, labels=labels)

### Plot Decoration
plt.title("Points distribution")
plt.legend()
plt.tight_layout()
plt.show()

#The legend doesn't seem to be in the best possible position given the Ascending nature of our data. Let's have a look at how we can resolve this
### Implementing a Stack plot
plt.stackplot(minutes, player1, player2, player3, labels=labels)

### Changing the location for our legend
plt.legend(loc='upper left')

### Plot Decoration
plt.title("Points distribution")
plt.tight_layout()
plt.show()

### Defining a colors list
colors = ['#6d904f', '#fc4f30', '#008fd5']

### Implementing a Stack plot
plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

### Plot Decoration
plt.title("Points distribution")
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f

#The data that we shall be using has each index adding upto a total of 8. Our aim is to draw some conclusions from this data which aren't very evident as of now
### Data to work on
player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

### Defining a colors list
colors = ['#6d904f', '#fc4f30', '#008fd5']

### Implementing a Stack plot
plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

### Plot Decoration
plt.title("Points distribution")
plt.legend(loc=(0.07, 0.05))
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f

#So now that we have covered Stack plots, I'm sure that we are aware of how important this plot can be in case there is a need for some comparative analysis or to see the change in statistics over a period of time for any given parameter.
#It aids in observing certain trends that might not be visible to us by just looking at the data and thus drawing conclusions which are essential to convey our ideas and inferences to the target audience

#Modifications for Line Chart
### First we need to import our dataset into our colab notebook
path = "https://raw.githubusercontent.com/HarshNagrani9/DataZen-7-Days-Data-Science-/main/matplotlib/line_fill.csv"
dataframe = pd.read_csv(path)

### Displaying to check successfull importing
dataframe.head()

### Grabbing the age column for further use
ages = dataframe['Age']
dev_salaries = dataframe['All_Devs']
py_salaries = dataframe['Python']
js_salaries = dataframe['JavaScript']

### Plotting a line chart for All Developers
plt.plot(ages, dev_salaries, color='#444', linestyle='--', linewidth=2, label="All Devs")

### Plotting a line chart for Python Developers
plt.plot(ages, py_salaries, linewidth=2, label="Python Devs")

### To show the legend
plt.legend()

### Plot Decoration
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()

### Plotting a line chart for All Developers
plt.plot(ages, dev_salaries, color='#444', linestyle='--', linewidth=2, label="All Devs")

### Plotting a line chart for Python Developers
plt.plot(ages, py_salaries, linewidth=2, label="Python Devs")

### Filling conditions
plt.fill_between(ages, py_salaries)

### To show the legend
plt.legend()

### Plot Decoration
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()

### Plotting a line chart for All Developers
plt.plot(ages, dev_salaries, color='#444', linestyle='--', linewidth=2, label="All Devs")

### Plotting a line chart for Python Developers
plt.plot(ages, py_salaries, linewidth=2, label="Python Devs")

### Filling conditions (With custom opacity using the "alpha" parameter)
plt.fill_between(ages, py_salaries, alpha=0.25)

### To show the legend
plt.legend()

### Plot Decoration
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()

### Plotting a line chart for All Developers
plt.plot(ages, dev_salaries, color='#444', linestyle='--', linewidth=2, label="All Devs")

### Plotting a line chart for Python Developers
plt.plot(ages, py_salaries, linewidth=2, label="Python Devs")

### Limit for the fill
overall_median = 57287

### Filling conditions (Limiting the fill using another argument)
plt.fill_between(ages, py_salaries, overall_median, alpha=0.25)

### To show the legend
plt.legend()

### Plot Decoration
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.tight_layou

#Now in case we want to represent this differently. For example, if we are above a value "X" I intend on showing it as GREEN and when it drops below this value "X" it should be RED.

### Plotting a line chart for All Developers
plt.plot(ages, dev_salaries, color='#444', linestyle='--', linewidth=2, label="All Devs")

### Plotting a line chart for Python Developers
plt.plot(ages, py_salaries, linewidth=2, label="Python Devs")

### Limit for the fill
overall_median = 57287

### Filling conditions (Limiting the fill using another argument)
plt.fill_between(ages, py_salaries, overall_median
                 , where=(py_salaries > overall_median)
                 , interpolate=True, alpha=0.25)

### Interpolate: To make sure certain X sections don't clipped and
### all regions are displayed correctly

plt.fill_between(ages, py_salaries, overall_median
                 , where=(py_salaries <= overall_median)
                 , interpolate=True, color='red', alpha=0.25)

### To show the legend
plt.legend()

### Plotting a line chart for All Developers
plt.plot(ages, dev_salaries, color='#444', linestyle='--', linewidth=2, label="All Devs")

### Plotting a line chart for Python Developers
plt.plot(ages, py_salaries, linewidth=2, label="Python Devs")

### Limit for the fill
overall_median = 57287

### Filling conditions (Filling between the two lines plotted by us)
plt.fill_between(ages, py_salaries, dev_salaries
                 , where=(py_salaries > dev_salaries)
                 , interpolate=True, alpha=0.25, label="Above Average")

### Interpolate: To make sure certain X sections don't clipped and
### all regions are displayed correctly

plt.fill_between(ages, py_salaries, dev_salaries
                 , where=(py_salaries <= dev_salaries)
                 , interpolate=True, color='red', alpha=0.25, label="Below Average")

### To show the legend
plt.legend()

### Plot Decoration
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()

#Histograms
#We use this type of chart when we have a large number of columns which we intend on plotting. In such scenarios a bar chart does not result in a feasible outcome thus leaving us looking for an alternative plot.

### Defining a list for ages
ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

### Plotting the histogram
plt.hist(ages, bins=5)

### Plot Decoration
plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

### Defining a list for ages
ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

### Plotting the histogram (With Edge separation this time)
plt.hist(ages, bins=5, edgecolor='black')

### Here "bins=5" means, we shall be having 5 bins (or divisions)
### into which our X-Axis will be distributed into.
### Basically, 5 equal parts of the range 18-55

### Plot Decoration
plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

### Defining a list for ages
ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

### Defining the bin sizes for our plot
bins = [10, 20, 30, 40, 50, 60]

### Plotting the histogram (With custom bin sizes)
plt.hist(ages, bins=bins, edgecolor='black')

### Plot Decoration
plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

### Now lets work with a CSV File
path = 'https://raw.githubusercontent.com/HarshNagrani9/DataZen-7-Days-Data-Science-/main/matplotlib/survey.csv'

### Loading the data into a DataFrame
df = pd.read_csv(path)

### Defining lists for our columns in the DataFrame
ids = df['Responder_id']
ages = df['Age']

### Defining the bin sizes for our plot
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

### Plot Decoration
plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

### Lets plot a Histogram for this data
plt.hist(ages, bins=bins, edgecolor='black')

#By the looks of the chart, it seems as if there is no data from 70 onwards on the X-Axis (Ages) but that isn't the case.

#To make the data in that region more visible we can shift to a logarithmic scale.

### Now lets work with a CSV File
path = 'https://raw.githubusercontent.com/HarshNagrani9/DataZen-7-Days-Data-Science-/main/matplotlib/survey.csv'

### Loading the data into a DataFrame
df = pd.read_csv(path)

### Defining lists for our columns in the DataFrame
ids = df['Responder_id']
ages = df['Age']

### Defining the bin sizes for our plot
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

### Plot Decoration
plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

### Lets plot a Histogram for this data (Using Logarithmic Scale)
plt.hist(ages, bins=bins, edgecolor='black', log=True)

#From this plot, now we can conclude that there were higher number of respondents in 90-100 than we had in 80-90. This observation could not be drawn from the prior plot.

#Lets try and plot a vertical line depicting our median

### Now lets work with a CSV File
path = 'https://raw.githubusercontent.com/HarshNagrani9/DataZen-7-Days-Data-Science-/main/matplotlib/survey.csv'

### Loading the data into a DataFrame
df = pd.read_csv(path)

### Defining lists for our columns in the DataFrame
ids = df['Responder_id']
ages = df['Age']

### Defining the bin sizes for our plot
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

### Lets plot a Histogram for this data
plt.hist(ages, bins=bins, edgecolor='black', log=True)

### Specifications for our median line
median_age = 29
color = '#fc4f30'

### Plot for the vertical line
plt.axvline(median_age, color=color, linewidth=2, label="Median Age")

### Plot Decoration
plt.legend()
plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

#Scatter Plots
#Scatter Plots are usually used when we are working with values for two attributes and we want to depict the relation between these two attributes.
### Using some hardcoded values to solidify syntax
plt.style.use('seaborn')

### Defining lists
x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

### Plotting our Scatter Plot
plt.scatter(x, y)
plt.show()

### Let's increase the size of our dots

### Plotting our Scatter Plot (With improved size of dots)
plt.scatter(x, y, s=100)
plt.show()

### Plotting our Scatter Plot (Basic Customisations)
plt.scatter(x, y, c='green', marker='X')
plt.show()

#The Green markers are now in the shape of the alphabet "X". You can play around with these different styles as per what suits you best.

#Here is the link to the entire list: https://matplotlib.org/stable/api/markers_api.html

#Matplotlib allows us to add edge color to our markers and enhance the look even further. Here are a few customisations that we can make to our plot using these attributes.

### Plotting our Scatter Plot (Basic Customisations)
plt.scatter(x, y, c='pink', marker='X', edgecolor='black', linewidth=1)
plt.show()

### Working with our CSV file

path = 'https://raw.githubusercontent.com/HarshNagrani9/DataZen-7-Days-Data-Science-/main/matplotlib/trending.csv'
df = pd.read_csv(path)

### Verifying our CSV read file
df.head()

### Extracting necessary columns from the DataFrame
view_count = df['view_count']
likes = df['likes']
ratio = df['ratio']

### Plot for our Data
plt.scatter(view_count, likes, edgecolor='black', linewidth=1, alpha=0.75)

### Plot Decoration
plt.title('Trending YouTube VIdeos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')
plt.tight_layout()

#As we can see there is one value which is separated from our main cluster. This value is termed as an "Outlier".

#We can improve the visibility by scaling our Axes to logarithmic function. Let's have a look at how we can do this

### Extracting necessary columns from the DataFrame
view_count = df['view_count']
likes = df['likes']
ratio = df['ratio']

### Plot for our Data
plt.scatter(view_count, likes, edgecolor='black', linewidth=1, alpha=0.75)

### Using the logarithmic scale
plt.xscale('log')
plt.yscale('log')

### Plot Decoration
plt.title('Trending YouTube VIdeos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')
plt.tight_layout()

#As we can observe, the entire dynamic has changed and now we are able to interpret the data in a completely different fashion.

#We can now see the correlation better after having changed the scales of our Axes.

#Lets use the ratios as our colors for the scatter plot.
### Plot for our Data (Using ratios as colors)
plt.scatter(view_count, likes, c=ratio,
            cmap='summer', edgecolor='black', linewidth=1, alpha=0.75)

### A color bar to tell us what the cmap represents
cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

### Using the logarithmic scale
plt.xscale('log')
plt.yscale('log')

### Plot Decoration
plt.title('Trending YouTube VIdeos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')
plt.tight_layout()

#As we have observed, using a scatter plot in this manner is a great way to depict the correlation between two attributes