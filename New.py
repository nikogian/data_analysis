import pandas as pd
import matplotlib.pyplot as plt

df_entry = pd.read_csv('Regions.csv')

for reg in df_entry['Region_number']:
    df = pd.read_excel('Regional_data.xlsx', sheet_name = f'{reg}')
    
     # Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['sizeMin'], df['price_per_m2'], alpha=0.5)

    # Add labels and title
    plt.xlabel('Size in m2')
    plt.ylabel('Price per m2')
    plt.title(f'Relationship between Size and Price in {df['region'][1]} Region')

    # Show the plot
    plt.show()



