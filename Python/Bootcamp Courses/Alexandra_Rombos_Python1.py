#!/usr/bin/env python
# coding: utf-8

# <h1>Python 1 - Overview</h1>
# <p>
#   Bootcamp will cover Python fundamentals while making a music playlist program
# </p>
# <ul>
# <li>Evaluating primitive types in python: type()</li>
# <li>Declaring variables and variable declaration conventions: =</li>
# <li>Math Operators and string concatenation: (+ , - , * , /,%)</li>
# <li>IF and WHILE statements with conditional operators: (==, >, >=, break)</li>
# <li>User input: input()</li>
# <li>Data collections - Lists: ([ ], append(), insert(), del, pop(), len(), sort())</li>
# <li>Data collections - Dictionaries: ({ },[ ], insert(), del, clear(), keys(), values())</li>
# <li>Declaring custom functions: def, return</li>
# <li>Classes and object oriented programming: class(), __init__(), methods</li>
# <li>Automating with FOR loops: for, in</li>

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

# <h1>Data Types</h1>
# <ul>
#   <li>
#    Four primitive types in Python
#     <ol>
#       <li>
#         Integers
#       </li>
#       <li>
#         Booleans
#       </li>
#       <li>
#         Floats
#       </li>
#       <li>
#         Strings
#       </li>
#     </ol>
#  <li>
#    Types may be changed using int(), str(), float(), and bool() methods    
#  </li>
# </ul>

# In[1]:


# The code to output the type of data for the number 3 has already been filled in for you as an example.
type(3)


# In[2]:


type(3.00)


# In[3]:


type(False)


# In[4]:


type('Hello World!')


# <h1>Variables</h1>
# <ul>
#   <li>
#     May consist of letters, numbers, and underscores, but not spaces.
#     <ul>
#       <li>
#         <b>Cannot start with a number.</b>
#       </li>
#     </ul>
#   </li>
#   <li>
#     Avoid using Python keywords (for, if, and, or, etc.)
# </li>
#   <li>
#     Be careful when using 1s and lower case ls, as well as 0s and Os.
# </li>
#   <li>
#     Keep it short.
#   <li>
#     Example: phone_num = 647606
# </li>
#     
# </ul>

# In[5]:


# Assign a value of 10 to a variable named hours_worked
hours_worked = 10


# In[6]:


# Use the print() function to print the number of hours worked 
print(hours_worked)


# In[7]:


current_time= 9.5


# <h1>Math Operators</h1>
# <ul>
#   <li>
#     Addition, Subtration, Multiplication and Division may be done using basic math operators (+ , - , * , /,%).
#   </li>
#   <li>
#     Many built-in string methods (title, upper, lower, index, split).
#   </li>
#   <li>
#     Python will also try to interpret your code with other data types
#   </li>
#   <ul><li>(+) may be used with strings!</li></ul>
# </ul>

# In[8]:


# Create two variables, price1 and price2 that have float values representing the respective price of two items
price1 = 3.40
price2 = 2.51
# Create a new variable whose value is the sum of the duration of both songs. Print the sum
tot_price = price1 + price2


# In[9]:


print(tot_price)


# In[10]:


name = 'peter'
job = 'works with'
tool = 'python'


# In[11]:


# We can concatenate (combine) strings together using the addition (+) symbol 
employment = name + ' ' + job + ' ' + tool
print(employment)


# In[12]:


num = 3


# In[13]:


python_string = tool + ' ' + str(num)
print(python_string)


# In[14]:


price1 = 3.40
price2 = 2.51
price_multi = price1 * price2
print(price_multi)
print(employment)
print(employment.title())
print(employment.lower())
print(employment.upper())
print(employment.index('works'))
print(employment.split(' '))
print(employment.replace('python', 'Finance'))


# <h1>IF and WHILE Statements</h1>
# <ul>
#   <li>
#     Will only run indented code if condition is true
#   <li>
#     Make use of <b>conditional operators</b> to create tests
#   </li>
#   <ul><li>(==) will return true if both variables are equal</li>
#   <li>(>) will return true if left variable is larger</li>
#   <li>(>=) will return if left variable is larger or equal to right variable</li></ul>
#   <li>IF will only run indented code once, WHILE will run indented code until condition is no longer true</li>
# </ul>

# In[15]:


yes = True
no = False

if yes: 
    print('This statement will print')
    print('This statement will also print')
    
if no:
    print('This statement will not print')


# In[16]:


num_employees = 1
if num_employees < 5:
    print('Employee Added!')


# In[17]:


dept_size = 10


# In[18]:


if dept_size < 16:
    print(f"New Hire. {dept_size} employees in department") # "f" formats the string so the value of dept_size can be printed
    dept_size += 1

elif dept_size < 18:
    print(f"It's getting cramped in here! {dept_size} employees in department")
    dept_size += 1

else:
    print("Size exceeded. New offices needed!")


# In[19]:


print('Peters "Laptop"')


# In[20]:


dept_size = 0
limit = 10
while dept_size < limit:
    print(dept_size)
    dept_size += 1


# In[21]:


while True:
    if dept_size == 20:
        break
    print(dept_size)
    dept_size += 1
    
