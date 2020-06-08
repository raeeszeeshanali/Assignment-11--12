#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.
x =[1,2.0,3+2j]
print(x)


# In[11]:


#Create a list of size 5 and execute the slicing structure 
a = [1,2,3,4,5]
x = slice(2)
print(a[x])


# In[18]:


# Write a program to get the sum and multiply of all the items in a given list.
x =[1,2,3,4,5]
y=sum(x)
print(y)
for z in x:
    z*=z
print(z)


# In[20]:


#Find the largest and smallest number from a given list.
x = [2,4,5,8,9]
print(max(x))
print(min(x))


# In[26]:


#Create a new list which contains the specified numbers after removing the even numbers from a predefined list. 

x = [4,5,7,8,9]
for i in x:
    if (i%2==0):
        x.remove(i)
print(x)


# In[60]:


# Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)

y = [ x**2 for x in range(1,30)]
x = y[:5] + y[-5:]
print(x)


# In[41]:


# Write a program to replace the last element in a list with another list.
#Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
#Expected output: [1,3,5,7,9,2,4,6,8]

x = [1,3,5,7,9,10]
y = [2,4,6,8]
x[-1:] = y
print(x)


# In[62]:


# Create a new dictionary by concatenating the following two dictionaries:
#a={1:10,2:20}
#b={3:30,4:40}
#Expected Result: {1:10,2:20,3:30,4:40}

a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)


# In[73]:


# Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
#Sample data (n=5)
#Expected Output: {1:1,2:4,3:9,4:16,5:25}

n=5
x = dict()
for x in range(1,n+1):
    d[x]=x*x

print(d) 


# In[ ]:


# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple 
# which contains every number. Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# The output should be:
#[‘34’,’67’,’55’,’33’,’12’,’98’]

values = input("Enter comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


# In[ ]:




