from openpyxl import load_workbook


def read_excel_dict(file, sheet_name):
    # 读取excel数据

    # 得到wb

    wb = load_workbook (file)

    # 得到sheet，web["Sheet_name"]

    sheet = wb[sheet_name]

    # 得到所有数据

    data = list (sheet.values)

    # 获取所有标题

    titles = data[0]

    # 转化成字典

    rows = [dict (zip (titles, row)) for row in data[1:]]

    return rows
