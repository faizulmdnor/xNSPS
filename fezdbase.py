import pyodbc
import pandas as pd

SERVER = 'FAIZULONXY\\SQLEXPRESS'  # Your server name
DATABASE = 'Fezdbase'  # Your database name


class DataRetriever:
    """
    class DataRetriever:

    A class used to retrieve data from a database.

    @staticmethod
    def query_db(sqlquery: str) -> pd.DataFrame:
        Executes a SQL query and returns the result as a pandas DataFrame.

        :param sqlquery: The SQL query to execute.
        :type sqlquery: str
        :return: A pandas DataFrame containing the result of the query.
        :rtype: pd.DataFrame

    @staticmethod
    def _create_connection():
        Creates and returns a new database connection.

        :return: A new database connection.
    """
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
