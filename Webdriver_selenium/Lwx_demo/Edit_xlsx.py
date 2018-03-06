# coding=utf-8
import xlrd, os


class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # Get 第一行作为key的值
        self.keys = self.table.row_values(0)
        # Get 总行数
        self.rowNum = self.table.nrows
        # Get 总列数
        self.colNum = self.table.ncols

    @property
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1行")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
                return r


if __name__ == '__main__':
    path_dir = os.getcwd()
    excelPath = path_dir + "\\test.xls"
    print(excelPath)
    sheetName = u'Sheet1'
    data = ExcelUtil(excelPath, sheetName)
    print(data.dict_data)
