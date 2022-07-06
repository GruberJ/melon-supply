import pandas as pd
import numpy as np
supplyfile = '/Users/gruber/Documents/melonmusk.xlsx'
df = pd.read_excel(supplyfile, 
index_col=None, na_values=['NA'], usecols="C,D,F,G,I,J", header=(2))
df['Reorder'] = np.where((df['Quantity_in_Stock'] <= df['Reorder_Level']) , 'Reorder', 'NaN')
reorder_rows = df.loc[df['Reorder']=="Reorder"]
writer = pd.ExcelWriter('/Users/gruber/Projects/labsupply/supplyfileoutput/melon_reorder_list.xlsx', engine='xlsxwriter')
reorder_rows[['Inventory_ID','Name','Quantity_in_Reorder','Reorder_Level']].to_excel(writer, sheet_name='Sheet1')
writer.save()