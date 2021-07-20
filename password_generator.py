#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing the required modules
import string 
import random


# In[ ]:


# length of password required
n = int(input("Length of password: "))

# adding the variables required to build a password
lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
num = string.digits
punc = string.punctuation

# char is the combined data used to build a password from the above variables
char = lowerCase + upperCase + num + punc

# forming a password in list format using the random module 
password_list = random.sample(char,n)

# changing the password in list to string format
password = ''.join(password_list)

# printing the password generated
print(password)

