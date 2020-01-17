
# 封装登录
class LoginApi:

    def __init__(self):
        # 验证码URL
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        # 登录URL
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 定义获取验证码方法
    def get_login_verify_code(self,session):
        # 返回验证码接口
        return session.get(self.verify_url)

    # 定义登录方法
    def login(self, session, username, password, verify_code):
        # 登录数据
        login_data = {
            "username": username,
            "password": password,
            "verify_code": verify_code
        }
        # 返回登陆接口
        return session.post(self.login_url, data=login_data)
