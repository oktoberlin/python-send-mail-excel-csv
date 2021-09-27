from sources.excel.excel_format import *

# SHEET STOCK LIST #
df_stock_list = pd.read_sql_query(sql_stockList, db) #Read the sql query
df_stock_list.index += 1 #Add index by 1

#df_stock_list.to_excel(writer, sheet_name='STOCK LIST', startrow=4)
df_stock_list.to_excel(writer, sheet_name='STOCK LIST', startrow=13)
df_stock_list_summary = pd.read_sql_query(sql_stockList_summary, db)
index=["20GP","20HC","20OT","20FR","20RF","20TK","40GP","40HC","40OT","40FR","40RF","40RH","40HT"]
df_stock_list_summary.index = index
df_stock_list_summary.to_excel(writer, sheet_name='STOCK LIST', startrow=df_stock_list.shape[0] + 17,startcol=1)

worksheet_stock_list = writer.sheets['STOCK LIST']
worksheet_stock_list.set_tab_color('green')

worksheet_stock_list.set_row(13, 13, header_format)
worksheet_stock_list.set_default_row(12.75)

# Format column Text Align
#worksheet_stock_list.set_column('A:Z', None, header_format) 
#worksheet_stock_list.set_row(13,13,header_format)

# Add Border
#border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
#worksheet_stock_list.set_column(0,len(df_stock_list.columns),15,border_fmt)

# Header Info
worksheet_stock_list.merge_range('B1:F1', 'PT. CITRA PRIMA CONTAINER', align_left)
worksheet_stock_list.merge_range(
    'B2:H4', 
    'JL. YOS SUDARSO NO. 16 KEL. WAY LUNIK KEC. PANJANG BANDAR LAMPUNG, PROVINSI : LAMPUNG', 
    align_left
)
worksheet_stock_list.merge_range('B5:F5', 'Phone : 62-721-3400050', align_left)
worksheet_stock_list.merge_range('B6:F6', 'Fax : 62-721-3400051', align_left)
worksheet_stock_list.write(
    'B9:B9', 
    f'Principal: {Principle_Code}PNJ MEDITERRANEAN SHIPPING COMPANY', 
    merge_info
)
worksheet_stock_list.write('B11:B11', f'Date : {date_now}', merge_info)

# Add Number Iteration
worksheet_stock_list.write('A14:A14', 'No.', merge_format_number)
    # Merge necessary column
worksheet_stock_list.merge_range('A7:Q7', 'Depot In Container List (Consignee Return)', font_size_title)
# Un-bold the number iteration
for row_num, value in enumerate(df_stock_list.index.get_level_values(level=0)):
    worksheet_stock_list.write(row_num+14, 0, value, column_number_format)

isempty = df_stock_list.empty
if isempty!=False:
    worksheet_stock_list.set_column(0, 0, 5, align_center)
    worksheet_stock_list.set_column(1, 1, 13, align_center)
    worksheet_stock_list.set_column(2, 4, 5, align_center)
    worksheet_stock_list.set_column(7, 7, 5, align_center)
    worksheet_stock_list.set_column(8, 12, 13, align_center)
    worksheet_stock_list.set_row(13, 13, align_center)
else:
    # Format column Text Align
    worksheet_stock_list.set_column('A:T', None, align_center) 
    
    # Auto-adjust column width
    for idx, col in enumerate(df_stock_list.columns):  # loop through all columns
        series = df_stock_list[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            ))+ 2  # adding a little extra space
        worksheet_stock_list.set_column(idx+1, idx+1, max_len)
    
    # Format Column width
    worksheet_stock_list.set_column(0, 0, 5)
    worksheet_stock_list.set_column(4, 4, 5)
    worksheet_stock_list.set_column(6, 8, 10)
