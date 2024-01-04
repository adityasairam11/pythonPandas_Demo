import pandas as pd
import numpy as np

cs_df = pd.read_csv('/Users/adityasairam/Documents/ChaatShop.csv')
print("print whole data:\n", cs_df)
print("print count:\n", cs_df.count())
print("print sum of individual columns:\n", cs_df.sum())
print("print sum of Sales column:\n", cs_df['Sales'].sum())
print("print sum of Sales column:\n", cs_df['Sales'].cumsum())
print("print min value of Sales column:", cs_df['Sales'].min())
print("print max value of Sales column:", cs_df['Sales'].max())

# pandas iteration:

for label, ser in cs_df.items():
    print('label:', label)
    print('content:', ser, sep='\n')

for index,row in cs_df.iterrows():
    print(f'{index},{row}')

print(cs_df.columns)
for row in cs_df.itertuples(index=False):
    print(row)