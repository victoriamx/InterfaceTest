import unittest,requests,json,sys
from config import *
from read_excel import *

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #公共属性
        cls.datalist=excel_to_list(os.path.join(data_path,'test_user_data.xlsx'),'TestUserLogin')

    def test_user_login_normal(self):
        case_data=get_test_data(self.datalist,'test_user_login_normal')
        if not case_data:
            print("error")

        url=case_data.get('url')
        data=case_data.get('data')
        expect_res=case_data.get('expect_res')

        res=requests.post(url=url,data=json.loads(data))
        self.assertEqual(res.text,expect_res)


