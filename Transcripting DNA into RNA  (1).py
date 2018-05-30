
# coding: utf-8

# In[3]:


#this program take a string representing the nucleotide bases of at DNA strand and outputs the transcript RNA strand 

def transcript(x): 
    list1 = list(x)
    for i in range(len(x)): 
        if list1[i] == "T": 
            list1[i] = "U"
            
    return "".join(list1)

