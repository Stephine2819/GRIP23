#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# ### Question 1: Car Matrix Generation

# In[2]:


data = pd.read_csv (r"C:\Users\HP\Downloads\dataset-1.csv")
data


# In[8]:


def generate_car_matrix(data):
    car_matrix = data.pivot_table(index='id_1', columns='id_2', values='car', fill_value=0)
    np.fill_diagonal(car_matrix.values, 0)   
    return car_matrix

# Under the function generate_car_matrix created a dataframe car_matrix with id_1 as index, id_2 as columns 
# and the car values from the data as values then replaced the diagonals with 0.
data = pd.read_csv(r"C:\Users\HP\Downloads\dataset-1.csv")
result = generate_car_matrix(data)
result


# ## Question 2: Car Type Count Calculation

# In[4]:


def get_type_count(data):
    data.loc[data['car'] <= 15, 'car_type'] = 'low'
    data.loc[(15 < data['car']) & (data['car'] <= 25), 'car_type'] = 'medium'
    data.loc[data['car'] > 25, 'car_type'] = 'high'
    type_counts = data['car_type'].value_counts().to_dict()
    sorted_counts = dict(sorted(type_counts.items()))
        
    return sorted_counts

# classified cars into three types 'low', 'medium' and 'high' based on their numerical values in the car column.
# Then counted the occurrences of each car type and return a dictionary with sorted countsin ascending order.

data = pd.read_csv (r"C:\Users\HP\Downloads\dataset-1.csv")
result = get_type_count(data)
print(result)


# ### Question 3: Bus Count Index Retrieval

# In[5]:


def get_bus_indexes(data):
    mean = data['bus'].mean()
    indices = data[data['bus'] > 2 * mean].index.tolist()
    indices.sort()
    
    return indices
# Calculated the mean value of the 'bus' column
# Identified indices where 'bus' values are greater than twice the mean and sorted the indices in ascending order


data = pd.read_csv(r"C:\Users\HP\Downloads\dataset-1.csv")
result = get_bus_indexes(data)
print(result)


# ### Question 4: Route Filtering

# In[57]:


def filter_routes(data):
    # Group by 'route' and calculate the average of the 'truck' column
    avg = data.groupby('route')['truck'].mean()
    
    # Filter routes where the average truck value is greater than 7
    list = avg[avg > 7].index.tolist()
    
    # Sort the list of routes
    list.sort()
    
    return list

# Read the CSV file into a DataFrame
data = pd.read_csv(r"C:\Users\HP\Downloads\dataset-1.csv")

# Call the function with the DataFrame
result = filter_routes(data)

# Display the result
print(result)


# ## Question 5: Matrix Value Modification

# In[9]:


def multiply_matrix(data):
    matrix=data.copy() 
    matrix = matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    matrix =matrix.round(1)
    return matrix
#The function takes a DataFrame and creates a copy with each element in the DataFrame multiplied by 0.75 if the value is greater than 20 and by 1.25 otherwise.
#Finally, it rounds all the values in the DataFrame to one decimal place.
data = result.copy()
multiply_matrix(data)


# ## Question 6: Time Check

# In[80]:


data = pd.read_csv (r"C:\Users\HP\Downloads\dataset-2.csv")
data

