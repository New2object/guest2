# coding=utf-8
import xlrd, xlwt
from datetime import date

file_path = './ExcelFile/demo.xls'
xlrd.Book.encoding = 'utf-8'
data = xlrd.open_workbook(file_path)
sheet_name = data.sheet_names()

table = data.sheet_by_index(0)
print(table)

rows_count = table.nrows  # 取总行数
print(rows_count)
cols_count = table.ncols  # 取总列数

row_data = table.row_values(0)
print(type(row_data))
col_data = table.col_values(0)
print(col_data)

datas = row_data[0]
print(datas)

# 获取某个单元格的值
cell_data = row_data[2]
cell_data_AL = table.cell(1, 1).value
print(cell_data)
print(cell_data_AL)

# 循环读取所有数据
for row in range(0, rows_count):
    for col in range(0, cols_count):
        data1 = table.cell(row, col).value
        print(data1, end='|')
    print('\n')

print(table.cell(1, 6).ctype)  # ['时间',42993.0,'2017.01.12',40900.0]
print(table.cell(2, 6).ctype)  # CType = 1 # 类型 0--empty, 1--string,2--number,3--date,4--boolean,5--error
print(table.cell(3, 6).ctype)
data2 = table.cell(0, 1)  # cell(row,col)
print(data2)

date_value = xlrd.xldate_as_tuple(table.cell_value(1, 6), data.datemode)
print(date_value)

print(date(*date_value[:3]))  # [:3] 切片,切到顺位第三个字符
print(date(*date_value[:3]).strftime('%Y/%m/%d'))  # 转换成字符串

# So,当我们循环读取并打印的时候,可以做一个判断,如果数据的Ctype为3，就做这样一个转换
for row in range(0, rows_count):
    for col in range(0, cols_count):
        if (table.cell(row, col).ctype == 3):
            date_value = xlrd.xldate_as_tuple(table.cell_value(row, col), data.datemode)
            data1 = date(*date_value[:3]).strftime('%Y/%m/%d')
        else:
            data1 = table.cell(row, col).value
        print(data1, end=' ')

    print('\n')

# 简单的Write Data

row = 1
col = 0
ctype = 1  # 类型 0--empty,1--string,2--number,3-date,4-boolean,5--error
value = '狂战士'
xf = 0  # 扩展的格式化 (默认是0)
table.put_cell_unragged(row, col, ctype, value, xf)
table.put_cell(row, col, ctype, value, xf)  # 只是暂时的修改,而且只能是修改已有的数据

for row in range(0, rows_count):
    for col in range(0, cols_count):
        if (table.cell(row, col).ctype == 3):
            date_value = xlrd.xldate_as_tuple(table.cell_value(row, col), data.datemode)
            data1 = date(*date_value[:3]).strftime('%Y/%m%d')
        else:
            data1 = table.cell(row, col).value
            print(data1, end=' ')
    print('\n')

# 关于合并的单元格的读取
workbook = xlrd.open_workbook('./ExcelFile/demo2.xlsx')
table2 = workbook.sheet_by_index(0)
print(table2.merged_cells)

# 创建工作簿,工作表
myWorkbook = xlwt.Workbook()  # Create JobFile
mysheet = myWorkbook.add_sheet('A Test Sheet')  # Create Job table

# 创建DataType,写入数据
myStyle = xlwt.easyxf('font: name Times New Roman, color-index red,bold on', num_format_str='#,##0.00')  # DataType
mysheet.write(3, 0, 'ADC', myStyle)  # 写数据的时候可以用这个格式,也可以不用
mysheet.write(2, 0, 1)  # 写入A3,数值等于1
mysheet.write(2, 1, 1)  # 写入B3,数值等于1
mysheet.write(2, 2, xlwt.Formula("A3+B3"))  # 写入C3,数值等于2

myWorkbook.save('./ExcelFile/test.xls')
