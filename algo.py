# Import pandas for data handling
import pandas as pd

# Read the Excel file
df = pd.read_excel('Etestdata_IDV_SPR_MCC.xlsx')

# Show the first few rows
print(df.head())

# Show all column names
print(df.columns.tolist())

# Drop specified columns and save to a new file
columns_to_drop = [
	'LOT7',
	'WAFER',
	'WAFER_ID',
	'OPERATION@ETEST@M0_IL',
	'PRODUCT@ETEST@M0_IL',
    'PROGRAM@ETEST@M0_IL',
	'TEST_END_DATE@ETEST@M0_IL'
]
df_new = df.drop(columns=columns_to_drop, errors='ignore')
df_new.to_excel('Etestdata_IDV_SPR_MCC_no_ids.xlsx', index=False)
print('New file created without specified columns.')
