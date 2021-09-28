import pandas as pd
from src.csv.time import time_now_filename
from src.csv.queries import *
from src.database.database import db

Client = 'MSC'
# File name
file_name = f'REPORT-{Client}-{time_now_filename}'
# give the excel filename

csv_filename = f'csv-output/{file_name}.csv'
excel_filename = f'csv-output/{file_name}.xlsx'

#writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

df1 = pd.read_sql_query(sql2, db) #Read the sql query
writer = pd.ExcelWriter(excel_filename, engine='openpyxl')
df1.to_excel(writer, sheet_name='STOCK LIST',index=False,header=False)
writer.save()

read_excel = pd.read_excel(excel_filename,sheet_name='STOCK LIST') #Read the sql query
read_excel.to_csv(csv_filename,index=False,header=False)
