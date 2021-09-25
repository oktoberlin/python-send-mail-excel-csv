import pandas as pd
import xlsxwriter
from sources.excel.time import time_now_filename
from sources.excel.queries import *
from sources.database.database import db

Client = 'MSC'
# File name
file_name = f'REPORT-{Client}-{time_now_filename}.xlsx'
# give the excel filename

excel_filename = f'excel-output/{file_name}'

# Writing Database into Excel
writer = pd.ExcelWriter(excel_filename, engine='xlsxwriter')

# Formatting Excel File
workbook = writer.book
for i in range(len(workbook.formats)):
    workbook.formats[i].set_font_size(10)
    workbook.formats[i].set_font_name('Arial Narrow')
'''
fmt=workbook.add_format({
    'font_name':'Arial Narrow',
    'font_size':10
})
'''
#fmt.set_font_size(10)
#fmt.set_font_name('Arial Narrow')

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
align_left = workbook.add_format()
align_left.set_align('left')
align_left.set_align('vcenter')

font_size_title = workbook.add_format({
    'font_size':12,
    'bold':True,
    'align':'center',
})


# SHEET MOV IN #
df_mov_in = pd.read_sql_query(sql_mov_in, db)
df_mov_in.index += 1 #Add index by 1

header_mov_in = [
"Container No","Size","Type","CD","Cleaning","Payload","Tare","Date Mnf",
"GateOut_CY","Date In","Ex Vessel Voy","Ex Consignee","Truck No",
"B/L NO","Principal","Grade","Remarks"
]

df_mov_in.to_excel(writer, sheet_name='MOVE IN', startrow=13, header=header_mov_in)
df_mov_in_summary = pd.read_sql_query(sql_mov_in_summary, db)
index=["20GP","20HC","20OT","20FR","20RF","20TK","40GP","40HC","40OT","40FR","40RF","40RH","40HT"]
df_mov_in_summary.index = index
df_mov_in_summary.to_excel(writer, sheet_name='MOVE IN', startrow=df_mov_in.shape[0] + 17,startcol=1)
worksheet_mov_in = writer.sheets['MOVE IN']
worksheet_mov_in.set_tab_color('#C00000')
#worksheet_mov_in.set_column('A:Z', None, fmt)
#worksheet_mov_in.set_row(0, None, fmt)
worksheet_mov_in.set_default_row(12.75)

isempty = df_mov_in.empty
if isempty!=False:
    # WORKSHEET 3 FORMAT
    #worksheet_mov_in.set_row(0, 26.25)
    
   

    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_stock_list.set_column(0,len(df_stock_list.columns),15,border_fmt)
    
    # Header Info
    worksheet_mov_in.set_column('B1:F1', 'PT. CITRA PRIMA CONTAINER', align_left)
    worksheet_mov_in.set_column(
        'B2:H4', 
        'JL. YOS SUDARSO NO. 16 KEL. WAY LUNIK KEC. PANJANG BANDAR LAMPUNG, PROVINSI : LAMPUNG', 
        align_left
    )
    worksheet_mov_in.set_column('B5:F5', 'Phone : 62-721-3400050', align_left)
    worksheet_mov_in.set_column('B6:F6', 'Fax : 62-721-3400051', align_left)
    worksheet_mov_in.write(
        'B9:B9', 
        f'Principal: {Principle_Code}PNJ MEDITERRANEAN SHIPPING COMPANY', 
        merge_info
    )
    worksheet_mov_in.write('B11:B11', f'Date : {time_now}', merge_info)

    # Add Number Iteration
    worksheet_mov_in.write('A14:A14', 'No.', merge_format_number)
     # Merge necessary column
    worksheet_mov_in.merge_range('A7:Q7', 'Depot In Container List (Consignee Return)', font_size_title)
    
    worksheet_mov_in.set_column('A:O', 10, align_center)
    worksheet_mov_in.set_column(0, 0, 5)
    worksheet_mov_in.set_column(1, 1, 20)
    worksheet_mov_in.set_column(8, 8, 20)
    worksheet_mov_in.set_column(9, 9, 20)
    worksheet_mov_in.set_column(10, 10, 20)
    worksheet_mov_in.set_column(11, 11, 20)
    worksheet_mov_in.set_column(12, 12, 20)
