import pandas as pd
import xlsxwriter

df = pd.read_csv('Clean_data.csv')

with pd.ExcelWriter('Regional_data.xlsx', engine='xlsxwriter') as writer:
    for reg in df['region'].unique():
        sheet_name = reg[:31] if len(reg) > 31 else reg
        df_region = df[df['region'] == reg]
        df_region.to_excel(writer, sheet_name=sheet_name, index=False)

print('Regional data saved in Regional_data.xlsx.')
