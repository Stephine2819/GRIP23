#!/usr/bin/env python
# coding: utf-8

# ### Question 1: Distance Matrix Calculation

# In[1]:


import pandas as pd
data = pd.read_csv (r"C:\Users\HP\Downloads\dataset-3.csv")
data


# In[2]:


def calculate_distance_matrix(data):
    all_ids =  pd.concat([data['id_start'], data['id_end']]).unique()
    distance_matrix = pd.DataFrame(index=all_ids, columns=all_ids, dtype=float)
    distance_matrix = distance_matrix.fillna(0) 
    for _, row in data.iterrows():
        distance_matrix.at[row['id_start'], row['id_end']] = row['distance']

    
    for k in all_ids:
        for i in all_ids:
            for j in all_ids:
                if distance_matrix.at[i, k] > 0 and distance_matrix.at[k, j] > 0:
                    if distance_matrix.at[i, j] == 0 or distance_matrix.at[i, k] + distance_matrix.at[k, j] < distance_matrix.at[i, j]:
                        distance_matrix.at[i, j] = distance_matrix.at[i, k] + distance_matrix.at[k, j]

    return distance_matrix

# Created a matrix with all unique IDs as both row and column indices.
# Initialized the matrix with zeros and filling it with the distances provided in the dataset.
# Applying the Floyd-Warshall algorithm to update the distances between all pairs of locations, considering intermediate locations (k).

data = pd.read_csv(r"C:\Users\HP\Downloads\dataset-3.csv")
result = calculate_distance_matrix(data)
result = result + result.T.where(~result.T.isna(), 0)# applying the same values to the lower traingle
print(result)


# ### Question 2: Unroll Distance Matrix

# In[3]:


def unroll_distance_matrix(distance_matrix):
    unrolled_distances = pd.DataFrame(columns=['id_start', 'id_end', 'distance'])
    for i in distance_matrix.index:
        for j in distance_matrix.columns:
            if i != j:
                unrolled_distances = unrolled_distances.append({
                    'id_start': i,
                    'id_end': j,
                    'distance': distance_matrix.at[i, j]
                }, ignore_index=True)

    return unrolled_distances

#Created an empty DataFrame with required columns distance values from the input distance_matrix.
#The function then iterates through the rows and columns of the input to check if i is not equal to j to avoid adding distances from the same location to itself.
#For each valid combination of i and j, the function appends a new row to the unrolled_distances DataFrame containing 'id_start', 'id_end', and 'distance'.

data = pd.read_csv (r"C:\Users\HP\Downloads\dataset-3.csv")
t = unroll_distance_matrix(result)
t['id_start'] = t['id_start'].astype(int)
t['id_end'] = t['id_end'].astype(int)
#Filtered the data that was already present in data
mask = ~t[['id_start', 'id_end']].isin(data[['id_start', 'id_end']]).all(axis=1)
filtered_result = t[mask]
print(filtered_result)


# ### Question 3: Finding IDs within Percentage Threshold

# In[4]:


def find_ids_within_ten_percentage_threshold(data, reference_value):
    reference_data = data[data['id_start'] == reference_value]
    average_distance = reference_data['distance'].mean()
    threshold = 0.1 * average_distance
    filtered_data = data[
        (data['distance'] >= (average_distance - threshold)) &
        (data['distance'] <= (average_distance + threshold))
    ]
    result = sorted(filtered_data['id_start'].unique())

    return result

#Function selects a subset of the DataFrame where the 'id_start' column is equal to a specified reference value which creates a new DataFrame containing only rows where the 'id_start' matches the reference value.
#Average distance from the 'distance' column and threshold value is calculated to include only those rows where the distance falls within the range of (average distance - threshold) to (average distance + threshold) and then extracting unique values

data = filtered_result.copy()
reference_value = 1001406  
result_within_threshold = find_ids_within_ten_percentage_threshold(data, reference_value)
print(result_within_threshold)


# ### Question 4: Calculate Toll Rate

# In[5]:


def calculate_toll_rate(data):
    vehicle_types = ['moto', 'car', 'rv', 'bus', 'truck']
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}
    for vehicle_type in vehicle_types:
        data[vehicle_type] = data['distance'] * rate_coefficients[vehicle_type]

    return data
# Created columns for each vehicle type with their rate coefficients
# Iterated through each vehicle type and calculated toll rates
data= filtered_result.copy()
calculate_toll_rate(data)