else:
    # Format column Text Align
    worksheet_mov_in.set_column('B:T', None, align_center) 
    
    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_stock_list.set_column(0,len(df_stock_list.columns),15,border_fmt)
    
    # Header Info
    worksheet_mov_in.merge_range('B1:F1', 'PT. CITRA PRIMA CONTAINER', align_left)
    worksheet_mov_in.merge_range(
        'B2:H4', 
        'JL. YOS SUDARSO NO. 16 KEL. WAY LUNIK KEC. PANJANG BANDAR LAMPUNG, PROVINSI : LAMPUNG', 
        align_left
    )
    worksheet_mov_in.merge_range('B5:F5', 'Phone : 62-721-3400050', align_left)
    worksheet_mov_in.merge_range('B6:F6', 'Fax : 62-721-3400051', align_left)
    worksheet_mov_in.write(
        'B9:B9', 
        f'Principal: {Principle_Code}PNJ MEDITERRANEAN SHIPPING COMPANY', 
        merge_info
    )
    worksheet_mov_in.write('B11:B11', f'Date : {time_now}', merge_info)

    # Add Number Iteration
    worksheet_mov_in.write('A14:A14', 'No.', merge_format_number)
     # Merge necessary column
    worksheet_mov_in.merge_range('A7:Q7', 'Depot In Container List (Consignee Return)', font_size_title)
    
    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_mov_in.set_column(0,len(df3.columns),15,border_fmt)


    # Format column Text Align
    worksheet_mov_in.set_column('B:T', None, align_center) 
    #worksheet_mov_in.set_column('N:Q', None, align_center)
    
    # Auto-adjust column width
    for idx, col in enumerate(df_mov_in.columns):  # loop through all columns
        series = df_mov_in[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            ))+ 2  # adding a little extra space
        worksheet_mov_in.set_column(idx+1, idx+1, max_len)

    # Format Column width
    worksheet_mov_in.set_column(0, 0, 5)
    worksheet_mov_in.set_column(4, 4, 5)
    worksheet_mov_in.set_column(6, 6, 10)
    worksheet_mov_in.set_column(7, 7, 10)
    worksheet_mov_in.set_column(8, 8, 10)
    #worksheet_mov_in.set_column(7, 7, 20)
    
    # Un-bold the number iteration
    for row_num, value in enumerate(df_mov_in.index.get_level_values(level=0)):
        worksheet_mov_in.write(row_num+14, 0, value, column_number_format)
    
    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_stock_list.conditional_format(xlsxwriter.utility.xl_range(6, 0, len(df_stock_list.index), len(df_stock_list.columns)), {'type': 'no_errors', 'format': border_fmt})
    
# SHEET REPO IN #
df_repo_in = pd.read_sql_query(sql_mov_in, db)
df_repo_in.index += 1 #Add index by 1

header_repo_in = [
"Container No","Size","Type","Condition","Cleaning","Payload","Tare","Date Mnf",
"GateOut_CY","Date In","Ex Vessel Voy","Ex Consignee","Truck No",
"B/L NO","Principal","Grade","Remarks"
]

df_repo_in.to_excel(writer, sheet_name='REPO IN', startrow=4, header=header_repo_in)
df_repo_in_summary = pd.read_sql_query(sql_mov_in_summary, db)
index=["20GP","20HC","20OT","20FR","20RF","20TK","40GP","40HC","40OT","40FR","40RF","40RH","40HT"]
df_repo_in_summary.index = index
df_repo_in_summary.to_excel(writer, sheet_name='REPO IN', startrow=df_repo_in.shape[0] + 7,startcol=0)
worksheet_repo_in = writer.sheets['REPO IN']

