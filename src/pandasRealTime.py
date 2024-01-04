import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy

hostname = 'dpg-clnhttpll56s73fi749g-a.oregon-postgres.render.com'
database = 'students_0tvp'
username = 'admin'
pwd = '8l89O7olmnorc09vDkTEd2V8XINATnrk'
port_id = 5432
conn = None
cur = None

engine = sqlalchemy.create_engine(f"postgresql://{username}:{pwd}@{hostname}:{port_id}/{database}")

# Data loading and inspection
cs_df = pd.read_csv('/Users/adityasairam/Documents/Sales_Record.csv')
pd.set_option('display.max_columns', None)
print(cs_df)
print(cs_df.head())
print(cs_df.describe())
print(cs_df.info())
print("print count:\n", cs_df.count())

# handling null and duplicates
print("dropping all rows which has nan:\n", cs_df.dropna())
print("dropping all columns which has nan:\n", cs_df.dropna(axis=1))
print("dropping all rows which has greater or equal to 2 nan:\n", cs_df.dropna(thresh=2))
print("replace nan with 0:\n", cs_df.fillna('to be filled'))
print("replace nan with previous value:\n", cs_df.ffill())
print("replace Bangalore to Bengaluru:\n", cs_df.replace('Bangalore', 'Bengaluru'))
print("replace few values, provided in a list:\n",
      cs_df.replace(['Delhi', 'Gurgaon'], ['New Delhi', 'Gurugram']))
print("drop duplicates from Age column:\n", cs_df.drop_duplicates(subset=['Age']))

# Statistical analysis
print("print sum of Profit column:\n", cs_df['Profit'].sum())
print(cs_df.loc[cs_df['Product_ID'] == cs_df['Profit'].max()])
print("print cumulative sum of Profit column:\n", cs_df['Profit'].cumsum())
print("print min value of Profit column:", cs_df['Profit'].min())
print("print max value of Profit column:", cs_df['Profit'].max())
print("print mean value of Billing_Amount column:", cs_df['Billing_Amount'].mean())
print("print product id and other details for the data which has max Profit for corresponding years:")
idx = cs_df.groupby('Year')['Profit'].idxmax()
# print("idx:\n", idx)
print(cs_df.loc[idx][['Product_ID', 'Product_Type', 'Billing_Amount', 'Year', 'Profit']])
print("Count of sales made in chennai:", cs_df[cs_df['State'] == 'Chennai']['State'].count())
print("Print the state and other details which has the least profit:\n", cs_df.sort_values(by='Profit').iloc[0])
print("Print the state and other details which has incurred loss:\n", cs_df[cs_df['Profit'] < 0])
print("count of occurrences where in the State is Gurgaon and Profit is greater than 400:")
print(cs_df[(cs_df['State'] == 'Gurgaon')
            & (cs_df['Profit'] > 400)]
      ['Profit'].count())
print("assign a new column named Sale_Amount which holds the value sum of Billing Amount and Profit")
cs_df = cs_df.assign(Sale_Amount=lambda x: (x['Billing_Amount'] + x['Profit']))

# write data to Postgres DB:
cs_df.to_sql('sales_new', engine, if_exists='replace')
db_df = pd.read_sql("SELECT * FROM sales_new", engine)
db_df = db_df.drop(['index'], axis=1)
engine.dispose()

print(db_df)
print(cs_df)

print("Result of comparison between db and pandas csv data frame::", cs_df.equals(db_df))

# plot a classic graph
cs_df.plot(x='Year', y='Profit')
plt.show()

# plot a scatter graph
cs_df.plot(kind='scatter', x='Year', y='Profit')
plt.show()

# plot as a pie chart
y = np.array([35, 25, 25, 15])
labels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels=labels, startangle=90)
plt.show()