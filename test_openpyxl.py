from sources.database.database import db
from sources.excel.queries import sql_mov_in
from openpyxl.styles import DEFAULT_FONT
from openpyxl import Workbook

def main():

    # Connect to DB -----------------------------------------------------------
    cur = db.cursor()

    # Create Excel (.xlsx) file -----------------------------------------------
    wb = Workbook()

    cur.execute(sql_mov_in)
    results = cur.fetchall()
    ws = wb.create_sheet('MOVE IN')
    ws.font.size=10
    #ws.append(cur.column_names)
    for row in results:
        ws.append(row)
    
    workbook_name = "test_workbook"
    wb.save(workbook_name + ".xlsx")
    db.commit()

if  __name__ =='__main__':main() 