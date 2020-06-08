#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Swap two numbers using the third variable as the result name and do the same task without using any third variable.
x = 3
y = 4
z = x 
x = y 
y = z
print(x,y)
x = 4
y = 4
x, y = y, x 
print (x, y) 


# In[8]:


#Create three variables in a single a line and assign different values to them and make sure their data types are different.
#Like one is int, another one is float and the last one is a string.
x = 2
y = 4.5
z = "Raees"
print(x,y,z)


# In[6]:


# Create a variable of value type complex and swap it with another variable whose value is an integer.
x = 2+3j
y = 10
x, y = y, x 
print (x, y) 


# In[6]:


# Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.
y = (raw_input("Enter the value"))
print(y)
x = (input("Enter the value:"))
print(x)


# In[2]:


# Write a program to complete the task given below:
# Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
# Use z for adding 30 into it and print the final result by using variable result.
x = int(input("Enter any digit inbetween:(1-10)"))
print(x)
y = int(input("Enter any digit inbetween:(1-10)"))
print(y)
z = x+y
print(z)
result = z+30
print(result)


# In[20]:


#Write a program to check the data type of the entered values. HINT: Printed output should say 
#The input value data type is: int/float/string/etc
x = 3
print("The input value data type is")
type(x)


# In[22]:


# If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. 
# Will it change the value.If Yes then Why?
a = 10
print(a)
a = 45.5
print(a)
# It over writes the new value everytime.


# In[ ]:




