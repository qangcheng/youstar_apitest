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

commonbody = get_filed("login.yml", "common_body")
commonprames = get_filed("login.yml", "common_prams")
new_versioncode = "new_versioncode=" + commonprames['new_versioncode']
debug = "debug=" + commonprames['debug']
url = "https://testv2.qmovies.tv/login_service/register_or_login?" + new_versioncode + '&' + debug


def iphone_login(account, password):
    """
    :param account:  手机登录账号
    :param password: 手机登录密码
    :return:
    """
    body = {
        "account": account,
        "password": password
    }
    body.update(commonbody)
    r = requests.post(url, json=body)
    token = r.json()['data'].get('token')
    uid = r.json()['data'].get('uid')
    roomId = r.json()['data'].get('roomId')
    # print(token, uid, roomId)
    print(r.json())
    # return token, uid, roomId
    return r


def vip_login():
    pass


if __name__ == '__main__':
    a = iphone_login(" 2323232323", "950720")
