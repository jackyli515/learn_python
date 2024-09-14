# 与HTTP服务交互的三种方式:
# 1、内置包urllib.request
# 2、三方包requests，灵活性高 pip install requests
# https://requests.readthedocs.io/en/latest/
# 3、

# 在要同一个真正的站点进行交互前，先在 httpbin.org 这样的网站上做实验常常是
# 可取的办法。尤其是当我们面对 3 次登录失败就会关闭账户这样的风险时尤为有用（不
# 要尝试自己编写 HTTP 认证客户端来登录你的银行账户）。
# 除了正式服务 ，日常测试和验证可以使用http://httpbin.org/


# 问题01：cookie的处理
#  http://httpbin.org/cookies
# https://requests.readthedocs.io/en/latest/user/quickstart/#cookies

import os


def __save_cookie():
    """
    存储cookies, username用于文件命名

    Parameters

    """

    # 将转换成字典格式的RequestsCookieJar（这里我用字典推导手动转的）保存到LWPcookiejar中
    # requests.utils.cookiejar_from_dict(
    #     {c.name: c.value for c in self.s.cookies}, self.cookie_jar
    # )

    # 保存到本地文件
    cookie_jar.save(cookie_file_path, ignore_discard=True, ignore_expires=True)
    # with open(cookie_file_path, "w") as f:
    #     f.write(tt)


def __read_cookie():
    """
    读取cookies, biz用于文件命名

    """

    try:
        cookie_jar.load(cookie_file_path, ignore_discard=True, ignore_expires=True)
        print(f"Loaded cookies from {cookie_file_path}")
        try:
            with open(cookie_file_path, "r") as f:
                tt = f.read()
                print(f"读取token={tt}")
        except FileNotFoundError:
            pass
    except FileNotFoundError:
        print(f"{cookie_file_path} not found. Creating a new one.")


import requests
from requests.cookies import cookielib

cookie_file_path = "tmp/cookies/tt.txt"
cookie_path = os.path.dirname(cookie_file_path)
if not os.path.exists(cookie_path):
    os.makedirs(cookie_path)
    print(f"创建文件夹成功:{cookie_path}")
session = requests.session()

cookie_jar = cookielib.LWPCookieJar()
session.cookies = cookie_jar
__read_cookie()
url = "http://httpbin.org/cookies/set/username/tt"
res = session.get(url)
__save_cookie()
print(res.text)
