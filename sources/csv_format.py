import pandas as pd
import xlsxwriter
from .time import time_now_filename
from sources.queries import *
from sources.database import db
from sources.excel_format import excel_filename
Client = 'MSC'
# File name
file_name = f'REPORT-{Client}-{time_now_filename}'
# give the excel filename

csv_filename = 'csv-output/test.csv'

writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

df1 = pd.read_sql_query(sql3, db) #Read the sql query
df1.to_excel(writer, sheet_name='MOV IN', header=False, index=False)

read_file = pd.read_excel('test.xlsx', sheet_name='MOV IN')
read_file.to_csv(csv_filename, index = None, header=False)

'''
# Writing Database into Excel
writer = pd.ExcelWriter(excel_filename, engine='xlsxwriter')

# Formatting Excel File
workbook = writer.book

fmt=workbook.add_format({
    "font_name": "Arial Narrow",
    "font_size":10
})

#cell_format.set_font_name('Arial Narrow')
#cell_format.set_font_size(10)
# GLOBAL FORMATTING
column_number_format = workbook.add_format({
    'bold': False,
    'align': 'center',
})

merge_info = workbook.add_format({
    'bold': True
})

merge_info_center = workbook.add_format({
    'bold': True,
})

merge_info_center.set_align('center')

merge_info_center.set_align('vcenter')

merge_format_number = workbook.add_format({
    'align': 'center',
    'bold': False
})

align_center = workbook.add_format({
    'align': 'center'
})

font_size_title = workbook.add_format({
    'font_size':12,
    'bold':True,
    'align':'center',
})
font_size_title.set_underline(1)

# WORKSHEET 1 FORMAT
#df1.index += 1
#df1.to_csv(writer, sheet_name='DAILY STOCK POSITION', startrow=5, index=False)
df1 = pd.read_sql_query(sql1, db) #Read the sql query
df1.index += 1 #Add index by 1

#df2.to_csv(writer, sheet_name='STOCK LIST', startrow=4)
df1.to_csv(writer, sheet_name='DAILY STOCK POSITION', startrow=8, header=False, index=False, startcol=1)

worksheet = writer.sheets['DAILY STOCK POSITION']

worksheet.set_column(0, 0, 10)
worksheet.set_row(0, 26.25)

# Merge necessary column
worksheet.merge_range('A1:S1', 'STOCK POSITION DAILY REPORT', font_size_title)
worksheet.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
worksheet.merge_range('A4:E4', f'{time_now}', merge_info)
worksheet.merge_range('A5:A8', 'TYPE CNTR', merge_info_center)
worksheet.merge_range('B5:D5', 'STOCK', merge_info_center)
worksheet.merge_range('B6:D6', 'AWAL', merge_info_center)
worksheet.merge_range('B7:D7', '', merge_info_center)

worksheet.write('B8:B8', "20'", merge_info_center)
worksheet.write('C8:C8', "40'", merge_info_center)
worksheet.write('D8:D8', "45'", merge_info_center)

worksheet.merge_range('E5:V5', 'IN WARD', merge_info_center)
worksheet.merge_range('W5:Y5', 'COMPLETED', merge_info_center)
worksheet.merge_range('Z5:AB5', 'TOTAL', merge_info_center)
worksheet.merge_range('AC5:AK6', 'STOCK AKHIR', merge_info_center)

worksheet.merge_range('E6:G7', 'TOTAL IN', merge_info_center)#worksheet.merge_range('G6:H6', 'Ex - Vessel', merge_format)

worksheet.merge_range('H6:M6', 'CONDITION', merge_info_center)
worksheet.merge_range('N6:V6', 'CLEANING', merge_info_center)
worksheet.merge_range('W6:Y6', 'REPAIR', merge_info_center)
worksheet.merge_range('Z6:AB6', 'OUT WARD', merge_info_center)

worksheet.merge_range('H7:J7', 'AV', merge_info_center)
worksheet.merge_range('K7:M7', 'DM', merge_info_center)
worksheet.merge_range('N7:P7', 'D/W & C/W', merge_info_center)
worksheet.merge_range('Q7:S7', 'W/W', merge_info_center)
worksheet.merge_range('T7:V7', 'S/W', merge_info_center)
worksheet.merge_range('W7:Y7', '', merge_info_center)
worksheet.merge_range('Z7:AB7', '', merge_info_center)
worksheet.merge_range('AC7:AE7', 'TODAY', merge_info_center)
worksheet.merge_range('AF7:AH7', 'AV', merge_info_center)
worksheet.merge_range('AI7:AK7', 'DMG', merge_info_center)

worksheet.write('E8:E8', "20'", merge_info_center)
worksheet.write('F8:F8', "40'", merge_info_center)
worksheet.write('G8:G8', "45'", merge_info_center)

worksheet.write('H8:H8', "20'", merge_info_center)
worksheet.write('I8:I8', "40'", merge_info_center)
worksheet.write('J8:J8', "45'", merge_info_center)

worksheet.write('K8:K8', "20'", merge_info_center)
worksheet.write('L8:L8', "40'", merge_info_center)
worksheet.write('M8:M8', "45'", merge_info_center)

worksheet.write('N8:N8', "20'", merge_info_center)
worksheet.write('O8:O8', "40'", merge_info_center)
worksheet.write('P8:P8', "45'", merge_info_center)

worksheet.write('Q8:Q8', "20'", merge_info_center)
worksheet.write('R8:R8', "40'", merge_info_center)
worksheet.write('S8:S8', "45'", merge_info_center)

worksheet.write('T8:T8', "20'", merge_info_center)
worksheet.write('U8:U8', "40'", merge_info_center)
worksheet.write('V8:V8', "45'", merge_info_center)

worksheet.write('W8:W8', "20'", merge_info_center)
worksheet.write('X8:X8', "40'", merge_info_center)
worksheet.write('Y8:Y8', "45'", merge_info_center)

worksheet.write('Z8:Z8', "20'", merge_info_center)
worksheet.write('AA8:AA8', "40'", merge_info_center)
worksheet.write('AB8:AB8', "45'", merge_info_center)

worksheet.write('AC8:AC8', "20'", merge_info_center)
worksheet.write('AD8:AD8', "40'", merge_info_center)
worksheet.write('AE8:AE8', "45'", merge_info_center)

worksheet.write('AF8:AF8', "20'", merge_info_center)
worksheet.write('AG8:AG8', "40'", merge_info_center)
worksheet.write('AH8:AH8', "45'", merge_info_center)

worksheet.write('AI8:AI8', "20'", merge_info_center)
worksheet.write('AJ8:AJ8', "40'", merge_info_center)
worksheet.write('AK8:AK8', "45'", merge_info_center)

worksheet.write('A9:A9', "FR", merge_info)
worksheet.write('A10:A10', "GP", merge_info)
worksheet.write('A11:A11', "GOH", merge_info)
worksheet.write('A12:A12', "HC", merge_info)
worksheet.write('A13:A13', "OT", merge_info)
worksheet.write('A14:A14', "RF", merge_info)
worksheet.write('A15:A15', "RH", merge_info)
worksheet.write('A16:A16', "TOTAL", None)

worksheet.set_column('B:AK', None, align_center)


#dicts = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
#,'AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK']
#for dict in dicts:
#
no_border_format = workbook.add_format({'bottom':0, 'top':0, 'left':0, 'right':0})
worksheet.conditional_format( 'A1:AK4' , { 'type' : 'no_errors' , 'format' : no_border_format} )

border_format = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
worksheet.conditional_format( 'A5:AK16' , { 'type' : 'no_errors' , 'format' : border_format} )
worksheet.set_column('A:Z', None, fmt)
worksheet.set_row(0, None, fmt)
# SHEET 2 #
df2 = pd.read_sql_query(sql2, db) #Read the sql query
df2.index += 1 #Add index by 1

#df2.to_csv(writer, sheet_name='STOCK LIST', startrow=4)
df2.to_csv(writer, sheet_name='STOCK LIST', startrow=4)
df2_summary = pd.read_sql_query(sql2_summary, db)
index=["20GP","20HC","20OT","20FR","20RF","20TK","40GP","40HC","40OT","40FR","40RF","40RH","40HT"]
df2_summary.index = index
df2_summary.to_csv(writer, sheet_name='STOCK LIST', startrow=df2.shape[0] + 7,startcol=0)

worksheet2 = writer.sheets['STOCK LIST']

isempty = df2.empty
if isempty!=False:
    worksheet2.set_row(0, 26.25)
    
    # Merge necessary column
    worksheet2.merge_range('A1:O1', 'CONTAINER STOCK LIST', font_size_title)
    worksheet2.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet2.merge_range('A4:E4', f'{time_now}', merge_info)

    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet2.set_column(0,len(df2.columns),15,border_fmt)
    
    # Add Number Iteration
    worksheet2.write('A5:A5', 'No.', merge_format_number)

    worksheet2.set_column('A:O', 10, align_center)
    worksheet2.set_column(0, 0, 5)
    worksheet2.set_column(1, 1, 20)
    worksheet2.set_column(8, 8, 20)
    worksheet2.set_column(9, 9, 20)
    worksheet2.set_column(10, 10, 20)
    worksheet2.set_column(11, 11, 20)
    worksheet2.set_column(12, 12, 20)
    worksheet2.set_column(14, 14, 20)
else:
        # WORKSHEET 2 FORMAT
    worksheet2.set_row(0, 26.25)
    
    # Merge necessary column
    worksheet2.merge_range('A1:L1', 'CONTAINER STOCK LIST', font_size_title)
    worksheet2.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet2.merge_range('A4:E4', f'{time_now}', merge_info)

    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet2.set_column(0,len(df2.columns),15,border_fmt)
    
    # Add Number Iteration
    worksheet2.write('A5:A5', 'No.', merge_format_number)

    # Format column Text Align
    worksheet2.set_column('B:I', None, align_center) 
    worksheet2.set_column('K:L', None, align_center)
    worksheet2.set_column('N:O', None, align_center)

    # Auto-adjust column width
    for idx, col in enumerate(df2.columns):  # loop through all columns
        series = df2[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            ))+ 2  # adding a little extra space
        worksheet2.set_column(idx+1, idx+1, max_len)

    # Format column width
    worksheet2.set_column(0, 0, 5)
    worksheet2.set_column(6, 6, 10)
    worksheet2.set_column(7, 7, 10)
    worksheet2.set_column(10, 10, 20)


    # Un-bold the number iteration
    for row_num, value in enumerate(df2.index.get_level_values(level=0)):
        worksheet2.write(row_num+5, 0, value, column_number_format)

# SHEET 3 #
df3 = pd.read_sql_query(sql3, db)
df3.index += 1 #Add index by 1

header_mov_in = [
"Container No","Size","Type","Condition","Cleaning","Payload","Tare","Date Mnf",
"GateOut_CY","Date In","Ex Vessel Voy","Ex Consignee","Truck No",
"B/L NO","Principal","Grade","Remarks"
]

df3.to_csv(writer, sheet_name='MOV IN', startrow=4, header=header_mov_in)
df3_summary = pd.read_sql_query(sql3_summary, db)
index=["20GP","20HC","20OT","20FR","20RF","20TK","40GP","40HC","40OT","40FR","40RF","40RH","40HT"]
df3_summary.index = index
df3_summary.to_csv(writer, sheet_name='MOV IN', startrow=df3.shape[0] + 7,startcol=0)
worksheet3 = writer.sheets['MOV IN']

isempty = df3.empty
if isempty!=False:
    # WORKSHEET 3 FORMAT
    worksheet3.set_row(0, 26.25)
    
    # Merge necessary column
    worksheet3.merge_range('A1:O1', 'MOVEMENT IN CONTAINER LIST', font_size_title)
    worksheet3.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet3.merge_range('A4:E4', f'{time_now}', merge_info)

    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet2.set_column(0,len(df2.columns),15,border_fmt)
    
    # Add Number Iteration
    worksheet3.write('A5:A5', 'No.', merge_format_number)

    worksheet3.set_column('A:O', 10, align_center)
    worksheet3.set_column(0, 0, 5)
    worksheet3.set_column(1, 1, 20)
    worksheet3.set_column(8, 8, 20)
    worksheet3.set_column(9, 9, 20)
    worksheet3.set_column(10, 10, 20)
    worksheet3.set_column(11, 11, 20)
    worksheet3.set_column(12, 12, 20)
else:
    worksheet3.set_row(0, 26.25)

    # Merge necessary column
    worksheet3.merge_range('A1:L1', 'MOVEMENT IN CONTAINER LIST', font_size_title)
    worksheet3.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet3.merge_range('A4:E4', f'{time_now}', merge_info)
    
    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet3.set_column(0,len(df3.columns),15,border_fmt)

    # Add Number Iteration
    worksheet3.write('A5:A5', 'No.', merge_format_number)

    # Format column Text Align
    worksheet3.set_column('B:L', None, align_center) 
    worksheet3.set_column('N:Q', None, align_center)
    
    # Auto-adjust column width
    for idx, col in enumerate(df3.columns):  # loop through all columns
        series = df3[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            ))+ 2  # adding a little extra space
        worksheet3.set_column(idx+1, idx+1, max_len)

    # Format Column width
    worksheet3.set_column(0, 0, 5)
    worksheet3.set_column(7, 7, 10)
    worksheet3.set_column(8, 8, 10)
    worksheet3.set_column(10, 10, 20)

    # Un-bold the number iteration
    for row_num, value in enumerate(df3.index.get_level_values(level=0)):
        worksheet3.write(row_num+5, 0, value, column_number_format)
    
    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet2.conditional_format(xlsxwriter.utility.xl_range(6, 0, len(df2.index), len(df2.columns)), {'type': 'no_errors', 'format': border_fmt})
    
# SHEET 4 #
df4 = pd.read_sql_query(sql4, db)
df4.index += 1 #Add index by 1

df4.to_csv(writer, sheet_name='MOV OUT', startrow=4)
df4_summary = pd.read_sql_query(sql4_summary, db)
index=["20GP","20HC","20OT","20FR","20RF","20TK","40GP","40HC","40OT","40FR","40RF","40RH","40HT"]
df4_summary.index = index
df4_summary.to_csv(writer, sheet_name='MOV OUT', startrow=df4.shape[0] + 7,startcol=0)
worksheet4 = writer.sheets['MOV OUT']

isempty = df4.empty
if isempty!=False:
    # WORKSHEET 3 FORMAT
    worksheet4.set_row(0, 26.25)
    
    # Merge necessary column
    worksheet4.merge_range('A1:O1', 'MOVEMENT OUT CONTAINER LIST', font_size_title)
    worksheet4.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet4.merge_range('A4:E4', f'{time_now}', merge_info)

    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet2.set_column(0,len(df2.columns),15,border_fmt)
    
    # Add Number Iteration
    worksheet4.write('A5:A5', 'No.', merge_format_number)

    worksheet4.set_column('A:O', 10, align_center)
    worksheet4.set_column(0, 0, 5)
    worksheet4.set_column(1, 1, 20)
    worksheet4.set_column(8, 8, 20)
    worksheet4.set_column(9, 9, 20)
    worksheet4.set_column(10, 10, 20)
    worksheet4.set_column(11, 11, 20)
    worksheet4.set_column(12, 12, 20)
    worksheet4.set_column(14, 14, 20)
else:
    # WORKSHEET 4 FORMAT
    worksheet4.set_row(0, 26.25)

    # Merge necessary column
    worksheet4.merge_range('A1:L1', 'MOVEMENT OUT CONTAINER LIST', font_size_title)
    worksheet4.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet4.merge_range('A4:E4', f'{time_now}', merge_info)
    
    # Adding border to data
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet2.set_column(0,len(df2.columns),5,border_fmt)

    # Add Number Iteration
    worksheet4.write('A5:A5', 'No.', merge_format_number)

    # Format column Text Align
    worksheet4.set_column('B:N', None, align_center) 
    
    # Auto-adjust column width
    for idx, col in enumerate(df4.columns):  # loop through all columns
        series = df4[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            ))+ 2  # adding a little extra space
        worksheet4.set_column(idx+1, idx+1, max_len)
    
    # Format Column width
    worksheet4.set_column(0, 0, 5)
    worksheet4.set_column(6, 6, 10)
    worksheet4.set_column(7, 7, 10)
    worksheet4.set_column(11, 11, 20)

    # Un-bold the number iteration
    for row_num, value in enumerate(df4.index.get_level_values(level=0)):
        worksheet4.write(row_num+5, 0, value, column_number_format)

# SHEET 5 #
df5 = pd.read_sql_query(sql5, db) #Read the sql query
df5.index += 1 #Add index by 1

#df2.to_csv(writer, sheet_name='STOCK LIST', startrow=4)
df5.to_csv(writer, sheet_name='DAMAGE', startrow=4)
df5_summary = pd.read_sql_query(sql5_summary, db)
index=["20GP","20HC","20OT","20FR","20RF","20TK","40GP","40HC","40OT","40FR","40RF","40RH","40HT"]
df5_summary.index = index
df5_summary.to_csv(writer, sheet_name='DAMAGE', startrow=df5.shape[0] + 7,startcol=0)

worksheet5 = writer.sheets['DAMAGE']

isempty = df5.empty
if isempty!=False:
    worksheet5.set_row(0, 26.25)
    
    # Merge necessary column
    worksheet5.merge_range('A1:O1', 'DAMAGE STOCK LIST', font_size_title)
    worksheet5.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet5.merge_range('A4:E4', f'{time_now}', merge_info)

    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet2.set_column(0,len(df2.columns),15,border_fmt)
    
    # Add Number Iteration
    worksheet5.write('A5:A5', 'No.', merge_format_number)

    worksheet5.set_column('A:O', 10, align_center)
    worksheet5.set_column(0, 0, 5)
    worksheet5.set_column(1, 1, 20)
    worksheet5.set_column(8, 8, 20)
    worksheet5.set_column(9, 9, 20)
    worksheet5.set_column(10, 10, 20)
    worksheet5.set_column(11, 11, 20)
    worksheet5.set_column(12, 12, 20)
    worksheet5.set_column(14, 14, 20)
    
else:
        # WORKSHEET 5 FORMAT
    worksheet5.set_row(0, 26.25)
    
    # Merge necessary column
    worksheet5.merge_range('A1:L1', 'DAMAGE STOCK LIST', font_size_title)
    worksheet5.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet5.merge_range('A4:E4', f'{time_now}', merge_info)

    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet2.set_column(0,len(df2.columns),15,border_fmt)
    
    # Add Number Iteration
    worksheet5.write('A5:A5', 'No.', merge_format_number)

    # Format column Text Align
    worksheet5.set_column('B:I', None, align_center) 
    worksheet5.set_column('K:L', None, align_center)
    worksheet5.set_column('N:O', None, align_center)

    # Auto-adjust column width
    for idx, col in enumerate(df5.columns):  # loop through all columns
        series = df5[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            ))+ 2  # adding a little extra space
        worksheet5.set_column(idx+1, idx+1, max_len)

    # Format column width
    worksheet5.set_column(0, 0, 5)
    worksheet5.set_column(6, 6, 10)
    worksheet5.set_column(7, 7, 10)
    worksheet5.set_column(10, 10, 20)


    # Un-bold the number iteration
    for row_num, value in enumerate(df5.index.get_level_values(level=0)):
        worksheet5.write(row_num+5, 0, value, column_number_format)

# SHEET 6 #
df6 = pd.read_sql_query(sql6, db) #Read the sql query
df6.index += 1 #Add index by 1

#df2.to_csv(writer, sheet_name='STOCK LIST', startrow=4)
df6.to_csv(writer, sheet_name='REPAIR FINISHED', startrow=4)
df6_summary = pd.read_sql_query(sql6_summary, db)
index=["20GP","20HC","20OT","20FR","20RF","20TK","40GP","40HC","40OT","40FR","40RF","40RH","40HT"]
df6_summary.index = index
df6_summary.to_csv(writer, sheet_name='REPAIR FINISHED', startrow=df6.shape[0] + 7,startcol=0)

worksheet6 = writer.sheets['REPAIR FINISHED']

isempty = df6.empty
if isempty!=False:
    worksheet6.set_row(0, 26.25)
    
    # Merge necessary column
    worksheet6.merge_range('A1:O1', 'REPAIR FINISHED LIST', font_size_title)
    worksheet6.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet6.merge_range('A4:E4', f'{time_now}', merge_info)

    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet2.set_column(0,len(df2.columns),15,border_fmt)
    
    # Add Number Iteration
    worksheet6.write('A5:A5', 'No.', merge_format_number)

    worksheet6.set_column('A:O', 10, align_center)
    worksheet6.set_column(0, 0, 5)
    worksheet6.set_column(1, 1, 20)
    worksheet6.set_column(8, 8, 20)
    worksheet6.set_column(10, 10, 20)
    worksheet6.set_column(11, 11, 20)
    worksheet6.set_column(12, 12, 20)
    worksheet6.set_column(14, 14, 20)
else:
        # WORKSHEET 5 FORMAT
    worksheet6.set_row(0, 26.25)
    
    # Merge necessary column
    worksheet6.merge_range('A1:L1', 'REPAIR FINISHED LIST', font_size_title)
    worksheet6.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet6.merge_range('A4:E4', f'{time_now}', merge_info)

    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet2.set_column(0,len(df2.columns),15,border_fmt)
    
    # Add Number Iteration
    worksheet6.write('A5:A5', 'No.', merge_format_number)

    # Format column Text Align
    worksheet6.set_column('B:I', None, align_center) 
    worksheet6.set_column('K:L', None, align_center)
    worksheet6.set_column('N:O', None, align_center)

    # Auto-adjust column width
    for idx, col in enumerate(df6.columns):  # loop through all columns
        series = df6[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            ))+ 2  # adding a little extra space
        worksheet6.set_column(idx+1, idx+1, max_len)

    # Format column width
    worksheet6.set_column(0, 0, 5)
    worksheet6.set_column(6, 6, 10)
    worksheet6.set_column(7, 7, 10)
    worksheet6.set_column(10, 10, 10)

    # Un-bold the number iteration
    for row_num, value in enumerate(df6.index.get_level_values(level=0)):
        worksheet6.write(row_num+5, 0, value, column_number_format)

# Save Excel File
writer.save()

'''