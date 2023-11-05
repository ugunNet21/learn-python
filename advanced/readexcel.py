import openpyxl

# Buka file Excel
workbook = openpyxl.load_workbook("file.xlsx")

# Dapatkan sheet pertama
sheet = workbook.worksheets[0]

# Cetak nama kolom
for column in sheet.columns:
    print(column[0].value)

# Cetak data dari baris pertama
for row in sheet.rows:
    for cell in row:
        print(cell.value, end=" ")
    print()

