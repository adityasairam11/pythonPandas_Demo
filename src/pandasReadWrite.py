import pandas as pd
import sqlalchemy

# read data from a csv file
cs_df = pd.read_csv('/Users/adityasairam/Documents/Sales_Record.csv')
print(cs_df)
# read data from a csv file and restrict to a particular column
# cs_df = pd.read_csv('/Users/adityasairam/Documents/Resources.csv', usecols=["Name"])
print(cs_df)
print("print head:\n", cs_df.head())
# create a backup of a csv file
cs_df.to_csv('/Users/adityasairam/Documents/Resources_backup.csv')

hostname = 'dpg-clnhttpll56s73fi749g-a.oregon-postgres.render.com'
database = 'students_0tvp'
username = 'admin'
pwd = '8l89O7olmnorc09vDkTEd2V8XINATnrk'
port_id = 5432
conn = None
cur = None

engine = sqlalchemy.create_engine(f"postgresql://{username}:{pwd}@{hostname}:{port_id}/{database}")
select_script = "SELECT * FROM EMPLOYEES"
db_df = pd.read_sql(select_script, engine)
print(db_df)
print("print head db data:\n", db_df.head())
cs_df.to_sql('new_employees', engine, if_exists='replace')
engine.dispose()

print("dropping all rows which has nan:\n", cs_df.dropna())
print("dropping all columns which has nan:\n", cs_df.dropna(axis=1))
print("dropping all rows which has greater or equal to 2 nan:\n", cs_df.dropna(thresh=2))
print("replace nan with 0:\n", cs_df.fillna('Role to be defined'))
print("replace nan with previous value:\n", cs_df.ffill())
print("replace QA to Quality Analyst:\n", cs_df.replace('QA', 'Quality Analyst'))
print("replace few values, provided in a list:\n",
      cs_df.replace(['Dev', 'Estimator'], ['Developer', 'Price Estimator']))
print("drop duplicates:\n", cs_df.drop_duplicates())
print("drop duplicates from Role column:\n", cs_df.drop_duplicates(subset=['Role']))
print("drop duplicates from Role column and keep only the last value:\n",
      cs_df.drop_duplicates(subset=['Name', 'Role'], keep='last'))
print(cs_df.info())