# encoding: utf-8
# Author    : Davide<m13632721415@163.com >
# Datetime  : 2023/3/15 17:48
# User      : chenqang
# Product   : PyCharm
# Project   : youstar_apitest
# File      : test_youstar_login.py
# explain   : 文件说明
import pytest
from api.login.login_api import iphone_login
import allure
import os
from common.resd_yaml import readyml

current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
login_yml = os.path.join(current_directory, "data", "login.yml")
loginparams_data = readyml(login_yml)["loginparams_info"]
print(loginparams_data)


# 第一种方法
class TestYoustarLogin(object):
    @pytest.mark.smoke
    @allure.severity("blocker")
    @allure.story("登录成功用例")
    @allure.title("输入正确账号密码登录")
    def test_login_success(self):
        """登录成功"""
        r = iphone_login("+8613632721415", "950720")
        assert r.json()["code"] == 0
        assert len(r.json()["data"].get("uid")) == 24
        assert r.json()["msg"] == ''

    @allure.story("登录失败用例")
    @pytest.mark.parametrize('account, password,title', [
        [" ", "950720", "账号为空"],
        ["+8613632721415", " ", ",密码为空"],
        ["+86136327214123235", "950720", "账号错误"],
        ["+8613632721415", "950720ewwe", "密码错误"]
    ])
    def test_login_fail(self, account, password, title):
        allure.dynamic.title(title)
        r = iphone_login(account, password)
        assert r.json()["code"] != 0
        assert r.json()["data"] == {}

    # 第二种方法
    @allure.story("参数化登录用例")
    @pytest.mark.parametrize("test_input,expected,title", loginparams_data)
    def test_login_params(self, test_input, expected, title):
        """参数化账号登录"""
        allure.dynamic.title(title)
        r = iphone_login(**test_input)
        assert r.json().get("code") == expected["code"]
        assert r.json().get("msg") == expected["msg"]
