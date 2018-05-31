
# coding: utf-8

# In[1]:


#this program computes the concentration of nitrogenous bases guanine and cytosine in a given DNA strand 

def GC_content(x): 
    num = 0 
    for i in range(len(x)): 
        if (x[i] == "G") or (x[i] == "C"): 
            num += 1 
    return (num/len(x))*100
    

