#!/usr/bin/env python
# coding: utf-8

# # Problem 1 Solution

# In[86]:


s = "Happy new year 😂😂😂2021"

print(s[::-1])


# # Problem 2 Solution

# In[141]:


lst = [1, 21, 3, 16, 15, 0, 7, 6]
n = 1
lst = sorted(lst)
s = 0
l = len(lst)-1
found = False
for i in range(s,l):
    if(lst[s]+lst[l] == n):
        print(lst[s],lst[l])
        print(lst[s]+lst[l])
        found = True
    elif(lst[s]+lst[l] < n):
               s += 1
    else:
               l -= 1
               
        
if found == False:
    print("No Such Elements")
else:
    print("Found")


# # Problem 3 Solution

# In[140]:


a = ['add', 'dad', 'god', 'dog', 'vile', 'live', 'evil', 'odd']
dict = {}

for i in a:
    key = ''.join(sorted(i))
    if key in dict.keys():
        dict[key].append(i)
    else:
        dict[key] = []
        dict[key].append(i)
for key, value in dict.items():
    print(value)


# In[72]:





# In[ ]:




