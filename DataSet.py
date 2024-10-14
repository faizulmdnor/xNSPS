from fezdbase import DataRetriever
import pandas as pd

tablename = 'vw_Operations'
df_data = DataRetriever.query_db_by_table(tablename=tablename)
print(df_data.head(10))