from fezdbase import DataRetriever
import pandas as pd

sqlquery = '''
        SELECT * FROM vw_UserDetails
    '''

data = DataRetriever.query_db(sqlquery=sqlquery)
data.to_csv('UserDetails.csv', index=False)