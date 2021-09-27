import pandas as pd
from openpyxl import Workbook
from sources.excel.time import time_now_filename,date_now
from sources.excel.queries import *
from sources.database.database import db

Client = 'MSC'
# File name
file_name = f'REPORT-{Client}-{time_now_filename}.xlsx'
# give the excel filename

excel_filename = f'excel-output/{file_name}'

# Writing Database into Excel
writer = pd.ExcelWriter(excel_filename, engine='openpyxl')

# Formatting Excel File
workbook = writer.book

#workbook.formats[0].set_font_size(10)
#workbook.formats[1].set_font_size(10)
#workbook.formats[0].set_font_name('Arial Narrow')
#workbook.formats[1].set_font_name('Arial Narrow')

cell_format=workbook.add_format()

#fmt.set_font_size(10)
#fmt.set_font_name('Arial Narrow')

cell_format.set_font_name('Arial Narrow')
cell_format.set_font_size(10)
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
    'bold': True
})

align_center = workbook.add_format()
align_center.set_align('center')
align_center.set_align('vcenter')

align_left = workbook.add_format({
    'text_wrap': True,
})
align_left.set_align('left')
align_left.set_align('vcenter')

font_size_title = workbook.add_format({
    'font_size':12,
    'bold':True,
    'align':'center',
})

header_format = workbook.add_format({
    #'bold': True,
    'text_wrap': True,
    'valign': 'vcenter',})