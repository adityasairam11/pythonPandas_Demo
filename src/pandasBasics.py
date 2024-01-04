import pandas as pd
import numpy as np

# series::
list_1 = ['a', 'b', 'c', 'd', 'e']
labels = [1, 2, 3, 4, 5]
ser_1 = pd.Series(data=list_1, index=labels)
print(ser_1)

arr_1 = np.array([1, 2, 3, 4])
ser_2 = pd.Series(arr_1)
print(ser_2)

dict_1 = {'fname': 'Aditya', 'l_name': 'Sairam', 'age': 29}
ser_3 = pd.Series(dict_1)
print(ser_3)

# data frames:

arr_2 = np.random.randint(10, 50, size=(2, 3))
df_1 = pd.DataFrame(arr_2, ['A', 'B'], ['C', 'D', 'E'])
print(df_1)

dict_1 = {"one": pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
          "two": pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])}
df_2 = pd.DataFrame(dict_1)
print(df_2)

# rows index not mentioned - random rows
df_3 = pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]))
print(df_3)

df_4 = pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]),
                              orient="index", columns=["one", "two", "three"])
print(df_4)

print("info:")
print(df_4.info())
