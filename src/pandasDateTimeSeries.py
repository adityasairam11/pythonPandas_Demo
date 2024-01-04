import pandas as pd

s = pd.Series(["12/09/2023 10:00:00+00:00", "12/10/2023 11:00:00+00:00", "12/11/2023 11:00:00+00:00"])
s = pd.to_datetime(s)
print(s)

dict_1 = {"tW": pd.Series([4.42, 4.34, 4.5], index=s)}
df_2 = pd.DataFrame(dict_1)
print(df_2)
print(df_2.index)

datetime_series = pd.Series(pd.date_range("2000-01-01", periods=3, freq='M'))
print(datetime_series)
print(datetime_series.dt.month)
print(datetime_series.dt.day)
print(datetime_series.dt.dayofyear)
print(datetime_series.dt.dayofweek)

dates = ['2017-01-05', 'Jan 5, 2017', '01/05/2017', '2017.01.05', '2017/01/05', '20170105']
print(pd.to_datetime(dates, format='mixed'))

h = pd.Period('2023-12-11 23:00:00', freq='H')
print(h)

print(h.is_leap_year)
