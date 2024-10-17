import pyodbc
import pandas as pd

SERVER = 'FAIZULONXY\\SQLEXPRESS'  # Your server name
DATABASE = 'fezdbase2'  # Your database name


class DataRetriever2:
    """
    Class responsible for retrieving and inserting data to and from a database.

    class DataRetriever:

        Retrieve data from the database using a SQL query.

        :param sqlquery: The SQL query to execute.
        :type sqlquery: str
        :return: A DataFrame containing the results of the SQL query.
        :rtype: pandas.DataFrame
        """
    @staticmethod
    def query_db(sqlquery: str) -> pd.DataFrame:
        conn = DataRetriever2._create_connection2()
        df = pd.read_sql(sqlquery, conn)
        conn.close()
        return df

    @staticmethod
    def _create_connection2():
        conn_str = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
        return pyodbc.connect(conn_str)

    @staticmethod
    def query_db_by_table(tablename):
        """
        :param tablename: The name of the table to query in the database.
        :return: A DataFrame containing all rows and columns from the specified table.
        """
        sql_query = f'''
            SELECT * FROM {tablename}
        '''
        conn = DataRetriever2._create_connection2()
        df = pd.read_sql(sql=sql_query, con=conn)
        conn.close()
        return df

class DataInserter2:
    @staticmethod
    def insert_data_by_tablename(tablename, df):
        """
        :param tablename: Name of the table where data will be inserted.
        :type tablename: str
        :param df: DataFrame containing the data to be inserted.
        :type df: pandas.DataFrame
        :return: None
        """
        conn = DataRetriever2._create_connection2()
        if not conn:
            print("Failed to create database connection")
            return

        cursor = conn.cursor()
        columns = ', '.join(df.columns)
        placeholders = ', '.join('?' * len(df.columns))
        sql_insert = f'INSERT INTO {tablename} ({columns}) VALUES ({placeholders})'

        try:
            for index, row in df.iterrows():  # Correct method name
                cursor.execute(sql_insert, tuple(row))
            conn.commit()
            print(f"Data inserted into {tablename} SUCCESS")
        except Exception as e:
            conn.rollback()
            print(f"Insert data into {tablename} FAILED: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
