import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Regions.csv')


# Average price per sqm for regions with more than 30 estates graph
colors = ['skyblue', 'orange']
bar_colors = [colors[i % len(colors)] for i in range(len(df['Regions']))]
df = df.sort_values('Average price per sqm')
plt.figure(figsize=(10, 6))
plt.barh(df['Regions'], df['Average price per sqm'], color=bar_colors)

min_lim = (df['Average price per sqm'].min()//1000) * 1000
max_lim = ((df['Average price per sqm'].max()//1000) + 1) * 1000
if df['Average price per sqm'].min() % 1000 == 0:
    min_lim -= 500
if df['Average price per sqm'].max() % 1000 == 0:
    max_lim += 500 

plt.xlim(min_lim, max_lim)
plt.title("Dubai real estate prices")
plt.xlabel('Avg estate price per m^2')
plt.ylabel('Region')
ax = plt.gca()
ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: f"{x:,.0f} €"))
plt.savefig('Avg_price_per_region.png', dpi=300, bbox_inches='tight')
plt.show()


# Number of estates per region graph
df = df.sort_values('Number of estates')
plt.figure(figsize=(10, 6))
plt.barh(df['Regions'], df['Number of estates'], color=bar_colors)
plt.xlim(0, ((df['Number of estates'].max()//10) + 1) * 10)
plt.title("Number of estates per region")
plt.xlabel('Number of Estates')
plt.ylabel('Region')
plt.savefig('Estates_per_region.png', dpi=300, bbox_inches='tight')
plt.show()

df = df.sort_values('Regions')
