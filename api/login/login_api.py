# encoding: utf-8
# Author    : Davide<m13632721415@163.com >
# Datetime  : 2022/12/9 15:29
# User      : chenqang
# Product   : PyCharm
# Project   : yourstar_api_test
# File      : login_api.py
# explain   : 文件说明

import requests
from common.get_fields import get_filed


class LoginApi(object):
    """登录接口"""

    def __init__(self):
        self.commonbody = get_filed("login.yml", "common_body")
        self.commonprames = get_filed("login.yml", "common_prams")
        self.new_versioncode = "new_versioncode=" + self.commonprames['new_versioncode']
        self.debug = "debug=" + self.commonprames['debug']
        self.url = "https://testv2.qmovies.tv/login_service/register_or_login?" + self.new_versioncode + '&' + self.debug

    def iphone_login(self, account, password):
        """
        :param account:  手机登录账号
        :param password: 手机登录密码
        :return: 
        """
        body = {
            "account": account,
            "password": password
        }
        body.update(self.commonbody)
        r = requests.post(self.url, json=body)
        token = r.json()['data'].get('token')
        uid = r.json()['data'].get('uid')
        roomId = r.json()['data'].get('roomId')
        print(token, uid, roomId)
        return token, uid, roomId

    def vip_login(self, Account, password):
        pass


if __name__ == '__main__':
    a = LoginApi()
    reul = a.iphone_login("+8613632721415", "950720")
    print(reul[2])

