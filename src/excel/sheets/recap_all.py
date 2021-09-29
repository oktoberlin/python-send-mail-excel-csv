from src.excel.excel_format import *
from src.excel.query_sql.sql_recapAll2 import *

# SHEET STOCK LIST #
df_recapAll = pd.read_sql_query(sql_recapAll, db) #Read the sql query
df_recapAll.index += 1 #Add index by 1

#df_stock_list.to_excel(writer, sheet_name='STOCK LIST', startrow=4)
df_recapAll.to_excel(writer, sheet_name='RECAP ALL', startrow=8, header=False, index=False, startcol=1)

df_recapAll_preStock = pd.read_sql_query(sql_recapAll_preStock, db)
df_recapAll_preStock.to_excel(writer, sheet_name='RECAP ALL', index=False, header=False, startrow=df_recapAll.shape[0] + 8,startcol=1)

df_recapAll_mov_in = pd.read_sql_query(sql_recapAll_move_in, db)
df_recapAll_mov_in.to_excel(writer, sheet_name='RECAP ALL', index=False, header=False, startrow=df_recapAll.shape[0] + 8,startcol=4)

df_recapAll_mov_in_avCondition = pd.read_sql_query(sql_recapAll_mov_in_avCondition, db)
df_recapAll_mov_in_avCondition.to_excel(writer, sheet_name='RECAP ALL', index=False, header=False, startrow=df_recapAll.shape[0] + 8,startcol=7)

df_recapAll_mov_in_dmgCondition = pd.read_sql_query(sql_recapAll_mov_in_dmgCondition, db)
df_recapAll_mov_in_dmgCondition.to_excel(writer, sheet_name='RECAP ALL', index=False, header=False, startrow=df_recapAll.shape[0] + 8,startcol=10)

df_recapAll_mov_in_dwCleaning = pd.read_sql_query(sql_recapAll_mov_in_dwCleaning, db)
df_recapAll_mov_in_dwCleaning.to_excel(writer, sheet_name='RECAP ALL', index=False, header=False, startrow=df_recapAll.shape[0] + 8,startcol=13)

df_recapAll_mov_in_wCleaning = pd.read_sql_query(sql_recapAll_mov_in_wCleaning, db)
df_recapAll_mov_in_wCleaning.to_excel(writer, sheet_name='RECAP ALL', index=False, header=False, startrow=df_recapAll.shape[0] + 8,startcol=16)

df_recapAll_mov_in_swCleaning = pd.read_sql_query(sql_recapAll_mov_in_swCleaning, db)
df_recapAll_mov_in_swCleaning.to_excel(writer, sheet_name='RECAP ALL', index=False, header=False, startrow=df_recapAll.shape[0] + 8,startcol=19)

df_recapAll_complete_repair = pd.read_sql_query(sql_recapAll_complete_repair, db)
df_recapAll_complete_repair.to_excel(writer, sheet_name='RECAP ALL', index=False, header=False, startrow=df_recapAll.shape[0] + 8,startcol=22)

df_recapAll_mov_out = pd.read_sql_query(sql_recapAll_mov_out, db)
df_recapAll_mov_out.to_excel(writer, sheet_name='RECAP ALL', index=False, header=False, startrow=df_recapAll.shape[0] + 8,startcol=25)

df_recapAll_stockList = pd.read_sql_query(sql_recapAll_stockList, db)
df_recapAll_stockList.to_excel(writer, sheet_name='RECAP ALL', index=False, header=False, startrow=df_recapAll.shape[0] + 8,startcol=28)

df_recapAll_avStockList = pd.read_sql_query(sql_recapAll_avStockList, db)
df_recapAll_avStockList.to_excel(writer, sheet_name='RECAP ALL', index=False, header=False, startrow=df_recapAll.shape[0] + 8,startcol=31)

df_recapAll_dmgStockList = pd.read_sql_query(sql_recapAll_dmgStockList, db)
df_recapAll_dmgStockList.to_excel(writer, sheet_name='RECAP ALL', index=False, header=False, startrow=df_recapAll.shape[0] + 8,startcol=34)


