from fezdbase import DataRetriever

# SQL query to fetch data from the view
sql_query = '''
    SELECT *
    FROM vw_UserDetails
'''

# Fetch data using the static method from the class
data = DataRetriever.query_db(sql_query)

# Display the first 5 rows of the DataFrame
print(data.head())
