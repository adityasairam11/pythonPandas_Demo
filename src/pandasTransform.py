import numpy as np
import pandas as pd

dict_1 = {'A': [2, 1, np.nan], 'B': [4, np.nan, np.nan], 'C': [8, 9, 7]}
df_1 = pd.DataFrame(dict_1)
print(df_1)

print("transform by adding 1:\n", df_1.transform(lambda x: x + 1))
print("sorting based on index in ascending order:\n", df_1.sort_index(ascending=True))
print("sorting based on index in descending order:\n", df_1.sort_index(ascending=False))
print("sorting in descending order based on C column:\n", df_1.sort_values(by='C', ascending=False))

# grouping data:
dict_5 = {'store': [1, 2, 1, 2], 'Flavor': ['Choc', 'Van', 'Strawb', 'Choc'],
          'Sales': [26, 12, 18, 22]}
df_5 = pd.DataFrame(dict_5)
print(df_5)
df_by_store = df_5.groupby('store')
print(df_by_store.first())
print(df_by_store.get_group(1))

dict_1 = {"one": pd.Series([1.0, 2.0, 3.0, 4.0], index=['a', 'b', 'c', 'd']),
          "two": pd.Series([1.0, 2.0, 3.0, 4.0, 5.0], index=['a', 'b', 'c', 'd', 'e'])}
df_2 = pd.DataFrame(dict_1)
print(df_2)
print("add a new column add which holds the result of adding existing columns data")
df_2['add'] = df_2['one'] + df_2['two']
print(df_2)
print("add a new column div which holds the result of dividing existing columns data")
df_2 = df_2.assign(div=lambda x: (x['one'] / x['two']))
print(df_2)
print("apply plus 1 function to whole data frame")
df_2 = df_2.apply(lambda x: x + 1, axis=1, result_type='broadcast')
print(df_2)

print("Result of assertion::", df_2.equals(df_5))
