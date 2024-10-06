import pyodbc
import pandas as pd

SERVER = 'FAIZULONXY\\SQLEXPRESS'  # Your server name
DATABASE = 'Fezdbase'  # Your database name


class DataRetriever:
    @staticmethod
    def query_db(sqlquery: str) -> pd.DataFrame:
        conn = DataRetriever._create_connection()
        df = pd.read_sql(sqlquery, conn)
        conn.close()
        return df

    @staticmethod
    def _create_connection():
        conn_str = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
        return pyodbc.connect(conn_str)