isempty = df_repo_in.empty
if isempty!=False:
    # WORKSHEET 3 FORMAT
    worksheet_repo_in.set_row(0, 26.25)
    
    # Merge necessary column
    worksheet_repo_in.merge_range('A1:O1', 'MOVEMENT IN CONTAINER LIST', font_size_title)
    worksheet_repo_in.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet_repo_in.merge_range('A4:E4', f'{time_now}', merge_info)

    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_stock_list.set_column(0,len(df_stock_list.columns),15,border_fmt)
    
    # Add Number Iteration
    worksheet_repo_in.write('A5:A5', 'No.', merge_format_number)

    worksheet_repo_in.set_column('A:O', 10, align_center)
    worksheet_repo_in.set_column(0, 0, 5)
    worksheet_repo_in.set_column(1, 1, 20)
    worksheet_repo_in.set_column(8, 8, 20)
    worksheet_repo_in.set_column(9, 9, 20)
    worksheet_repo_in.set_column(10, 10, 20)
    worksheet_repo_in.set_column(11, 11, 20)
    worksheet_repo_in.set_column(12, 12, 20)
else:
    worksheet_repo_in.set_row(0, 26.25)

    # Merge necessary column
    worksheet_repo_in.merge_range('A1:L1', 'MOVEMENT IN CONTAINER LIST', font_size_title)
    worksheet_repo_in.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet_repo_in.merge_range('A4:E4', f'{time_now}', merge_info)
    
    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_repo_in.set_column(0,len(df3.columns),15,border_fmt)

    # Add Number Iteration
    worksheet_repo_in.write('A5:A5', 'No.', merge_format_number)

    # Format column Text Align
    worksheet_repo_in.set_column('B:L', None, align_center) 
    worksheet_repo_in.set_column('N:Q', None, align_center)
    
    # Auto-adjust column width
    for idx, col in enumerate(df_repo_in.columns):  # loop through all columns
        series = df_repo_in[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            ))+ 2  # adding a little extra space
        worksheet_repo_in.set_column(idx+1, idx+1, max_len)

    # Format Column width
    worksheet_repo_in.set_column(0, 0, 5)
    worksheet_repo_in.set_column(7, 7, 10)
    worksheet_repo_in.set_column(8, 8, 10)
    worksheet_repo_in.set_column(10, 10, 20)

    # Un-bold the number iteration
    for row_num, value in enumerate(df_repo_in.index.get_level_values(level=0)):
        worksheet_repo_in.write(row_num+5, 0, value, column_number_format)
    
    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_stock_list.conditional_format(xlsxwriter.utility.xl_range(6, 0, len(df_stock_list.index), len(df_stock_list.columns)), {'type': 'no_errors', 'format': border_fmt})

# SHEET MOV OUT #
df_mov_out = pd.read_sql_query(sql_mov_out, db)
df_mov_out.index += 1 #Add index by 1

df_mov_out.to_excel(writer, sheet_name='MOVE OUT', startrow=4)
df_mov_out_summary = pd.read_sql_query(sql_mov_out_summary, db)
index=["20GP","20HC","20OT","20FR","20RF","20TK","40GP","40HC","40OT","40FR","40RF","40RH","40HT"]
df_mov_out_summary.index = index
df_mov_out_summary.to_excel(writer, sheet_name='MOVE OUT', startrow=df_mov_out.shape[0] + 7,startcol=0)
worksheet_mov_out = writer.sheets['MOVE OUT']
worksheet_mov_out.set_tab_color('yellow')

isempty = df_mov_out.empty
if isempty!=False:
    # WORKSHEET 3 FORMAT
    worksheet_mov_out.set_row(0, 26.25)
    
    # Merge necessary column
    worksheet_mov_out.merge_range('A1:O1', 'MOVEMENT OUT CONTAINER LIST', font_size_title)
    worksheet_mov_out.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet_mov_out.merge_range('A4:E4', f'{time_now}', merge_info)

    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_stock_list.set_column(0,len(df_stock_list.columns),15,border_fmt)
    
    # Add Number Iteration
    worksheet_mov_out.write('A5:A5', 'No.', merge_format_number)

    worksheet_mov_out.set_column('A:O', 10, align_center)
    worksheet_mov_out.set_column(0, 0, 5)
    worksheet_mov_out.set_column(1, 1, 20)
    worksheet_mov_out.set_column(8, 8, 20)
    worksheet_mov_out.set_column(9, 9, 20)
    worksheet_mov_out.set_column(10, 10, 20)
    worksheet_mov_out.set_column(11, 11, 20)
    worksheet_mov_out.set_column(12, 12, 20)
    worksheet_mov_out.set_column(14, 14, 20)
