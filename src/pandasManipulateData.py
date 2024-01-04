import pandas as pd
import numpy as np

# generate a new array with random data ranging from 10 - 50 and 2 x 3 matrix.
arr_2 = np.random.randint(10, 50, size=(2, 3))
df_1 = pd.DataFrame(arr_2, ['A', 'B'], ['C', 'D', 'E'])
print(df_1)
print("Choosing data from a particular column")
print(df_1['D'])
print("Choosing data from a particular row")
print(df_1.loc[['A']])
print("Choosing data from a particular row based on index value")
print(df_1.iloc[['0']])
print("Choosing data from a specific row/ column")
print(df_1.loc[['A', 'B'], ['D', 'E']])
print("Adding a new row which is sum of existing ones")
df_1['Total'] = df_1['C'] + df_1['D'] + df_1['E']
print(df_1)
print("Renaming column names")
df_1 = df_1.rename(columns={'C': 'C-Val'})
print(df_1)

dict_1 = {"one": pd.Series([1.0, 2.0, 3.0, 4.0], index=['a', 'b', 'c', 'd']),
          "two": pd.Series([1.0, 2.0, 3.0, 4.0, 5.0], index=['a', 'b', 'c', 'd', 'e'])}
df_2 = pd.DataFrame(dict_1)
print(df_2)
print("add a new column multiply which holds the result of multiplying existing columns data")
df_2['mult'] = df_2['one'] * df_2['two']
print("-------------")
print(df_2)
print("add a new column add which holds the result of adding existing columns data")
df_2['add'] = df_2['one'] + df_2['two']
print(df_2)
print("add a new column div which holds the result of dividing existing columns data")
df_2 = df_2.assign(div=lambda x: (x['one'] / x['two']))
print(df_2)
print("get unique values")
print(df_2['two'].unique())

dict_2 = {'C': 44, 'D': 45, 'E': 46}
new_row = pd.Series(dict_2, name='F')
print("-------------")
df_1 = df_1._append(new_row)
print(df_1)
print("Dropping a column")
df_1.drop('Total', axis=1, inplace=True)
print(df_1)
print("Dropping a row")
df_1.drop('A', axis=0, inplace=True)
print(df_1)
print("Adding a new column and making it the index")
df_1['Sex'] = ['M', 'F']
print(df_1)
df_1.set_index('Sex', inplace=True)
print(df_1)

# keep 1st data frame and combine with the second data frame, only the nan values from df1 will be replaced with df2 values
df_3 = pd.DataFrame({'A': [1., np.nan, 3., np.nan]})
df_4 = pd.DataFrame({'A': [8., 9., 2., 4.]})
df_3 = df_3.combine_first(df_4)
print(df_3)

# grouping data:
dict_5 = {'store': [1, 2, 1, 2], 'Flavor': ['Choc', 'Van', 'Strawb', 'Choc'],
          'Sales': [26, 12, 18, 22]}
df_5 = pd.DataFrame(dict_5)
print(df_5)
df_by_store = df_5.groupby('store')
print(df_by_store.first())
print(df_by_store.get_group(1))
print(df_by_store.sum().loc[1])
print(df_by_store.describe())
# print("Grouping by store:\n", df_by_store.mean())

df = pd.DataFrame({"A": [12, 4, 5, None, 1],
                   "B": [7, 2, 54, 3, None],
                   "C": [20, 16, 11, 3, 8],
                   "D": [14, 3, None, 2, 6]})

# skip the Na values while finding the mean
print(df.mean(axis=1, skipna=True))
print(df.mean(axis=0))

# concat data frames:
df_6 = pd.DataFrame({'A': [1, 2, 3],
                     'B': [4, 5, 6]},
                    index=[1, 2, 3])
df_7 = pd.DataFrame({'A': [7, 8, 9],
                     'B': [10, 11, 12]},
                    index=[4, 5, 6])

print(pd.concat([df_6, df_7]))

# merge two data frames:
df_8 = pd.DataFrame({'A': [1, 2, 3],
                     'B': [4, 5, 6],
                     'key': [1, 2, 3]})
df_9 = pd.DataFrame({'A': [7, 8, 9],
                     'B': [10, 11, 12],
                     'key': [1, 4, 5]})

print(df_8)
print(df_9)
print(pd.merge(df_8, df_9, how='right', on='key'))

df_10 = pd.DataFrame({'A': [1, 2, 3],
                      'B': [4, 5, 6]},
                     index=[1, 2, 3])
df_11 = pd.DataFrame({'C': [7, 8, 9],
                      'D': [10, 11, 12]},
                     index=[1, 5, 6])

print(df_10.join(df_11, how='left'))