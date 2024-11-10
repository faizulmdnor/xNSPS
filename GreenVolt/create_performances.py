import pandas as pd
from GreenVolt_db import greenvolt
import numpy as np
import random

def create_performance(empids, year):
    performance_scores = {emp_id: random.randint(50, 100) for emp_id in empids}
    scores = list(performance_scores.values())

    mean_score = np.mean(scores)
    std_dev_score = np.std(scores)

    categories = {
        'High':[],
        'Mid-High':[],
        'Mid':[],
        'Low-Mid':[],
        'Low':[]
    }

    for emp_id, score in performance_scores.items():
        if score > mean_score + 1.5 * std_dev_score:
            categories['High'].append(emp_id)
        elif mean_score + 0.5 * std_dev_score < score <= mean_score + 1.5 * std_dev_score:
            categories['Mid-High'].append(emp_id)
        elif mean_score - 0.5 * std_dev_score <= score <= mean_score + 0.5 * std_dev_score:
            categories['Mid'].append(emp_id)
        elif mean_score - 1.5 * std_dev_score < score < mean_score - 0.5 * std_dev_score:
            categories['Low-Mid'].append(emp_id)
        else:
            categories['Low'].append(emp_id)
    category_list = []
    for category, ids in categories.items():
        category_list.extend([(emp_id, category) for emp_id in ids])

    df1 = pd.DataFrame(category_list, columns=['emp_id', 'category'])
    df1['Year'] = year
    df1 = df1[['emp_id', 'Year', 'category']]
    return df1

tablename = 'vw_Employees'
df_data = greenvolt.query_table(table_name=tablename)

df_data['Date_Hired'] = pd.to_datetime(df_data['Date_Hired'])
df_data['Hired_Year'] = df_data['Date_Hired'].dt.year

emp_hired_year = df_data[['emp_id', 'Hired_Year']]

year_hired = sorted(df_data['Hired_Year'].unique().tolist())

df_perfomance = pd.DataFrame(columns=['emp_id','Year', 'category'])

for year in year_hired:
    df = df_data[df_data['Hired_Year'] <= year]
    empids = df['emp_id'].tolist()
    performance = create_performance(empids, year)
    df_perfomance = pd.concat([df_perfomance, performance])

df_perfomance.reset_index(drop=True, inplace=True)

ins_table = 'Employees_Performance'
greenvolt.insert_data(ins_table, df_perfomance)