else:
    # WORKSHEET 4 FORMAT
    worksheet_mov_out.set_row(0, 26.25)

    # Merge necessary column
    worksheet_mov_out.merge_range('A1:L1', 'MOVEMENT OUT CONTAINER LIST', font_size_title)
    worksheet_mov_out.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet_mov_out.merge_range('A4:E4', f'{time_now}', merge_info)
    
    # Adding border to data
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_stock_list.set_column(0,len(df_stock_list.columns),5,border_fmt)

    # Add Number Iteration
    worksheet_mov_out.write('A5:A5', 'No.', merge_format_number)

    # Format column Text Align
    worksheet_mov_out.set_column('B:N', None, align_center) 
    
    # Auto-adjust column width
    for idx, col in enumerate(df_mov_out.columns):  # loop through all columns
        series = df_mov_out[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            ))+ 2  # adding a little extra space
        worksheet_mov_out.set_column(idx+1, idx+1, max_len)
    
    # Format Column width
    worksheet_mov_out.set_column(0, 0, 5)
    worksheet_mov_out.set_column(6, 6, 10)
    worksheet_mov_out.set_column(7, 7, 10)
    worksheet_mov_out.set_column(11, 11, 20)

    # Un-bold the number iteration
    for row_num, value in enumerate(df_mov_out.index.get_level_values(level=0)):
        worksheet_mov_out.write(row_num+5, 0, value, column_number_format)

# SHEET REPO OUT #
df_repo_out = pd.read_sql_query(sql_mov_out, db)
df_repo_out.index += 1 #Add index by 1

df_repo_out.to_excel(writer, sheet_name='REPO OUT', startrow=4)
df_repo_out_summary = pd.read_sql_query(sql_mov_out_summary, db)
index=["20GP","20HC","20OT","20FR","20RF","20TK","40GP","40HC","40OT","40FR","40RF","40RH","40HT"]
df_repo_out_summary.index = index
df_repo_out_summary.to_excel(writer, sheet_name='REPO OUT', startrow=df_repo_out.shape[0] + 7,startcol=0)
worksheet_repo_out = writer.sheets['REPO OUT']

isempty = df_repo_out.empty
if isempty!=False:
    # WORKSHEET 3 FORMAT
    worksheet_repo_out.set_row(0, 26.25)
    
    # Merge necessary column
    worksheet_repo_out.merge_range('A1:O1', 'MOVEMENT OUT CONTAINER LIST', font_size_title)
    worksheet_repo_out.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet_repo_out.merge_range('A4:E4', f'{time_now}', merge_info)

    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_stock_list.set_column(0,len(df_stock_list.columns),15,border_fmt)
    
    # Add Number Iteration
    worksheet_repo_out.write('A5:A5', 'No.', merge_format_number)

    worksheet_repo_out.set_column('A:O', 10, align_center)
    worksheet_repo_out.set_column(0, 0, 5)
    worksheet_repo_out.set_column(1, 1, 20)
    worksheet_repo_out.set_column(8, 8, 20)
    worksheet_repo_out.set_column(9, 9, 20)
    worksheet_repo_out.set_column(10, 10, 20)
    worksheet_repo_out.set_column(11, 11, 20)
    worksheet_repo_out.set_column(12, 12, 20)
    worksheet_repo_out.set_column(14, 14, 20)
