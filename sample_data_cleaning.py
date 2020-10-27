#!/usr/bin/env python
# coding: utf-8

# # DATA Cleaning

# In[1]:


import pandas as pd
import numpy as np


# ## load raw data with first row header , and skip the first row

# In[2]:


my_data=pd.read_excel(r"C:\Users\venuk\OneDrive\Desktop\assignment\Sample Data.xlsx",skiprows=1)


# In[3]:


my_data_rows=my_data.head(0)
my_data_rows=list(my_data_rows)


# In[4]:


my_data.columns = [''] * len(my_data.columns)


# In[5]:


my_data.columns=my_data_rows


# In[6]:


my_data.head()


# In[7]:


## we have to remove / in BP column and make it 2 seperate columns BP_Systolic BP_Diastloic


# In[8]:


## BP variable is in the form 120/80  so we have do 2 seperate columns , 120 and 80 in each


# In[9]:


my_data["BP"][:5]


# In[10]:


BP_Systolic=[]
BP_Diastloic=[]
for i in range(0,25):
    output=my_data["BP"][i].split('/',1)
    BP_Systolic.append(output[0])
    BP_Diastloic.append(output[1])


# In[11]:


BP_Systolic[:10]


# In[12]:


len(BP_Diastloic)


# In[13]:


my_data["BP_Diastloic"]=BP_Diastloic


# In[14]:


my_data["BP_Systolic"]=BP_Systolic


# In[15]:


my_data=my_data.drop("BP",1)    #dropping the BP column


# In[16]:


my_data.columns


# In[17]:


# dose we have ml and mg so seperate into 2 columns


# In[18]:


my_data["Dose"][:5]


# In[19]:


mg_data=[]
ml_data=[]
ml_output=[]


# In[20]:


for i in range(0,25):
    if str(my_data["Dose"][i]).endswith("ml"):
        ml_data.append(my_data["Dose"][i])
    else:
        ml_data.append("NA")


# In[21]:


len(ml_data)


# In[22]:


for i in range(0,25):
    if str(my_data["Dose"][i]).endswith("mg"):
        mg_data.append(my_data["Dose"][i])
    else:
        mg_data.append("NA")


# In[23]:


#mg_data


# In[24]:


my_data_filter=pd.DataFrame({"mg_data":mg_data,"ml_data":ml_data})


# In[25]:


#my_data_filter


# In[26]:


mg_list=[]
ml_list=[]


# In[27]:


for i in range(0,25):
    output=my_data_filter["mg_data"][i].replace('mg',"")
    mg_list.append(output)


# In[28]:


len(mg_list)


# In[29]:


for i in range(0,25):
    output=my_data_filter["ml_data"][i].replace('ml',"")
    ml_list.append(output)


# In[30]:


len(ml_list)


# In[31]:


my_data["Dose_in_ml"]=ml_list
my_data["Dose_in_mg"]=mg_list


# In[32]:


my_data=my_data.drop("Dose",1)


# In[33]:


# In order type we have multiple orders in one columns so split and make each column for medicine,Diagnostic and  others


# In[34]:


my_data["Order Type"].value_counts()


# In[35]:


med=[]
Dia=[]
others=[]


# In[36]:


for i in range(0,25):
    if my_data["Order Type"][i] in ["Medicine","Medicine , Diagnostic","Medicine , Diagnostic, Other"]:
        med.append("Y")
    else:
        med.append("NA")


# In[37]:


#med


# In[38]:


for i in range(0,25):
    if my_data["Order Type"][i] in ["Diagnostic","Medicine , Diagnostic","Medicine , Diagnostic, Other"]:
        Dia.append("Y")
    else:
        Dia.append("NA")


# In[39]:


#Dia


# In[40]:


for i in range(0,25):
    if my_data["Order Type"][i] in ["Other","Medicine , Diagnostic, Other"]:
        others.append("Y")
    else:
        others.append("NA")


# In[41]:


#others


# In[42]:


my_data["Diagnostic"]=Dia
my_data["Medicine"]=med
my_data["Other"]=others


# In[43]:


my_data.head()


# In[44]:


my_data=my_data.drop("Order Type",1)


# In[45]:


## convert categorical to numerical 


# In[46]:


my_data["Order Name"].value_counts()


# In[47]:


my_data["Order Name"]=pd.factorize(my_data["Order Name"])[0]


# In[48]:


#my_data["Order Name"]


# In[49]:


#my_data.columns


# In[50]:


my_data=my_data[["Patient Name"  ,  "SSN",   "Age"  , "Gender", "Pregnant" , "Address"   ,  
 "Allergy With"  ,  "Allergy Affects" ,"Insurance Name",  "Insurance Id",   
 "Health issue" ,   "Patient Type"  ,  "Order Name",      "Order Set name", "Medicine",     
 "Diagnostic"    ,  "Other" , "Temperature"  ,  
 "BP_Systolic"    , "BP_Diastloic"  ,  "Heart Rate"  ,    "Heart Issues"  ,  "Diabetic"     ,  
"Cancer" ,  "Medicine Name"  ,"Dose_in_ml",     
"Dose_in_mg" ,  "Route" ,       "Frequency"]]


# In[51]:


my_data.head()


# In[52]:


my_data.to_csv("after_cleaning.csv")