df_recapAll_stockListSummary = pd.read_sql_query(sql_recapAll_stockListSummary, db)
df_recapAll_stockListSummary.to_excel(writer, sheet_name='RECAP ALL', index=False, header=False, startrow=df_recapAll.shape[0] + 11,startcol=30)


df_recapAll_stockListBoxes = pd.read_sql_query(sql_recapAll_stockListBoxes, db)
df_recapAll_stockListBoxes.to_excel(writer, sheet_name='RECAP ALL', index=False, header=False, startrow=df_recapAll.shape[0] + 13,startcol=31)

worksheet_recapAll = writer.sheets['RECAP ALL']
worksheet_recapAll.set_tab_color('#7030A0')
worksheet_recapAll.protect()
worksheet_recapAll.set_column(0, 0, 20)
worksheet_recapAll.set_row(0, 26.25)

# Merge necessary column
worksheet_recapAll.merge_range('A1:S1', 'DAILY CONTAINER STOCK AND MOVEMENT REPORT', font_size_title)
worksheet_recapAll.merge_range('A3:E3', f'PRINCIPAL: {Principle_Code}', merge_info)
worksheet_recapAll.merge_range('A4:E4', f'{time_now}', merge_info)
worksheet_recapAll.merge_range('A5:A8', 'TYPE CNTR', merge_info_center)
worksheet_recapAll.merge_range('B5:D5', 'STOCK', merge_info_center)
worksheet_recapAll.merge_range('B6:D6', 'AWAL', merge_info_center)
worksheet_recapAll.merge_range('B7:D7', '', merge_info_center)

worksheet_recapAll.write('B8:B8', "20'", merge_info_center)
worksheet_recapAll.write('C8:C8', "40'", merge_info_center)
worksheet_recapAll.write('D8:D8', "45'", merge_info_center)

worksheet_recapAll.merge_range('E5:V5', 'IN WARD', merge_info_center)
worksheet_recapAll.merge_range('W5:Y5', 'COMPLETED', merge_info_center)
worksheet_recapAll.merge_range('Z5:AB5', 'TOTAL', merge_info_center)
worksheet_recapAll.merge_range('AC5:AK6', 'STOCK AKHIR', merge_info_center)

worksheet_recapAll.merge_range('E6:G7', 'TOTAL IN', merge_info_center)#worksheet.merge_range('G6:H6', 'Ex - Vessel', merge_format)

worksheet_recapAll.merge_range('H6:M6', 'CONDITION', merge_info_center)
worksheet_recapAll.merge_range('N6:V6', 'CLEANING', merge_info_center)
worksheet_recapAll.merge_range('W6:Y6', 'REPAIR', merge_info_center)
worksheet_recapAll.merge_range('Z6:AB6', 'OUT WARD', merge_info_center)

worksheet_recapAll.merge_range('H7:J7', 'AV', merge_info_center)
worksheet_recapAll.merge_range('K7:M7', 'DM', merge_info_center)
worksheet_recapAll.merge_range('N7:P7', 'D/W & C/W', merge_info_center)
worksheet_recapAll.merge_range('Q7:S7', 'W/W', merge_info_center)
worksheet_recapAll.merge_range('T7:V7', 'S/W', merge_info_center)
worksheet_recapAll.merge_range('W7:Y7', '', merge_info_center)
worksheet_recapAll.merge_range('Z7:AB7', '', merge_info_center)
worksheet_recapAll.merge_range('AC7:AE7', 'TODAY', merge_info_center)
worksheet_recapAll.merge_range('AF7:AH7', 'AV', merge_info_center)
worksheet_recapAll.merge_range('AI7:AK7', 'DMG', merge_info_center)

worksheet_recapAll.write('E8:E8', "20'", merge_info_center)
worksheet_recapAll.write('F8:F8', "40'", merge_info_center)
worksheet_recapAll.write('G8:G8', "45'", merge_info_center)