print('Exited!')


# <h1>Lists</h1>
# <ul>
#   <li>
#    Collection of items in a particular order
#   <li>
#    Indexing (order) starts from <b>0</b>
#   </li>
#   <li>Accessing items in a list can be done with square brackets ([ ])</li>
#   <li>Items can be easily added to lists using append() and insert() methods</li>
# </ul>

# In[22]:


banks = ["RBC", "CIBC", "TD", "BMO"]
print(banks)
print(banks[0])
print(banks[3])
print(banks[0:3]) # Prints up until 3 (in this case at positions 0, 1, and 2
print(banks[:1]) # Starts at index 0
print(banks[1:]) # Includes the last value since it is empty
print(banks[-1]) # Counts backwards --> prints the last value at index -1
banks[0] = 'Scotiabank'
print(banks)


# In[23]:


banks.append("RBC")
print(banks)


# In[24]:


banks.insert(1, "FNBC")
print(banks)


# In[25]:


print(len(banks)) # List size
del(banks[1])
print(banks)


# In[26]:


last_bank = banks.pop()
print(last_bank)


# In[27]:


mix_list = ["Peter", 31445, True, 'IT']
print(mix_list)
print(mix_list[2])


# In[28]:


print(f"{mix_list[0]} employee number: {mix_list[1]} - Dept:{mix_list[3]}")


# <h1>Dictionaries</h1>
# <ul>
#   <li>
#    Collection of key-value pairs
#   <li>
#    No positions as with lists, values stored at specific key
#     <ul><li>keys can be of any data type</li></ul>
#   </li>
#   <li>Accessing values in a dictionary can still be done with square brackets ([ ])</li>
#   <li>Declared using braces ({ })</li>
# </ul>

# In[29]:


employee = {'name':'Peter', 'employee_num':'31445', 'department':'IT'}
print(employee)


# In[30]:


print(employee['name']) # Must use the name of the key, not a number


# In[31]:


employee['department'] = 'Finance'
print(employee)


# In[32]:


employee['management'] = False
print(employee)


# In[33]:


print(employee.items())
print(employee.keys())
print(employee.values())


# In[34]:


if 'name' in employee.keys():
    print('yes, name is in one of the keys')
else:
    print("Not a keys")


# In[35]:


mix_list = ["Peter", 31445, True, 'IT']

if 'IT' in mix_list:
    print("YES!")
    
else:
    print('NO')


# <h1>For Loops</h1>
# <ul>
#   <li>
#    Execute a block of code once for each item in collection (List/Dictionary)
#   <li>
#    Declare temporary variable to iterate through collection
#   </li>
#   <li>Can be used in combination with IF statements</li>
# </ul>

# In[36]:


for bank in banks:
    print(bank)
    
for key, value in employee.items():
    print(f"{key}:{value}")


# In[37]:


banks = ["RBC", "CIBC", "TD", "BMO"]
print(banks)


# In[38]:


for i in range(10):
    print(i)


# <h1>Functions</h1>
# <ul>
#   <li>
#    Named blocks of code that do one specific job
#   <li>
#    Functions are also referred to as methods
#   <li>
#    Prevents rewriting of code that accomplishes the same task
#   </li>
#   <li>Keyword <i>def</i> used to declare functions</li>
#   <li>Variables may be passed to functions</li>
# </ul>

# In[39]:


def greeting():
    print('Hi!')

greeting()


# In[40]:


def descriptive_name(name, employee_num, department):
    print(f"{name}. Employee num: {employee_num} - Dept: {department}")

descriptive_name('Peter', 31445, 'IT')
descriptive_name('Mike', 22110, 'Marketing')


# <h1>Classes</h1>
# <ul>
#   <li>
#   Object-orientated programming approach popular and efficient
#   </li>
#   <li>
#    Define classes of real-world things or situations
#     <ul>
#       <li>Attributes of various data types</li>
#       <li>Functions inside of a class are the same except called methods</li>
#       <li>Methods may be accessed using the dot operator</li>
#     </ul>
#   </li>
#   <li>Instanciate objects of your classes</li>
#   <li>__init()__ method used to prefill attributes</li>
#   <li>Capitalize class names</li>
# </ul>

# In[41]:


class Employee():
    def __init__(self, name, employee_num, department):
        self.name = name
        self.employee_num = employee_num
        self.department = department
    def descriptive_name(self):
        print(f'{self.name}. Employee num: {self.employee_num} - Dept: {self.department}')


# In[42]:


employee1 = Employee('Peter', 31445, 'IT')
employee2 = Employee('Mike', 22044, 'Finance')

employee1.descriptive_name()


# <h1>User Input</h1>
# <ul>
#   <li>
#      Pauses your program and waits for the user to enter some text
#   <li>
#     Variable used with Input() will be a <b>string</b> even if user inputs an integer
#   </li>
#   <ul><li>Will need to make use of type casting</li></ul>
# </ul>

# In[43]:


my_age = input('Enter your age:\n')
print(my_age)
print(f"Your age is {my_age})


# 
# <h1>Putting It All Together</h1>
# 

# In[ ]:





# In[ ]:





# In[ ]:




