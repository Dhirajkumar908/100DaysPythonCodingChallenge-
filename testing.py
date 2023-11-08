from openpyxl import Workbook
import datetime
wb=Workbook()
ws=wb.active
print(wb.sheetnames)
for sheet in wb:
    print( sheet.title)
treeData=[["Type", "Leaf Color", "Height"], ["Maple", "Red", 549], ["Oak", "Green", 783], ["Pine", "Green", 1204]]

for row in treeData:
    ws.append(row)


wb.save('mysheet.csv')