worksheet_recapAll.write('H8:H8', "20'", merge_info_center)
worksheet_recapAll.write('I8:I8', "40'", merge_info_center)
worksheet_recapAll.write('J8:J8', "45'", merge_info_center)

worksheet_recapAll.write('K8:K8', "20'", merge_info_center)
worksheet_recapAll.write('L8:L8', "40'", merge_info_center)
worksheet_recapAll.write('M8:M8', "45'", merge_info_center)

worksheet_recapAll.write('N8:N8', "20'", merge_info_center)
worksheet_recapAll.write('O8:O8', "40'", merge_info_center)
worksheet_recapAll.write('P8:P8', "45'", merge_info_center)

worksheet_recapAll.write('Q8:Q8', "20'", merge_info_center)
worksheet_recapAll.write('R8:R8', "40'", merge_info_center)
worksheet_recapAll.write('S8:S8', "45'", merge_info_center)

worksheet_recapAll.write('T8:T8', "20'", merge_info_center)
worksheet_recapAll.write('U8:U8', "40'", merge_info_center)
worksheet_recapAll.write('V8:V8', "45'", merge_info_center)

worksheet_recapAll.write('W8:W8', "20'", merge_info_center)
worksheet_recapAll.write('X8:X8', "40'", merge_info_center)
worksheet_recapAll.write('Y8:Y8', "45'", merge_info_center)

worksheet_recapAll.write('Z8:Z8', "20'", merge_info_center)
worksheet_recapAll.write('AA8:AA8', "40'", merge_info_center)
worksheet_recapAll.write('AB8:AB8', "45'", merge_info_center)

worksheet_recapAll.write('AC8:AC8', "20'", merge_info_center)
worksheet_recapAll.write('AD8:AD8', "40'", merge_info_center)
worksheet_recapAll.write('AE8:AE8', "45'", merge_info_center)

worksheet_recapAll.write('AF8:AF8', "20'", merge_info_center)
worksheet_recapAll.write('AG8:AG8', "40'", merge_info_center)
worksheet_recapAll.write('AH8:AH8', "45'", merge_info_center)

worksheet_recapAll.write('AI8:AI8', "20'", merge_info_center)
worksheet_recapAll.write('AJ8:AJ8', "40'", merge_info_center)
worksheet_recapAll.write('AK8:AK8', "45'", merge_info_center)

worksheet_recapAll.write('A9:A9', "FR", merge_info)
worksheet_recapAll.write('A10:A10', "GP", merge_info)
worksheet_recapAll.write('A11:A11', "GOH", merge_info)
worksheet_recapAll.write('A12:A12', "HC", merge_info)
worksheet_recapAll.write('A13:A13', "OT", merge_info)
worksheet_recapAll.write('A14:A14', "RF", merge_info)
worksheet_recapAll.write('A15:A15', "RH", merge_info)
worksheet_recapAll.write('A16:A16', "TOTAL (BOXES)", None)

worksheet_recapAll.write('A17:A17', "TOTAL (TEUS)", None)

worksheet_recapAll.merge_range('AC19:AD19', "Capasity Depo", merge_info_center)
worksheet_recapAll.write('AE19:AE19', "1.500", merge_info_center)
worksheet_recapAll.write('AF19:AF19', "teus", align_leftBold)

worksheet_recapAll.merge_range('AC20:AD20', "Capasity Used", merge_info_center)
worksheet_recapAll.write('AG20:AG20', "teus", align_leftBold)

worksheet_recapAll.merge_range('AC21:AD21', "Free Capasity", merge_info_center)
worksheet_recapAll.write('AG21:AG21', "teus", align_leftBold)

worksheet_recapAll.write('AG22:AG22', "boxes", align_leftBold)

worksheet_recapAll.conditional_format('AE21:AE21',
                                    {
                                    'type': 'no_errors',
                                    'format': percent_fmt,  
                                    })
worksheet_recapAll.conditional_format('AE20:AE20',
                                    {
                                    'type': 'no_errors',
                                    'format': percent_fmt,  
                                    })
#worksheet_recapAll.set_column('AE:AE',None,percent_fmt)
worksheet_recapAll.write('AE20:AE20', df_recapAll_stockListSummary.iloc[0,0], merge_info_center)
worksheet_recapAll.write('AE21:AE21', df_recapAll_stockListSummary.iloc[1,0], merge_info_center)
#worksheet_recapAll.set_column('AE21:AE21',None,percent_fmt)

'''
worksheet_recapAll.write(11,30, df_recapAll_stockListSummary.iloc[0,0], merge_info_center)
#worksheet_recapAll.write('AE21:AE21', df_recapAll_stockListSummary.iloc[1,1], merge_info_center)


#worksheet_recapAll.set_selection('B17:D17')

worksheet_recapAll.write('E17:G17', "45'", merge_info_center)
worksheet_recapAll.write('W17:Y17', "45'", merge_info_center)
worksheet_recapAll.write('Z17:AB17', "45'", merge_info_center)
worksheet_recapAll.write('AC17:AE17', "45'", merge_info_center)
'''

worksheet_recapAll.merge_range('B17:D17', df_recapAll_preStock.iloc[0,0], merge_info_center)
worksheet_recapAll.merge_range('E17:G17', df_recapAll_mov_in.iloc[0,0], merge_info_center)
worksheet_recapAll.merge_range('H17:J17', df_recapAll_mov_in_avCondition.iloc[0,0], merge_info_center)
worksheet_recapAll.merge_range('K17:M17', df_recapAll_mov_in_dmgCondition.iloc[0,0], merge_info_center)
worksheet_recapAll.merge_range('N17:P17', df_recapAll_mov_in_dwCleaning.iloc[0,0], merge_info_center)
worksheet_recapAll.merge_range('Q17:S17', df_recapAll_mov_in_wCleaning.iloc[0,0], merge_info_center)
worksheet_recapAll.merge_range('T17:V17', df_recapAll_mov_in_swCleaning.iloc[0,0], merge_info_center)
worksheet_recapAll.merge_range('W17:Y17', df_recapAll_complete_repair.iloc[0,0], merge_info_center)
worksheet_recapAll.merge_range('Z17:AB17', df_recapAll_mov_out.iloc[0,0], merge_info_center)
worksheet_recapAll.merge_range('AC17:AE17', df_recapAll_stockList.iloc[0,0], merge_info_center)
worksheet_recapAll.merge_range('AF17:AH17', df_recapAll_avStockList.iloc[0,0], merge_info_center)
worksheet_recapAll.merge_range('AI17:AK17', df_recapAll_dmgStockList.iloc[0,0], merge_info_center)
#worksheet_recapAll.merge_range('B17:D17', '=SUM(C16+D16)*2+B16', None)

worksheet_recapAll.set_column('B:AK', None, align_center)

'''
dicts = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
,'AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK']
for dict in dicts:
    worksheet.write(f"{dict}16", f"={dict}9+{dict}10+{dict}11+{dict}12+{dict}13+{dict}14+{dict}15",None)
'''
no_border_format = workbook.add_format({'bottom':0, 'top':0, 'left':0, 'right':0})
worksheet_recapAll.conditional_format( 'A1:AK4' , { 'type' : 'no_errors' , 'format' : no_border_format} )

border_format = workbook.add_format({'bottom':1, 'top':1, 'left':1, 'right':1})
worksheet_recapAll.conditional_format( 'A5:AK17' , { 'type' : 'no_errors' , 'format' : border_format} )

worksheet_recapAll.conditional_format( 'AC19:AE21' , { 'type' : 'no_errors' , 'format' : border_format} )
worksheet_recapAll.conditional_format( 'AF20:AF22' , { 'type' : 'no_errors' , 'format' : border_format} )


#worksheet_recapAll.set_column('A:Z', None, fmt)
#worksheet_recapAll.set_row(0, None, fmt)