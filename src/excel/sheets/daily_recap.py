from src.excel.excel_format import *
from src.excel.query_sql.sql_dailyRecap import sql_dailyRecap

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