else:
    # WORKSHEET 4 FORMAT
    worksheet_repo_out.set_row(0, 26.25)

    # Merge necessary column
    worksheet_repo_out.merge_range('A1:L1', 'MOVEMENT OUT CONTAINER LIST', font_size_title)
    worksheet_repo_out.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet_repo_out.merge_range('A4:E4', f'{time_now}', merge_info)
    
    # Adding border to data
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_stock_list.set_column(0,len(df_stock_list.columns),5,border_fmt)

    # Add Number Iteration
    worksheet_repo_out.write('A5:A5', 'No.', merge_format_number)

    # Format column Text Align
    worksheet_repo_out.set_column('B:N', None, align_center) 
    
    # Auto-adjust column width
    for idx, col in enumerate(df_repo_out.columns):  # loop through all columns
        series = df_repo_out[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            ))+ 2  # adding a little extra space
        worksheet_repo_out.set_column(idx+1, idx+1, max_len)
    
    # Format Column width
    worksheet_repo_out.set_column(0, 0, 5)
    worksheet_repo_out.set_column(6, 6, 10)
    worksheet_repo_out.set_column(7, 7, 10)
    worksheet_repo_out.set_column(11, 11, 20)

    # Un-bold the number iteration
    for row_num, value in enumerate(df_repo_out.index.get_level_values(level=0)):
        worksheet_repo_out.write(row_num+5, 0, value, column_number_format)

# SHEET STOCK LIST #
df_stock_list = pd.read_sql_query(sql_stockList, db) #Read the sql query
df_stock_list.index += 1 #Add index by 1

#df_stock_list.to_excel(writer, sheet_name='STOCK LIST', startrow=4)
df_stock_list.to_excel(writer, sheet_name='STOCK LIST', startrow=4)
df_stock_list_summary = pd.read_sql_query(sql_stockList_summary, db)
index=["20GP","20HC","20OT","20FR","20RF","20TK","40GP","40HC","40OT","40FR","40RF","40RH","40HT"]
df_stock_list_summary.index = index
df_stock_list_summary.to_excel(writer, sheet_name='STOCK LIST', startrow=df_stock_list.shape[0] + 7,startcol=0)

worksheet_stock_list = writer.sheets['STOCK LIST']
worksheet_stock_list.set_tab_color('green')

isempty = df_stock_list.empty
if isempty!=False:
    worksheet_stock_list.set_row(0, 26.25)
    
    # Merge necessary column
    worksheet_stock_list.merge_range('A1:O1', 'CONTAINER STOCK LIST', font_size_title)
    worksheet_stock_list.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet_stock_list.merge_range('A4:E4', f'{time_now}', merge_info)

    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_stock_list.set_column(0,len(df_stock_list.columns),15,border_fmt)
    
    # Add Number Iteration
    worksheet_stock_list.write('A5:A5', 'No.', merge_format_number)

    worksheet_stock_list.set_column('A:O', 10, align_center)
    worksheet_stock_list.set_column(0, 0, 5)
    worksheet_stock_list.set_column(1, 1, 20)
    worksheet_stock_list.set_column(8, 8, 20)
    worksheet_stock_list.set_column(9, 9, 20)
    worksheet_stock_list.set_column(10, 10, 20)
    worksheet_stock_list.set_column(11, 11, 20)
    worksheet_stock_list.set_column(12, 12, 20)
    worksheet_stock_list.set_column(14, 14, 20)
else:
    # WORKSHEET 2 FORMAT
    worksheet_stock_list.set_row(0, 26.25)
    
    # Merge necessary column
    worksheet_stock_list.merge_range('A1:L1', 'CONTAINER STOCK LIST', font_size_title)
    worksheet_stock_list.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
    worksheet_stock_list.merge_range('A4:E4', f'{time_now}', merge_info)

    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_stock_list.set_column(0,len(df_stock_list.columns),15,border_fmt)
    
    # Add Number Iteration
    worksheet_stock_list.write('A5:A5', 'No.', merge_format_number)

    # Format column Text Align
    worksheet_stock_list.set_column('B:I', None, align_center) 
    worksheet_stock_list.set_column('K:L', None, align_center)
    worksheet_stock_list.set_column('N:O', None, align_center)

    # Auto-adjust column width
    for idx, col in enumerate(df_stock_list.columns):  # loop through all columns
        series = df_stock_list[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            ))+ 2  # adding a little extra space
        worksheet_stock_list.set_column(idx+1, idx+1, max_len)

    # Format column width
    worksheet_stock_list.set_column(0, 0, 5)
    worksheet_stock_list.set_column(6, 6, 10)
    worksheet_stock_list.set_column(7, 7, 10)
    worksheet_stock_list.set_column(10, 10, 20)


    # Un-bold the number iteration
    for row_num, value in enumerate(df_stock_list.index.get_level_values(level=0)):
        worksheet_stock_list.write(row_num+5, 0, value, column_number_format)

