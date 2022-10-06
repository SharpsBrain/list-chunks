#!/usr/bin/env python
# coding: utf-8

# In[4]:


my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky','nerdy', 'geek', 'love',
               'questions','words', 'life']
 
# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]
 
# How many elements each
# list should have
n = 6
 
x = list(divide_chunks(my_list, n))
print (x)


# In[7]:


my_list = [1, 2, 3, 4, 5,
           6, 7, 8, 9]
start = 0
end = 12
step = 3
for i in range(start, end, step):
    x = i
    print(my_list[x:x+step])


# In[ ]:




