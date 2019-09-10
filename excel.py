
def get_column_val():
    wb = openpyxl.load_workbook('demo.xlsx')
    sheet = wb.get_sheet_by_name('Sheet1')
    for i in range(1, sheet.max_row+1):
        yield sheet['A'+str(i)].value

import openpyxl
for data in get_column_val():
    print(data)