# SHEET STOCK LIST #
df_dailyRecap = pd.read_sql_query(sql_dailyRecap, db) #Read the sql query
df_dailyRecap.index += 1 #Add index by 1

#df_stock_list.to_excel(writer, sheet_name='STOCK LIST', startrow=4)
df_dailyRecap.to_excel(writer, sheet_name='DAILY RECAP', startrow=8, header=False, index=False, startcol=1)

worksheet_dailyRecap = writer.sheets['DAILY RECAP']
worksheet_dailyRecap.set_tab_color('#00B0F0')

worksheet_dailyRecap.set_column(0, 0, 10)
worksheet_dailyRecap.set_row(0, 26.25)

# Merge necessary column
worksheet_dailyRecap.merge_range('A1:S1', 'STOCK POSITION DAILY REPORT', font_size_title)
worksheet_dailyRecap.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
worksheet_dailyRecap.merge_range('A4:E4', f'{time_now}', merge_info)
worksheet_dailyRecap.merge_range('A5:A8', 'TYPE CNTR', merge_info_center)
worksheet_dailyRecap.merge_range('B5:D5', 'STOCK', merge_info_center)
worksheet_dailyRecap.merge_range('B6:D6', 'AWAL', merge_info_center)
worksheet_dailyRecap.merge_range('B7:D7', '', merge_info_center)

worksheet_dailyRecap.write('B8:B8', "20'", merge_info_center)
worksheet_dailyRecap.write('C8:C8', "40'", merge_info_center)
worksheet_dailyRecap.write('D8:D8', "45'", merge_info_center)

worksheet_dailyRecap.merge_range('E5:V5', 'IN WARD', merge_info_center)
worksheet_dailyRecap.merge_range('W5:Y5', 'COMPLETED', merge_info_center)
worksheet_dailyRecap.merge_range('Z5:AB5', 'TOTAL', merge_info_center)
worksheet_dailyRecap.merge_range('AC5:AK6', 'STOCK AKHIR', merge_info_center)

worksheet_dailyRecap.merge_range('E6:G7', 'TOTAL IN', merge_info_center)#worksheet.merge_range('G6:H6', 'Ex - Vessel', merge_format)

worksheet_dailyRecap.merge_range('H6:M6', 'CONDITION', merge_info_center)
worksheet_dailyRecap.merge_range('N6:V6', 'CLEANING', merge_info_center)
worksheet_dailyRecap.merge_range('W6:Y6', 'REPAIR', merge_info_center)
worksheet_dailyRecap.merge_range('Z6:AB6', 'OUT WARD', merge_info_center)

worksheet_dailyRecap.merge_range('H7:J7', 'AV', merge_info_center)
worksheet_dailyRecap.merge_range('K7:M7', 'DM', merge_info_center)
worksheet_dailyRecap.merge_range('N7:P7', 'D/W & C/W', merge_info_center)
worksheet_dailyRecap.merge_range('Q7:S7', 'W/W', merge_info_center)
worksheet_dailyRecap.merge_range('T7:V7', 'S/W', merge_info_center)
worksheet_dailyRecap.merge_range('W7:Y7', '', merge_info_center)
worksheet_dailyRecap.merge_range('Z7:AB7', '', merge_info_center)
worksheet_dailyRecap.merge_range('AC7:AE7', 'TODAY', merge_info_center)
worksheet_dailyRecap.merge_range('AF7:AH7', 'AV', merge_info_center)
worksheet_dailyRecap.merge_range('AI7:AK7', 'DMG', merge_info_center)

