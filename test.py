import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Regional_data.xlsx', sheet_name='Business Bay')


# GRAPHS (box plot for outliers)

# plt.figure(figsize=(10, 6))
# plt.boxplot([df['bathrooms'], df['bedrooms']], labels=['No of bathrooms', 'No of bedrooms'], vert=True, patch_artist=True, boxprops=dict(facecolor='skyblue'))

# plt.title('Box Plot Demonstrating Outliers')
# plt.xlabel('Outliers')

# plt.show()


# plt.figure(figsize=(10, 6))
# plt.boxplot(df['price_per_m2'], vert=True, patch_artist=True, boxprops=dict(facecolor='skyblue'))

# plt.title('Box Plot Demonstrating Outliers')
# plt.xlabel('Price per m2')

# plt.show()


# plt.figure(figsize=(10, 6))
# plt.boxplot(df['sizeMin'], vert=True, patch_artist=True, boxprops=dict(facecolor='skyblue'))

# plt.title('Box Plot Demonstrating Outliers')
# plt.xlabel('Size in m2')

# plt.show()


# OUTLIERS

def outliers_detection(column):
    # Step 1: Calculate Q1 (25th percentile) and Q3 (75th percentile)
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    # Step 2: Calculate the Interquartile Range (IQR)
    IQR = Q3 - Q1
    print(Q1,Q3,IQR)
    # Step 3: Define the lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Step 4: Identify outliers
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)][column]
    outliers = set(outliers)  # Convert to set to remove duplicates
    return outliers


for col in ['bathrooms', 'bedrooms', 'price_per_m2','sizeMin']:
    outliers = outliers_detection(col)
    for val in df[col]:
        if val in outliers:
            print(f'{val} is an outlier')




