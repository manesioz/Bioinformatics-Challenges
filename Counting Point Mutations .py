
# coding: utf-8

# In[1]:


#this program computes the Hamming Distance of two homologous and equal length DNA strands 

def hamming_dist(s, t): 
    num = 0
    for i in range(len(s)): 
        if s[i] == t[i]: 
            num += 1
    return (len(s) - num)

