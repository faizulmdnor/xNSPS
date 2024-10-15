from fezdbase import DataRetriever
table = DataRetriever.query_db_by_table(tablename='vw_Operations')
print(table.head(10))
for index, row in table.iterrows():
    if table.loc[index, 'gender'] == 'Female':
        print(f'{table.loc[index, "firstname"]} {table.loc[index, "lastname"]} is a female')
        table.loc[index, 'binary'] = False
    else:
        print(f'{table.loc[index, "firstname"]} {table.loc[index, "lastname"]} is a male')
        table.loc[index, 'binary'] = True
print(table)