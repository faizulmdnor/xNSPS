import pandas as pd
import pyodbc

SERVER = 'FAIZULONXY\\SQLEXPRESS'
DATABASE = 'GreenVolt'
conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;')
cursor = conn.cursor()

class greenvolt:
    @staticmethod
    def query_table(table_name):
        sql_query = f"""
                SELECT *
                FROM {table_name}
        """
        df = pd.read_sql(sql_query, conn)
        return df

    @staticmethod
    def insert_data(table_name, df):
        columns = ', '.join(df.columns)
        placeholder = ', '.join('?' * len(df.columns))
        sql_insert = f'''
            INSERT INTO {table_name} ({columns}) VALUES ({placeholder})
        '''

        try:
            for index, row in df.iterrows():
                cursor.execute(sql_insert, tuple(row))
            conn.commit()
            print(f"Insert data into {table_name} - SUCCESS")
        except Exception as err:
            conn.rollback()
            print(f"Insert data into {table_name} - FAILED: {err}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
