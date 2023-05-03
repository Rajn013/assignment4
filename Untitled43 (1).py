#!/usr/bin/env python
# coding: utf-8

#  1 What exactly is []

# an empty list, which is a data structure that can hold a collection of elements, but with no elements in it initially.

# 2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)

# In[15]:


spam = [2,4,6,8,10]
spam[2] = 'hello'
spam


# Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
# 

# 3. What is the value of spam[int(int('3' * 2) / 11)]?

# In[18]:


spam = ['a','b','c','d']
spam[int(int('3'*2) / 11)]


# 4. What is the value of spam[-1]?

# In[19]:


spam[-1]


# 5. What is the value of spam[:2]?

# In[20]:


spam[:2]


# Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.
# 6. What is the value of bacon.index('cat')?

# In[23]:


bacon = [3.14, 'cat', 11 , 'cat', True]
bacon.index('cat')


# 7. How does bacon.append(99) change the look of the list value in bacon?

# In[24]:


bacon.append(89)
bacon


# 8. How does bacon.remove('cat') change the look of the list in bacon?

# In[25]:


bacon.remove('cat')
bacon


# 9. What are the list concatenation and list replication operators?

# In[26]:


R1 = [1,4]
R2 = [2,5]

R1+R2


# In[28]:


R1 = [3,5]

R1*3


# 10. What is difference between the list methods append() and insert()?

# In[29]:


bacon.append(99)
bacon


# In[30]:


spam.insert(2,'hello')
spam


# 11. What are the two methods for removing items from a list?

# In[34]:


bacon = [3.14, 'cat', 11 , 'cat', True]
bacon.remove('cat')
bacon


# In[35]:


bacon.pop()
bacon


# 12. Describe how list values and string values are identical.

# Both lists and strings can be passed to len()
# Have indexes and slices
# Can be used in for loops
# Can be concatenated or replicated
# Can be used with the in and not in operators

# 13.What's the difference between tuples and lists?

# Lists : are mutable - they can have values added, removed, or changed. lists use the square brackets.
# Tuples : are immutable; they cannot be changed at all. Tuples are written using parentheses.

# 14.How do you type a tuple value that only contains the integer 42?
# 

# In[36]:


tuple =(42)
tuple


# 15.How do you get a list value's tuple form? How do you get a tuple value's list form?

# In[1]:


R1= [1,2,3,4,5,6,7]
L1 =tuple(R1)
L1


# In[2]:


P1 = [7,6,5,4,3,2,1]
P = list(P1)
P


# .16Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
# 
# ans They contain references to list values.

# 17.How do you distinguish between copy.copy() and copy.deepcopy()?
# 
# 
# Ans . The copy.copy() function will do a shallow copy of a list,
# The copy.deepcopy() function will do a deep copy of a list. only copy.deepcopy() will duplicate any lists inside the list

# In[ ]:




