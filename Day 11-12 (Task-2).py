#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Write a program in Python to perform the following operation:
#If a number is divisible by 3 it should print “Consultadd” as a string
#If a number is divisible by 5 it should print “c” as a string
#If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.

x = 9
if (x/3):
    print("consultadd")
else:
    print("not divisble")
y = 15
if(y/5):
    print("c")
z = 15
if (x/3,x/5):
    print("Consultadd python training")
else: 
    print("not divisble")


# In[1]:


#Write a program in Python to perform the following operator based task:
#Ask user to choose the following option first:
#If User Enter 1 - Addition 
#If User Enter 2 - Subtraction
#If User Enter 3 - Division
#If USer Enter 4 - Multiplication
#If User Enter 5 - Average
#Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
#Ask user to enter two more numbers as first1 and second2 for calculating the average as soon as user choose an option 5.
#At the end if the answer of any operation is Negative print a statement saying “zsa”
#NOTE: At a time user can perform one action at a time.

option = input("Enter from option 1,2,3,4,5: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if option == '1':
    sum = float(num1) + float(num2)
    print(sum)
elif option == '2':
    (num1-num2)
elif option == '3':
    print(num1/num2)
elif option == '4':
    print(num1*num2)
elif option == '5':
    print(num1+num2/2)

   


# In[2]:


#Write a program in Python to implement the given flowchart:
a=10
b=20
c=30
avg=(a+b+c)/3
print("avg=", avg)
if(avg>a and avg>b and avg>c):
    print("avg is higher than a,b,c")
else:
    if(avg>a and avg>b):
        print("avg is higher than a,b,c")
    elif(avg>a and avg>c):
        print("avg is higher than a,c")
    elif(avg>b and avg>c):
        print("avg is higher than b,c")
    elif(avg>a):
        print("avg is just higher than a")
    elif(avg>b):
        print("avg is just highr than b")
    elif(avg>c):
        print("avg is just higher than c")


# In[7]:


# Write a program in Python to break and continue if the following cases occurs:
#If user enters a negative number just break the loop and print “It’s Over”
#If user enters a positive number just continue in the loop and print “Good Going”
while True:
    x= int(input("Enter a number :"))
    if(x<0):
         break
    print("It’s Over")




# In[ ]:


#write a program in Python which will find all such numbers which are divisible  by 7 but are not a multiple of 5, 
#between 2000 and 3200.


# In[10]:


for x in range(2000,3200):
    if x%7==0 and x%5!=0:
        print(x)


# In[12]:


# What is the output of the following code examples?
x=123 
for i in x:
    print(i)


# In[15]:


i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("error")


# In[17]:


count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break


# In[3]:


# Write a program that prints all the numbers from 0 to 6 except 3 and 6.
for x in range(6):
    if (x == 3 or x==6):
        continue
        print(x)

        
        
        


# In[ ]:


# Write a program that accepts a string as an input from user and calculate the number of digits and letters.
#Expected output: consul12
#Letters 6
#Digits 2

