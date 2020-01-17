import json
import unittest
import requests
from parameterized import parameterized
from api.login import LoginApi
from app import BASE_DIR


def login_mag():
    Ldata = []
    with open(BASE_DIR + "/data/login_data.json","r",encoding="utf-8") as f:
        data = json.load(f)
        # print(data)
        for n in data:
            username = n.get("username")
            password = n.get("password")
            verify_code = n.get("verify_code")
            yzm_code = n.get("yzm_code")
            login_code = n.get("login_code")
            status = n.get("status")
            msg = n.get("msg")
            Ldata.append((yzm_code,username,password,verify_code,login_code,status,msg))
    print("登录测试数据的获取",Ldata)
    return Ldata

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        # login_mag()

    def setUp(self) -> None:
        self.session = requests.Session()
    def tearDown(self) -> None:
        self.session.close()

    # 登陆成功
    @parameterized.expand(login_mag())
    def test01_Login(self,yzm_code,usernamee, password, verify_code,login_code,status,msg):
        # 获取验证码
        response = self.login_api.get_login_verify_code(self.session)
        # 断言
        self.assertEqual(yzm_code, response.status_code)
        # 登录
        response = self.login_api.login(self.session, usernamee, password, verify_code)
        json_data = response.json()
        print(json_data)
        # 断言
        self.assertEqual(login_code, response.status_code)
        self.assertEqual(status, json_data.get("status"))
        self.assertIn(msg, json_data.get("msg"))
