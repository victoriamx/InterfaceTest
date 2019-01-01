import xlrd

def excel_to_list(data_file,sheet):
    data_list=[]
    wb=xlrd.open_workbook(data_file).sheet_by_name(sheet)
    header=wb.row_values(0)
    for i in range(1,wb.nrows):
        d=dict(zip(header,wb.row_values(i)))#将标题和每行数据组装成字典
        data_list.append(d)
    return data_list

def get_test_data(datalist,case_name):
    for item in datalist:
        if case_name==item['case_name']:
            return item

if __name__=='__main__':
    case_data=get_test_data(excel_to_list('test_user_data.xlsx','TestUserLogin'),'test_user_login_normal')
    print(case_data)