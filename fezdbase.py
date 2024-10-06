import pyodbc
import pandas as pd


class get_data:
    @staticmethod
    def query_db(sqlquery):
        # Database connection details
        server = 'FAIZULONXY\\SQLEXPRESS'  # Your server name
        database = 'Fezdbase'  # Your database name

        # Establish connection
        conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')

        # Execute query and load into pandas DataFrame
        df = pd.read_sql(sqlquery, conn)

        # Close the connection
        conn.close()

        return df
