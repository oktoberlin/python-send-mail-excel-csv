from sources.excel.excel_format2 import *

# SHEET MOV IN #
df_mov_in = pd.read_sql_query(sql_mov_in, db)
df_mov_in.index += 1 #Add index by 1

header_mov_in = [
"Container No","Size","Type","CD","Cleaning","Payload","Tare","Date Mnf",
"GateOut_CY","Date In","Ex Vessel Voy","Ex Consignee","Truck No",
"B/L NO","Principal","Grade","Remarks"
]
'''
df = df.style.set_properties(**{
    'background-color': 'grey',
    'font-size': '20pt',
})
'''
df_mov_in.to_excel(writer, sheet_name='MOVE IN', startrow=13, header=header_mov_in)
df_mov_in_summary = pd.read_sql_query(sql_mov_in_summary, db)
index=["20GP","20HC","20OT","20FR","20RF","20TK","40GP","40HC","40OT","40FR","40RF","40RH","40HT"]
df_mov_in_summary.index = index
df_mov_in_summary.to_excel(writer, sheet_name='MOVE IN', startrow=df_mov_in.shape[0] + 17,startcol=1)
worksheet_mov_in = writer.sheets['MOVE IN']

worksheet_mov_in.set_tab_color('#C00000')
#worksheet_mov_in.set_column('A:Z', None, fmt)
worksheet_mov_in.set_row(13, 13, header_format)
worksheet_mov_in.set_default_row(12.75)

# Format column Text Align
#worksheet_mov_in.set_column('A:Z', None, header_format) 
#worksheet_mov_in.set_row(13,13,header_format)

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
worksheet_mov_in.write('B11:B11', f'Date : {date_now}', merge_info)

# Add Number Iteration
worksheet_mov_in.write('A14:A14', 'No.', merge_format_number)
    # Merge necessary column
worksheet_mov_in.merge_range('A7:Q7', 'Depot In Container List (Consignee Return)', font_size_title)
# Un-bold the number iteration
for row_num, value in enumerate(df_mov_in.index.get_level_values(level=0)):
    worksheet_mov_in.write(row_num+14, 0, value, column_number_format)

isempty = df_mov_in.empty
if isempty!=False:
    
    worksheet_mov_in.set_column(0, 0, 5, align_center)
    worksheet_mov_in.set_column(1, 1, 13, align_center)
    worksheet_mov_in.set_column(2, 4, 5, align_center)
    worksheet_mov_in.set_column(7, 7, 5, align_center)
    worksheet_mov_in.set_column(8, 12, 13, align_center)
    worksheet_mov_in.set_row(13, 13, align_center)

else:
    
    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_mov_in.set_column(0,len(df3.columns),15,border_fmt)


    # Format column Text Align
    worksheet_mov_in.set_column('A:T', None, align_center) 
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
    worksheet_mov_in.set_column(6, 8, 10)
    #worksheet_mov_in.set_column(7, 7, 20)
    
    
    
    # Add Border
    #border_fmt = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
    #worksheet_stock_list.conditional_format(xlsxwriter.utility.xl_range(6, 0, len(df_stock_list.index), len(df_stock_list.columns)), {'type': 'no_errors', 'format': border_fmt})
    