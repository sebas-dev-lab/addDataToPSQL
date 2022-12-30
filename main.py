import pandas as pd
from sqlalchemy import create_engine

toConnect = []
with open('db.config.txt') as config:
    toConnect = config.readlines()


toConnect = dict([tuple(x.split('=')) for x in toConnect])
conn_string = f"postgresql+psycopg2://{toConnect['DB_USER'].strip()}:{toConnect['DB_PASS'].strip()}@{toConnect['DB_HOST'].strip()}:{toConnect['DB_PORT'].strip()}/{toConnect['DB_DATA'].strip()}"
engine = create_engine(conn_string)

listFiles = toConnect['DB_TABLES'].strip('][').split(', ')

for x in listFiles:
    df = pd.read_excel(f'{x}.xlsx')
    df.to_sql(x, con=engine, if_exists='append', index=False)
