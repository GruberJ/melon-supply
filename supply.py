import pandas as pd
import numpy as np
supplyfile = '/Users/gruber/Documents/easymelonmusk.xlsx'
df = pd.read_excel(supplyfile, index_col=None, na_values=['NA'], usecols="A,B,E,G,H")
df['Reorder'] = np.where((df['Quantity_in_Stock'] <= df['Reorder_Level']) , 'Reorder', 'NaN')
reorder_rows = df.loc[df['Reorder']=="Reorder"]
writer = pd.ExcelWriter('reorder_list.xlsx', engine='xlsxwriter')
reorder_rows[['Inventory_ID','Name','Quantity_in_Reorder','Reorder_Level']].to_excel(writer, sheet_name='Sheet1')
writer.save()