worksheet_dailyRecap.write('E8:E8', "20'", merge_info_center)
worksheet_dailyRecap.write('F8:F8', "40'", merge_info_center)
worksheet_dailyRecap.write('G8:G8', "45'", merge_info_center)

worksheet_dailyRecap.write('H8:H8', "20'", merge_info_center)
worksheet_dailyRecap.write('I8:I8', "40'", merge_info_center)
worksheet_dailyRecap.write('J8:J8', "45'", merge_info_center)

worksheet_dailyRecap.write('K8:K8', "20'", merge_info_center)
worksheet_dailyRecap.write('L8:L8', "40'", merge_info_center)
worksheet_dailyRecap.write('M8:M8', "45'", merge_info_center)

worksheet_dailyRecap.write('N8:N8', "20'", merge_info_center)
worksheet_dailyRecap.write('O8:O8', "40'", merge_info_center)
worksheet_dailyRecap.write('P8:P8', "45'", merge_info_center)

worksheet_dailyRecap.write('Q8:Q8', "20'", merge_info_center)
worksheet_dailyRecap.write('R8:R8', "40'", merge_info_center)
worksheet_dailyRecap.write('S8:S8', "45'", merge_info_center)

worksheet_dailyRecap.write('T8:T8', "20'", merge_info_center)
worksheet_dailyRecap.write('U8:U8', "40'", merge_info_center)
worksheet_dailyRecap.write('V8:V8', "45'", merge_info_center)

worksheet_dailyRecap.write('W8:W8', "20'", merge_info_center)
worksheet_dailyRecap.write('X8:X8', "40'", merge_info_center)
worksheet_dailyRecap.write('Y8:Y8', "45'", merge_info_center)

worksheet_dailyRecap.write('Z8:Z8', "20'", merge_info_center)
worksheet_dailyRecap.write('AA8:AA8', "40'", merge_info_center)
worksheet_dailyRecap.write('AB8:AB8', "45'", merge_info_center)

worksheet_dailyRecap.write('AC8:AC8', "20'", merge_info_center)
worksheet_dailyRecap.write('AD8:AD8', "40'", merge_info_center)
worksheet_dailyRecap.write('AE8:AE8', "45'", merge_info_center)

worksheet_dailyRecap.write('AF8:AF8', "20'", merge_info_center)
worksheet_dailyRecap.write('AG8:AG8', "40'", merge_info_center)
worksheet_dailyRecap.write('AH8:AH8', "45'", merge_info_center)

worksheet_dailyRecap.write('AI8:AI8', "20'", merge_info_center)
worksheet_dailyRecap.write('AJ8:AJ8', "40'", merge_info_center)
worksheet_dailyRecap.write('AK8:AK8', "45'", merge_info_center)

worksheet_dailyRecap.write('A9:A9', "FR", merge_info)
worksheet_dailyRecap.write('A10:A10', "GP", merge_info)
worksheet_dailyRecap.write('A11:A11', "GOH", merge_info)
worksheet_dailyRecap.write('A12:A12', "HC", merge_info)
worksheet_dailyRecap.write('A13:A13', "OT", merge_info)
worksheet_dailyRecap.write('A14:A14', "RF", merge_info)
worksheet_dailyRecap.write('A15:A15', "RH", merge_info)
worksheet_dailyRecap.write('A16:A16', "TOTAL", None)

worksheet_dailyRecap.set_column('B:AK', None, align_center)

'''
dicts = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
,'AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK']
for dict in dicts:
    worksheet.write(f"{dict}16", f"={dict}9+{dict}10+{dict}11+{dict}12+{dict}13+{dict}14+{dict}15",None)
'''
no_border_format = workbook.add_format({'bottom':0, 'top':0, 'left':0, 'right':0})
worksheet_dailyRecap.conditional_format( 'A1:AK4' , { 'type' : 'no_errors' , 'format' : no_border_format} )

border_format = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
worksheet_dailyRecap.conditional_format( 'A5:AK16' , { 'type' : 'no_errors' , 'format' : border_format} )
#worksheet_dailyRecap.set_column('A:Z', None, fmt)
#worksheet_dailyRecap.set_row(0, None, fmt)

# Save Excel File
writer.save()