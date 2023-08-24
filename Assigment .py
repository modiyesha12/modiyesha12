#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Q1. How will you reverse a list?

l1 = ["apple","chiku","mango","guavav"]
l1[::-1]




## Q2How will you remove last object from a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

l2= [2, 33, 222, 14,25]
print(l2[-1])


# In[4]:


print(l2[:-1])


# In[12]:


## Write a Python function to get the largest number, smallest num and sumof all from a list. 

print(l2)
print(min(l2))
print(max(l2))
print(sum(l2))


# In[14]:


##Write a Python program to remove duplicates from a list. 
x = [2, 4, 10, 20, 5, 2, 20, 4]
print(x)
unique= set(x) ## duplicate values are not allowed in sets 
print(unique)


# In[17]:


## Write a Python program to check a list is empty or not. 
x= [1,2,3,4,5]
if len(x)==0:
    print("empty list")
else:
    print("list is not empty")


# In[27]:


## Write a Python function that takes two lists and returns true if they have at least one common member

def data(x,y):
    result = False
    for l1 in x:
        for l2 in y:
            if l1 == l2:
                result = True
                return result
print(data([1,2,3,4,5],[1,4,5,6,7]))







