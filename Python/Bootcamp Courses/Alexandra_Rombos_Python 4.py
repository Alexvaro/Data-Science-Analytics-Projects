#!/usr/bin/env python
# coding: utf-8

# # Python 4
# For this bootcamp we'll be using a few data visualization modules to plot data using Python. 
# 
# In this notebook we will:
# 1. Import required modules and datasets
# 2. Manipulate the data using Pandas
# 3. Visualize the data
# 
# 

# In[1]:


#Remove warnings from our outputs
import warnings
warnings.filterwarnings("ignore")


# # Matplotlib
# 
# "Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python."
# 
# Matplotlib is one of the most popular libraries used to create data vizualizations in Python. It uses an object-oriented API (classes) which we've already worked with when using Pandas
# 
# Below is a breakdown of some of the key elements that go into a matplotlib figure
# 
# Two main concepts to understand
# - A figure is the whole figure and can contain any number of axes (usually at least 1)
# - Axes are the "plot" that will contain your title, legend, etc.

# <img src="images/mplib_anatomy.png"/>

# In[3]:


import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5,6]
data = np.array(x)
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introduct
# Create a figure and an axes.
fig, ax = plt.subplots()
# Plot some data on the axes.
ax.plot(data, data, label='linear')
# Plot more data on the axes...
ax.plot(data, data**2, label='quadratic')
# ... and some more.
ax.plot(data, data**3, label='cubic')
# Add an x-label to the axes.
ax.set_xlabel('x label')
# Add a y-label to the axes.
ax.set_ylabel('y label')
# Add a title to the axes.
ax.set_title("01-11-2021")
# Add a legend.
ax.legend()
#Save our plot as an image
plt.savefig('line_plot.png')


# # Pandas Plotting
# Pandas offers a easy way to access Matplotlib to plot the data inside of a DataFrame.
# 
# We will go over a few ways to plot some stock data.
# 

# In[1]:


#Import Pandas 
import pandas as pd

#A few configurations
pd.plotting.register_matplotlib_converters()
get_ipython().run_line_magic('matplotlib', 'inline')

print("Setup Complete")


# In[3]:


# Import stock data
stock_df = pd.read_csv('data/stocks.csv', index_col = 'date', parse_dates = True)


# In[4]:


#Take a look at the data
stock_df.head()


# In[5]:


#Plotting data as easy as calling the plot() function
stock_df.plot(kind = 'line')


# In[6]:


#Plotting data as easy as calling the plot() function
stock_df.plot(kind = 'line', figsize = (10,7), title = 'Stock Data 2017-2018')


# In[17]:


import matplotlib.pyplot as plt


# In[18]:


#Define a MPL figure and axes to give us more control of our visual
fig, axs = plt.subplots(2, 2, figsize = (20,10))
fig.suptitle('Vertically stacked subplots', fontsize = 20)
#Must specify the axes we want to plot onto, and can specify addicitonal styling parameters with 'colormap'
stock_df.plot(kind = 'line', subplots = True, colormap = 'jet', ax = axs)
#Use a FOR loop to add on the X and Y labels
for ax in axs.flat:
    ax.set(xlabel='Date', ylabel='Price')


# In[19]:


from pandas.plotting import scatter_matrix
scatter_matrix(stock_df, alpha = 0.2, figsize = (6,6), diagonal = 'kde')


# # Barchart
# For the next portion of the bootcamp, we're going to be using Airbnb data. 
# 
# We'll be going over some of the other kinds of plots we can create directly from a Pandas DataFrame
# 
# 

# In[21]:


#https://www.kaggle.com/shivamb/netflix-shows
#Import new dataset from the data/netflix_titles.csv file into variable net_df
net_df = pd.read_csv('data/netflix_titles.csv')


# In[22]:


net_df.head()


# In[25]:


#Calculate the number of movies per country
freq = net_df['country'].value_counts()
print(freq)


# In[26]:


#Plot this data as a bar chart
plt.figure(figsize = (30,10)) 
freq.plot(kind = 'bar', title = "Number of Titles Per Country")


# In[33]:


#Create a pivot so we can visualize the data
net_pivot = net_df.pivot_table(values = 'show_id', index = 'country', columns = "type", aggfunc = 'count')


# In[34]:


#Create new column for sorting
net_pivot['Sum'] = net_pivot['Movie'] + net_pivot['TV Show']


# In[35]:


net_pivot.head()


# In[36]:


#Sort by new column in decsending order
net_pivot = net_pivot.sort_values('Sum', ascending = False)


# In[37]:


#drop uneccesary column
net_pivot.drop(columns = 'Sum', inplace = True)


# In[39]:


net_pivot.head()


# In[40]:


#Create a basic bar chart of the pivot table
net_pivot.plot(kind='bar',figsize=(30,10))


# In[41]:


#We can stack the bar chart and change the orientation to horizontal
net_pivot.plot(kind='barh', figsize=(30,10), stacked=True)


# In[45]:


#Pie charts and configurations
net_pivot.plot(kind='pie', subplots=True, figsize=(25, 10), autopct='%.2f')
plt.show()


# # Seaborn
# Seaborn is a Python data visualization library based on matplotlib. 
# 
# It provides a high-level interface for drawing attractive and informative statistical graphics.
# 
# 

# In[46]:


import seaborn as sns

#Load tip data and 
tips = sns.load_dataset("tips")


# In[47]:


tips.head()


# In[48]:


#Assign a style
sns.set(style="darkgrid")

# Set the width and height of the figure
plt.figure(figsize=(16,6))
sns.relplot(x='total_bill', y='tip', data=tips)


# In[49]:


# We can add a third dimension with color and style
sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips);


# In[51]:


#Add a fourth dimension using different variables for hue and style
sns.relplot(x="total_bill", y="tip", hue="smoker", style = "time",data=tips);


# In[52]:


#Replot using size variable for hue
sns.relplot(x="total_bill", y="tip", hue="size", data=tips)


# In[53]:


#The size parameter allows us to change the size of data points using variables
sns.relplot(x="total_bill", y="tip", size="size", data=tips);


# In[54]:


#The sizes parameter determines the scale of the data points
sns.relplot(x = 'total_bill', y = 'tip', size = "size", sizes = (15,200), data = tips)


# In[56]:


#The col parameter creates subplots along the provided variable
sns.relplot(x = 'total_bill', y = 'tip', hue = 'smoker', col = 'time', data = tips)


# In[58]:


#Try plotting the Day of the week to see if it has an effect on the tip amount
sns.relplot(x = "total_bill", y = 'tip', hue = 'day', col = 'time', data = tips)
#Derive one insight from the graph


# In[ ]:





# In[60]:


#Create a pivot table of the tips data
hm = tips.pivot_table(index = 'day', columns = 'size', values = 'tip')


# In[61]:


hm.head()


# In[65]:


#An effective way to plot our pivoted data is with a heatmap
sns.heatmap(hm)
plt.savefig('heatmap.png')

