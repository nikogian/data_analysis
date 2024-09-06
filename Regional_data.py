import pandas as pd
import xlsxwriter

df = pd.read_csv('Clean_data.csv')

with pd.ExcelWriter('Regional_data.xlsx', engine='xlsxwriter') as writer:
    for ind in range(1, df['Region_number'].max() + 1):
        df_region = df[df['Region_number'] == ind]
        df_region.drop(['Region_number'], axis=1, inplace=True)
        df_region.to_excel(writer, sheet_name = str(ind), index=False)

print('Regional data saved in Regional_data.xlsx.')

