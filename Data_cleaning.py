import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
#import os
#commit test

df = pd.read_csv('uae_real_estate_2024.csv')
# Elimination of non verified entries, and droping of non relevant columns
print(f'Initial number of data rows: {df.shape[0]}')
df = df[df['verified']]
print(f'Number of Verified data rows: {df.shape[0]}')
df = df.drop(['addedOn', 'type', 'priceDuration', 'description', 'verified'], axis='columns')

# Sqft to m2 convertion
df['sizeMin'] = df['sizeMin'].str.replace('sqft', '').astype(float)
df['sizeMin'] = df['sizeMin'] * 0.092903
df['sizeMin'] = df['sizeMin'].astype(int)

# Currency convertion to Euro
df['price'] = df['price'] * 0.24
df['price'] = df['price'].astype(int)

# Price per m2 column creation
df['price_per_m2'] = df['price']/df['sizeMin']
df['price_per_m2'] = df['price_per_m2'].astype(int)

# Convertion of values 'studio' in 'bedrooms' and 7+ in 'bathrooms' columns
df['bedrooms'] = df['bedrooms'].replace('studio', 0)
df['bedrooms'] = df['bedrooms'].replace('7+', 7)
df['bedrooms'] = pd.to_numeric(df['bedrooms'], errors='coerce').fillna(0).astype('int64')

df['bathrooms'] = df['bathrooms'].replace('7+', 7)
df['bathrooms'] = pd.to_numeric(df['bathrooms'], errors='coerce').fillna(0).astype('int64')

df['furnishing'] = df['furnishing'].astype(str)
df['furnishing'] = df['furnishing'].replace('PARTLY', 'NO')
df['furnishing'] = df['furnishing'].replace('YES', 1)
df['furnishing'] = df['furnishing'].replace('NO', 0)
df['furnishing'] = pd.to_numeric(df['furnishing'], errors='coerce').fillna(0).astype('int64')

# Region column creation
def region(addr):
    l = addr.split(', ')
    return l[-2]

df['displayAddress'] = df['displayAddress'].astype('string')
df['region'] = df['displayAddress'].apply(lambda x: region(x))
df = df.drop('displayAddress', axis='columns')

cols = df.columns.tolist()  # Get the list of column names
cols.insert(1, cols.pop(cols.index('region')))  # Move 'New_Index' to the second position
df = df[cols]  # Reorder the DataFrame columns


# Creating a new DataFrame with regions with at least 30 estates
all_regions = list(df['region'])
unique_regions = list(set(df['region']))
price_m2_list = df['price_per_m2'].tolist()

regions_list = []
regions_estates_list = []
avg_price_m2_list = []
reg_counter = 0

for reg in unique_regions:
    est_counter = 0
    ind = 0
    est_price_m2 = 0
    for test_reg in all_regions:
        if test_reg == reg:
            est_counter += 1
            est_price_m2 += price_m2_list[ind]
        ind += 1
    if est_counter >= 30:
        regions_estates_list.append(est_counter)
        regions_list.append(reg)
        avg_price_m2_list.append(int(est_price_m2 / est_counter))
        reg_counter += 1

dict = {'Regions': regions_list, 'Number of estates' : regions_estates_list, 'Average price per sqm' : avg_price_m2_list}
df_new = pd.DataFrame(dict)
print(f'Number of Regions with 30 or more estates: {df_new.shape[0]}')

# New column creation for numeric representation of region data
df_new['Original_Index'] = df_new.index
df_new.sort_values(by='Number of estates', ascending=False, inplace=True)
df_new['Region_number'] = range(1, len(df_new) + 1)
df_new.sort_values(by='Original_Index', inplace=True)
df_new.drop('Original_Index', axis='columns', inplace=True)

cols_new = df_new.columns.tolist()  # Get the list of column names
cols_new.insert(1, cols_new.pop(cols_new.index('Region_number')))  # Move 'New_Index' to the second position
df_new = df_new[cols_new]  # Reorder the DataFrame columns


print(df.dtypes)
print(df_new.dtypes)

df_new.to_csv('Regions.csv', index=False)  # index=False prevents writing row indices
print('Regions.csv saved successfully!')

df.to_csv('Clean_data.csv', index=False)
print('Clean_data.csv saved successfully!')
