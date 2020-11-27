import xlrd

def my_function():
    book = xlrd.open_workbook("F:/Python/GR/Input_Output/Content/run_input.xlsx")
    sh = book.sheet_by_index(0)
    #print("Sheetname:{0} Rows:{1} Columns:{2}". format(sh.name, sh.nrows, sh.ncols))
    data = [[sh.cell_value(r, c) for c in range(sh.ncols)] for r in range(sh.nrows)]
    #print(data)
    return data