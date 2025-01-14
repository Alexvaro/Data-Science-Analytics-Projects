#!/usr/bin/env python
# coding: utf-8

# # Python 3
# For this tutorial we'll be using the Iris dataset from sklearn. 
# 
# In this notebook we will:
# 1. Import required modules and dataset
# 2. Define multiple Classification models
# 3. Fit the data to our models
# 4. Use our trained models to predict a class label 
# 5. Evaluate our models and chose the best performing model 
# 
# 

# In[111]:


#Import Pandas to your workspace
import pandas as pd


# In[112]:


#Read the "data/features.csv" file and store it into a variable
features = pd.read_csv("data/features.csv")


# In[113]:


#Display the first few rows of the DataFrame
features.head()


# <h1>groupby()</h1>
# 
# <ul>
#     <li>groupby combines 3 steps all in one function:
#         <ol>
#             <li>Split a DataFrame</li>
#             <li>Apply a function</li>
#             <li>Combine the results</li>
#         </ol>
#     </li>
#     <li>groupby must be given the name of the column to group by as a string</li>
#     <li>The column to apply the function onto must also be specified, as well as the function to apply</li>
# </ul>

# <img src="images/groupbyviz.jfif"/>

# In[114]:


#Apply groupby to the Year and Month columns, calculating the mean of the CIP
# List of function : TAB after .
# Function description : Shift + tab
#reset_index() makes things aesthetically pleasing
year_CPI = features.groupby(["Year", "Month"])["CPI"].mean().reset_index()


# In[115]:


year_CPI.head().round(2)


# In[116]:


#Groupby returns a DataFrame, so we have access to all the same methods we saw earlier
year_CPI.sort_values(by = "Year", ascending = False, inplace = True)
year_CPI.head()


# In[117]:


#Read the "data/stores.csv" file and store it into a variable called stores
# "data/" is just telling the program that "stores.csv" is in the "data" folder
stores = pd.read_csv("data/stores.csv")


# In[118]:


#Display the first few rows of the stores DataFrame
stores.head()


# In[119]:


#Convert the values in the 'Type' column from upper to lower case 
stores["Type"] = stores["Type"].str.lower()
# [ ] brackets refer to a column in the data
# ".str" allows you to access the string commands
stores.head()


# In[120]:


#Rename the 'Size' column to 'Area'
stores.rename(columns = {'Size' : 'Area'}, inplace = True)


# In[121]:


#Display the first few rows to verify changes
stores.head()


# <h1>merge()</h1>
# 
# <ul>
#     <li>Merge two DataFrames along common columns</li>
#     <li>Must be provided the DataFrame to merge with, as well as the names of the common columns</li>
#     <li>Will merge and map rows where the values in both DataFrames are equal</li>
# </ul>

# <img src="images/mergetypes.png"/>

# <img src="images/mergeinner.png"/>

# In[122]:


features.head()


# In[123]:


stores.head()


# In[124]:


#Merge the stores DataFrame into the features DataFrame on the Stores column
df_merged = features.merge(stores, on = "Store")


# In[125]:


#Display a few rows to verify changes
df_merged.head()


# In[126]:


#Export the final version of our DataFrame to a .csv file named "final_data.csv" 
df_merged.to_csv('final_data.csv', index = False)
df_merged.to_excel('final_data.xlsx', index = False)
# "index = False" does not save the "index" column in the file 


# <h1>Part 2 - Machine Learning</h1>

# In[127]:


#Import libraries we will need

# numpy
import numpy

# scikit-learn
import sklearn

import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

from sklearn import model_selection

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn import datasets

from IPython.display import display

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)


# In[128]:


#2.2 Load Dataset
dataset = datasets.load_iris()
display(dataset)

feature_names = dataset['feature_names']

iris_data = pd.DataFrame(data = dataset['data'], columns = feature_names)
target = pd.DataFrame(data = dataset['target'], columns = ['class'])

# Converting to a DataFram in Pandas, extracting the data from the 'data' and 'target' dictionaries


# In[129]:


target.head()


# In[130]:


# 3.1 Dimensions of Dataset

print(iris_data.shape)


# In[131]:


#Peek at the Data
print(iris_data.head(20))


# In[132]:


#Statistical Summary
print(iris_data.describe())


# In[133]:


#Class Distribution - value_counts function to see number of each class
target['class'].value_counts()


# In[134]:


#Data Visualization
#Using the plot() function, we can make boxplots by simply specifying the kind of plot
# sharex/sharey = "do you want to share the access values for different columns?"
iris_data.plot(kind = "box", subplots = True, layout=(2,2), sharex = False, sharey = False)

plt.show()
#creates it after you make the specifications


# In[135]:


#Histograms
iris_data.hist()
plt.show()


# In[136]:


# Multivariate Plots
# scatter plot matrix

scatter_matrix(iris_data)
plt.show()


# In[137]:


#Create the Train and Test set
X = iris_data[feature_names].values
Y = target.values

test_size = 0.20
# Setting the test values as 20% of the data 

#We use train_test_split to shuffle and divide our data into our train and test sets
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size = test_size, random_state = 7)


# <img src='images/train_test_split.png'/>

# <img src='images/mlprocess.png'/>

# In[138]:


#Verify our split
X_test.shape


# In[139]:


#Create an instance of our algorithm (model)
LDA = LinearDiscriminantAnalysis()


# In[140]:


#Feed our training data to our model
LDA.fit(X_train, Y_train)


# In[141]:


#Test our model on the test set
LDA.score(X_test, Y_test)
# Gives back a percentage of the model's performance


# In[142]:


X_test


# In[143]:


Y_test


# In[144]:


# "predict() takes a list from the X_test to predict the value that corresponds with the Y_test"
LDA.predict([[6.7, 3.1, 5.6, 2.4]])


# In[145]:


#Use predict() to obtain prediction from our model on data points
for point in X_test:
    prediction = LDA.predict([point])
    print(point)
    print(f"LDA believes this is a {prediction}!")

