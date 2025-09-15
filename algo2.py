import pandas as pd

# Read the new file without ID columns
df_noids = pd.read_excel('Etestdata_IDV_SPR_MCC_no_ids.xlsx')
print('Preview of file without ID columns:')
print(df_noids.head())

# Create a new Excel file with only the column names
columns_df = pd.DataFrame({'Columns': df_noids.columns})
columns_df.to_excel('Etestdata_IDV_SPR_MCC_columns.xlsx', index=False)
print('New Excel file with columns only has been created.')
