import pandas as pd
from sqlalchemy import create_engine

# Read configurations and transform to dictionary
toConnect = []
with open('db.config.txt') as config:
    toConnect = config.readlines()
toConnect = dict([tuple(x.split('=')) for x in toConnect])

# Connect to postgreSQL
conn_string = f"postgresql+psycopg2://{toConnect['DB_USER'].strip()}:{toConnect['DB_PASS'].strip()}@{toConnect['DB_HOST'].strip()}:{toConnect['DB_PORT'].strip()}/{toConnect['DB_DATA'].strip()}"
engine = create_engine(conn_string)

# Read and add data from <data>.xlsx to PostgreSQL database
listFiles = toConnect['DB_TABLES'].strip('][').split(', ')
for x in listFiles:
    df = pd.read_excel(f'{x}.xlsx')
    df.to_sql(x, con=engine, if_exists='append', index=False)
