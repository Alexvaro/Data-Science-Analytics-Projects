#!/usr/bin/env python
# coding: utf-8

# <h1>Python 2 - Object Oriented Programming and Pandas</h1>
# 
# <!-- :    : -->
# 
# <p>4 Pillars of OOP</p>
# <ul>
#     
# <li>Encapsulation: Group related variables and functions together to reduce complexity and increase reusability</li>
# <li>Data Abstraction: Creating methods to interface with attributes of your class. Show only essentials to reduce complexity</li>
# <li>Inheritance</li>
# <li>Polymorphism</li>
# 
# </ul>

# ## Jupyter Notebook 
# 
# This is a web-based application (runs in the browser) that is used to interpret Python code. 
# 
# - To add more code cells (or blocks) click on the **'+'** button in the top left corner
# - There are 3 cell types in Jupyter:
#     - Code: Used to write Python code
#     - Markdown: Used to write texts (can be used to write explanations and other key information)
#     - NBConvert: Used convert Jupyter (.ipynb) files to other formats (HTML, LaTex, etc.) 
#     
# 
# - To run Python code in a specific cell, you can click on the **'Run'** button at the top or press **Shift + Enter**
# - The number sign (#) is used to insert comments when coding to leave messages for yourself or others. These comments will not be interpreted as code and are overlooked by the program
# 

# <h1>Inheritance</h1>
# <ul>
#     <li>New classes do not need to be declared from scratch. They may build on existing classes</li>
#     <li>When one class inherits from another, it automatically takes on all the attributes and methods of the first class</li>
#     <li>Goal: Eliminate redundant code by inheriting attributes and methods from a parent class</li>
# </ul>
# 

# In[31]:


class Employee():
    def __init__(self, employee_num, department, name):
        self.employee_num = employee_num
        self.department = department
        self.name = name
        self.days_worked = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.name} ({self.employee_num}) of {self.department}"
        return long_name.title()
    
    def num_days(self):
        print(f"{self.name} has worked {self.days_worked} days")
        
    def increment_days(self):
        self.days_worked += 1
        print("Days worked increased!")


# In[32]:


new_hire = Employee(1213, "Machine Learning", "Peter Ling") 
description = new_hire.get_descriptive_name()


# In[33]:


print(description)


# In[34]:


new_hire.num_days()


# In[35]:


new_hire.increment_days()


# In[36]:


class Engineer(Employee):
    def __init__(self, employee_num, department, name, p_eng):
        super().__init__(employee_num, department, name)
        self.p_eng = p_eng
    


# In[44]:


new_eng_hire = Engineer(1213, "Marketing", "Shakti", False)


# In[39]:


new_eng_hire.get_descriptive_name()


# In[40]:


new_eng_hire.num_days()


# In[47]:


new_eng_hire.p_eng


# <h1>Polymorphism</h1>
# 
# <ul>
#     <li>Because child classes inherit all attributes and methods from their parent class, we may wish to refactor and customize classes to specific use cases.</li>
#     <li>Overiding involves the redefining of methods to better suit child classes </li>
# </ul>

# In[67]:


class Recruiter(Employee):
    def __init__(self, employee_num, department, name):
        super().__init__(employee_num, department, name)
        self.hires = []
        
    def get_descriptive_name(self):
        long_name = f"{self.name} ({self.employee_num}) has hired {len(self.hires)} many employees."
        return long_name.title()
    
        
    def add_hire(self, emp_id):
        self.hires.append(emp_id)
        print(self.hires)


# In[68]:


new_rec_hire = Recruiter(1000, "Sales", "Robert")


# In[69]:


new_rec_hire.get_descriptive_name()


# In[70]:


new_rec_hire.add_hire(1080) 


# In[71]:


new_rec_hire.get_descriptive_name()


# <h1>Pandas</h1>

# In[72]:


import pandas as pd


# <h1>Reading CSV Files</h1>
# 
# <ul>
#     <li>Function to use in Pandas: read_csv()</li>
#     <li>Value passed to read_csv() must be string and the <b>exact</b> name of the file</li>
#     <li>CSV Files must be in the same directory as the python file/notebook</li>
# </ul>

# In[73]:


