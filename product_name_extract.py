import csv
import openpyxl

with open('New GB sheet.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    
    next(reader)

    item_names = [row[6] for row in reader]  

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Item Names"

for index, name in enumerate(item_names, start=1):
    sheet.cell(row=index, column=1, value=name)

workbook.save('item_names.xlsx')