features_df = pd.read_csv('features.csv')


# <h1>Basic DataFrame Functions</h1>
# 
# <ul>
#     <li>head() will display the first 5 values of the DataFrame</li>
#     <li>tail() will display the last 5 values of the DataFrame </li>
#     <li>shape will display the dimensions of the DataFrame</li>
#     <li>columns() will return the columns of the DataFrame as a list</li>
#     <li>dtypes will display the types of each column of the DataFrame</li>
#     <li>drop() will remove a column from the DataFrame</li>
# </ul>

# In[74]:


print(features_df)


# In[98]:


features_df.head(10)


# In[76]:


features_df.tail()


# In[80]:


features_df.shape


# In[81]:


features_df.columns


# In[82]:


features_df.columns = ['Store', 'Date', 'Temperature', 'Fuel Price', 
                       'MD1', 'MD2', 'MD3', 'MD4', 'MD5', 'CPI', 
                       'Unemployment', 'IsHoliday']


# In[83]:


features_df.head()


# In[84]:


features_df.rename(columns = {'Temperature': 'Temp'}, inplace=True)


# In[85]:


features_df.head()


# In[86]:


features_df.dtypes
# in Panda 'object' is a 'string' data type


# <h1>Indexing and Series Functions</h1>
# 
# <ul>
#     <li>Columns of a DataFrame can be accessed through the following format: df_name["name_of_column"] </li>
#     <li>Columns will be returned as a Series, which have different methods than DataFrames </li>
#     <li>A couple useful Series functions: max(), median(), min(), value_counts(), sort_values()</li>
# </ul>

# In[87]:


features_df.head()


# In[88]:


features_df['CPI']


# In[89]:


features_df.fillna(0)


# In[90]:


features_df["CPI"].max()


# In[91]:


features_df["CPI"].min()


# In[92]:


features_df["CPI"].median()


# In[93]:


features_df["Store"].unique()
#shows the distinct values in a column


# In[97]:


features_df['Date'].value_counts()


# In[100]:


features_df.drop(columns="MD1").head()


# In[105]:


features_df.drop(columns=["MD1", "MD2", "MD3", "MD4", "MD5"], inplace = True)
# inplace = True stores the data back into the dataframe
# You can only drop something once or else if you run it again an error will occur since it can't be found


# In[107]:


features_df.head()


# <h1>Indexing</h1>
# 
# <ul>
#     <li>Because Pandas will select entries based on column values by default, selecting data based on row values requires the use of the iloc method. 
#     </li>
#     <li>
#       Allowed inputs are:
#         <ul>
#             <li>An integer, e.g. 5.</li>
#             <li>A list or array of integers, e.g. [4, 3, 0].</li>
#             <li>A slice object with ints, e.g. 1:7.</li>
#         </ul>
#     </li>
# </ul>

# In[106]:


features_df.loc[0:10, "Fuel Price":"IsHoliday"]


# In[109]:


features_df.iloc[[0,1], [1,3]]
# iloc = integer location
# first [] gives the rows and second [] gives the columns


# <h1>Formatting Data</h1>
# 
# <ul>
#     <li>To access and format the string values of a DataFrame, we can access methods within the "str" module of the DataFrame </li>
#     <li>We may also format float values using options.display.float_format() in Pandas</li>
# </ul>

# In[110]:


new = features_df['Date'].str.split("-", expand=True)
# splits the values in separate columns
new.head()


# In[111]:


"2010-02-05".split("-")


# In[112]:


features_df["Year"] = new[0]
features_df["Month"] = new[1]
# adds columns to the dataframe


# In[113]:


features_df.head()


# In[116]:


features_df.to_csv('features_pandas.csv')
features_df.to_excel('features_pandas.xlsx')


# <h1>Conditional Indexing</h1>
# 
# <ul>
#     <li>Conditional Operators (>, ==, >=) can be used to return rows based on their values </li>
#     <li>Bitwise Operators (|, &) can be used to combine conditonal statements</li>
# </ul>

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


##CLASS EXERCISE 
# find the rows with Fuel_Price larger than 3.00 AND IsHoliday is True

# find the rows with CPI < 200  OR Unemployment < 5


# In[ ]:





# In[ ]:




